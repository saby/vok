## Логотип контрагента.

Получить логотип контрагента. 
Можно определить есть ли он по ключу has_logo в методе req.

**Ограничения по лицензии**:

Доступен в базовой версии лицензии

**URL** : `/logo`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
File/null
```

**Пример запроса**

```text
https://api.sbis.ru/vok/logo?inn=7712040126
```

***

##Регистрация контрагента.

Получить информацию о регистрации контрагента.

**Ограничения по лицензии**:

Доступен в базовой версии лицензии

**URL** : `/registration-information`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "object",
  "properties": {
    "pfr": {
      "description": "Информация о ПФР",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "registration_date": {
              "description": "Дата регистрации",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "withdrawal_date": {
              "description": "Дата снятия",
              "type": "string"
            }
          }
        }
      ]
    },
    "fss": {
      "description": "Информация о ФСС",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "registration_date": {
              "description": "Дата регистрации",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "withdrawal_date": {
              "description": "Дата снятия",
              "type": "string"
            }
          }
        }
      ]
    },
    "fns": {
      "description": "Информация о ФНС",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "registration_date": {
              "description": "Дата регистрации",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "withdrawal_date": {
              "description": "Дата снятия",
              "type": "string"
            }
          }
        }
      ]
    },
    "registration": {
      "description": "Информация о регистрации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "date": {
              "description": "Дата",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "way": {
              "description": "способ",
              "type": "string"
            }
          }
        }
      ]
    },
    "liquidation": {
      "description": "Информация о ликвидации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "date": {
              "description": "Дата",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "way": {
              "description": "способ",
              "type": "string"
            }
          }
        }
      ]
    },
    "accreditation": {
      "description": "Информация о аккредитации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "accreditation_date": {
              "description": "Дата аккредитации",
              "type": "string"
            },
            "accreditation_record_number": {
              "description": "Номер записи аккредитации",
              "type": "string"
            },
            "name": {
              "description": "Название организации",
              "type": "string"
            },
            "termination_date": {
              "description": "Дата прекращения аккредитации",
              "type": "string"
            },
            "renewal_date": {
              "description": "Дата продления",
              "type": "string"
            }
          }
        }
      ]
    }
  }
}
```

**Пример запроса**

```text
https://api.sbis.ru/vok/pdf/registration-information?inn=7712040126
```

***Пример ответа***
```json
{
  "pfr": [
    {
      "registration_date": "1992-04-13",
      "withdrawal_date": null,
      "name": "ПФР №5 по МО (Одинцовский р-н)2-5, ГУ"
    }
  ],
  "fss": [
    {
      "registration_date": "2000-02-18",
      "withdrawal_date": null,
      "name": "Филиал №29 Государственного учреждения - Московского регионального отделения Фонда социального страхования Российской Федерации"
    }
  ],
  "registration": [
    {
      "date": "2019-01-31",
      "name": "Администрация Одинцовского района Московской области ",
      "way": "Создание юридического лица до 01.07.2002"
    }
  ],
  "liquidation": [
    {
      "date": "2012-08-27",
      "name": "Межрайонная инспекция ФНС России №46 по г.Москве",
      "way": "Прекращение деятельности ЮЛ на основании п.2 ст.21.1 ФЗ от 08.08.2001 №129-ФЗ"
    }
  ],
  "accreditation": [
    {
      "name": "МИ ФНС №47 по г.Москве",
      "accreditation_record_number": "10160001214",
      "accreditation_date": "2016-09-07",
      "termination_date": null,
      "renewal_date": null
    }
  ]
}
```
