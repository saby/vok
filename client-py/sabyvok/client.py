import requests


def inn_or_ogrn(func):
    """
    Decorator checks inn or ogrn availability
    """
    def wrapper(*args, **kwargs):
        inn = args[1] if len(args) > 1 else kwargs.get('inn')
        ogrn = args[2] if len(args) > 2 else kwargs.get('ogrn')
        if not inn and not ogrn:
            raise NoInnOrOgrnError
        return func(*args, **kwargs)
    return wrapper


class NoInnOrOgrnError(Exception):
    """
    Raises on not enough arguments
    """


class SabyVokClient:
    _host = 'http://api.sbis.ru/vok/'
    _oauth_url = 'https://api.sbis.ru/oauth/service/'

    def __init__(self, client_id, secret, key):
        """
        Args:
            client_id (str): client id
            secret (str): client secret
            key (str): client service key
        """
        self._client_id = client_id
        self._secret = secret
        self._key = key
        self._session_id = None
        self._access_token = None

    @inn_or_ogrn
    def req(self, inn=None, ogrn=None, kpp=None):
        """
        Main requisites

        Args:
            inn (str): INN
            ogrn (str): OGRN
            kpp (str): KPP

        Returns:
            list: https://github.com/saby/vok/blob/main/doc/req/README.md
        """
        return self._get_main_data('req', inn, ogrn, kpp)

    @inn_or_ogrn
    def logo(self, inn=None, ogrn=None, kpp=None):
        """
        Logo

        Args:
            inn (str): INN
            ogrn (str): OGRN
            kpp (str): KPP

        Returns:
            binary: https://github.com/saby/vok/blob/main/doc/req/README.md
        """
        return self._get_main_data('logo', inn, ogrn, kpp)

    @inn_or_ogrn
    def registration_information(self, inn=None, ogrn=None, kpp=None):
        """
        Main requisites

        Args:
            inn (str): INN
            ogrn (str): OGRN
            kpp (str): KPP

        Returns:
            list: https://github.com/saby/vok/blob/main/doc/req/README.md
        """
        return self._get_main_data('registration-information', inn, ogrn, kpp)

    @inn_or_ogrn
    def tenders_info(self, inn=None, ogrn=None):
        """
        Tenders info

        Args:
            inn (str): INN
            ogrn (str): OGRN

        Returns:
            list: https://github.com/saby/vok/blob/main/doc/tenders/README.md
        """
        return self._get_main_data('tenders-info', inn, ogrn)

    @inn_or_ogrn
    def tenders(self, inn=None, ogrn=None, limit=10, page=0):
        """
        Tenders info

        Args:
            inn (str): INN
            ogrn (str): OGRN

        Returns:
            list: https://github.com/saby/vok/blob/main/doc/tenders/README.md
        """
        params = {
            'inn': inn,
            'ogrn': ogrn,
            'limit': limit,
            'page':  page,
        }
        return self._perform_request_json('tenders', params)

    def _get_main_data(self, url, inn=None, ogrn=None, kpp=None):
        """
        Get simple data

        Args:
            inn (str): INN
            ogrn (str): OGRN
            kpp (str): KPP

        Returns:
            (list|dict): Data from server
        """
        params = {
            'inn': inn,
            'ogrn': ogrn,
        }
        if kpp:
            params['kpp'] = kpp
        if url == 'logo':
            return self._perform_request_binary(
                url,
                params
            )
        return self._perform_request_json(
            url,
            params
        )

    @property
    def _request_headers(self):
        """
        Request headers with auth data

        Returns:
            dict: request headers
        """
        return {
            "User-Agent": "SabyVok Python Client / 1.0.1",
            "X-SBISAccessToken": self._saby_access_token,
            "X-SBISSessionId": self._saby_session_id,
            "Content-Type": "application/json; charset=utf-8",
        }

    @property
    def _saby_session_id(self):
        """
        Session id for request

        Returns:
            str: Saby session id
        """
        if self._session_id is None:
            self._obtain_saby_session()
        return self._session_id

    @property
    def _saby_access_token(self):
        """
        Access token for request

        Returns:
            str: Saby access token
        """
        if self._access_token is None:
            self._obtain_saby_session()
        return self._access_token

    def _obtain_saby_session(self):
        """
        Obtain session id from Saby
        """
        response = requests.post(
            self._oauth_url,
            json={
                "app_client_id": self._client_id,
                "app_secret": self._secret,
                "secret_key": self._key,
            }
        ).json()
        self._access_token = response['access_token']
        self._session_id = response['sid']

    def _perform_request(self, url, params, method='get'):
        """
        Performs the request to Saby API

        Args:
            url (str): url
            params (dict): get params

        Returns:
            requests.response: obtained data
        """
        full_url = f'{self._host}{url}'
        if method == 'post':
            return requests.post(full_url, params=params, headers=self._request_headers)
        else:
            return requests.get(full_url, params=params, headers=self._request_headers)

    def _perform_request_json(self, url, params, method='get'):
        """
        Returns json from server

        Args:
            url (str): url
            params (dict): get params

        Returns:
            (dict|list): obtained data
        """
        return self._perform_request(url, params, method).json()

    def _perform_request_binary(self, url, params, method='get'):
        """
        Returns json from server

        Args:
            url (str): url
            params (dict): get params

        Returns:
            binary: obtained data
        """
        return self._perform_request(url, params, method).content
