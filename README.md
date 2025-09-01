# API сервиса «Всё о компаниях»

###Клиент для Python3

https://pypi.org/project/sabyvok/

[README](client-py/README.md)

###Демо-стенд

Демо-стенд доступен без авторизации. Дальше к адресной строке добавляется метод и параметры запроса.  
https://api.sbis.ru/vok-demo/  
https://sbis.ru/contragents_api_demo - интерфейс для демо стенда

Для демо-версии доступны ИНН:  
7605016030 — Тензор  
7736050003 — Газпром  
7707049388 — Ростелеком  
7814593627 — Бодрус  
7827004484 — Концерн ТИТАН-2  
772871281410 — Чепенко Владимир Анатольевич, ИП  
6382082839 — Межрайонная ИФНС России № 23 по Самарской Области  
7708503727 — РЖД  
7709464710 — Эталонинвест  

В демо-версии не доступны методы отдающие файлы



###Получение данных

**Авторизация**

Подробно об авторизации - [https://sbis.ru/help/integration/api/auth](https://sbis.ru/help/integration/api/auth). Интересующие пункты: "Добавить приложение" и "Настроить сервисную авторизацию".

**Запрос**

Общение с API происходит по url: https://api.sbis.ru/vok/. Дальше к адресной строке добавляется метод, например получение реквизитов (req) - https://api.sbis.ru/vok/req.
В конце добавляются параметры запроса, например вот таким запросом можно получить данные о компании Газпром - https://api.sbis.ru/vok/req?inn=7736050003.
Метод http запроса и параметры запроса описаны для каждого метода в отдельном README.
Во все запросы нужно подавать headers как указано в статье об авторизации.
При отсутствии лицензии на API ВОК в ответе на запрос будет возвращаться код http ошибки - 403

**Массовые запросы**

Массовыми являются все методы, исключая методы отдающие файлы, поисковые методы и методы событий. Статистика по запросам клиента также не массовая.

Количество реквизитов ограничено 20 значениями.

Единовременно можно подавать только 1 тип реквизитов - ИНН или ОГРН.

Количество дневных запросов будет вычисляться из количества поданных в массвый запрос реквизитов (ИНН, ОГРН).

КПП дополняет только реквизит ИНН.

Если подаётся пара ИНН + КПП они должны идти до одиночных ИНН в списках реквизитов.

Формат ответа для всех массовых методов начинается так
```json
{
  "type": "array",
  "items": [
    {
      ...
    }
  ]
}
```

Пример запроса:  
[https://api.sbis.ru/vok-demo/req?inn=7605016030&inn=7736050003](https://api.sbis.ru/vok-demo/req?inn=7605016030&inn=7736050003)



**Методы**

req - основные реквизиты контрагента [подробное описание](doc/req/req.md)

logo, registration-information - логотип и регистрационные данные контрагента [подробное описание](doc/req/README.md)

tenders, tenders-info, customers, rivals - данные о торгах [подробное описание](doc/tenders/README.md)

owners, affiliate, dirs-history, founders-history - данные о лицах связанных с контрагентом [подробное описание](doc/affiliate/README.md)

subscriptions/(events, contractors, subscribe, unsubscribe) - данные о событиях, подписка на них [подробное описание](doc/subscriptions/README.md)

pdf/(business-report, due-diligence-report, financial-report, signed-excerpt), xml/(egrul-excerpt, reporting-excerpt) -  [подробное описание](doc/pdf/README.md)

[finance](doc/finance/finance.md), [cost-business](doc/finance/cost-business.md), [reliability](doc/finance/reliability.md), [reliability/blocks](doc/finance/reliability_blocks.md), [market-position](doc/finance/market-position.md), [creditworthiness](doc/finance/creditworthiness.md) - данные об аналитике 

statistic-courts, courts, executive-lists - данные о судах контрагента [подробное описание](doc/courts/README.md)

[bankruptcy](doc/bankruptcy/bankruptcy.md), [bankruptcy/file](doc/bankruptcy/bankruptcy_file.md) - данные о банкротстве контрагента

fea - статистика о внешнеэкономической деятельности контрагента [подробное описание](doc/fea/README.md)

license/(stat, data) - лицензии и сертификаты контрагента [подробное описание](doc/license/README.md)

sro, sro/file - присутствие контрагента в СРО [подробное описание](doc/sro/README.md)

inspections/(stat, data) - проверки контрагента [подробное описание](doc/inspections/README.md)

vacancies/(stat, data) - вакансии контрагента [подробное описание](doc/vacancies/README.md)

trademarks, trademarks/image - товарные знаки контрагента [подробное описание](doc/trademarks/README.md)

contractor-history - История изменений контрагента [подробное описание](doc/history/README.md)

contacts-official - Контактные данные контрагента [подробное описание](doc/contacts/README.md)

excerpts/(list, last, file) - Выписки контрагента [подробное описание](doc/excerpts/README.md)

search - Поисковые методы [подробное описание](doc/search/README.md)

branches - Филиалы контрагента [подробное описание](doc/branches/README.md)

client/stat - Статистика запросов клиента [подробное описание](doc/client/README.md)

pledges, pledges/file - Залог/Лизинг [подробное описание](doc/pledges/README.md)

vehicle, vehicle/stat - Автотранспорт [подробное описание](doc/vehicle/README.md)

events, events/file - События контаргента [подробное описание](doc/events/README.md)
