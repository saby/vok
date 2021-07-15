# API сервиса «Всё о компаниях»

**Демо-стенд**

Демо-стенд доступен без авторизации  
https://api.sbis.ru/vok-demo/  
Для демо-версии доступны ИНН:  
7605016030 — Тензор  
7736050003 — Газпром  
7707049388 — Ростелеком  

Пример запроса:  
[https://api.sbis.ru/vok-demo/req?inn=7605016030](https://api.sbis.ru/vok-demo/req?inn=7605016030)

**Методы**

req - основные реквизиты контрагента [подробное описание](doc/req/README.md)

tenders, tenders-info, customers, rivals - данные о торгах [подробное описание](doc/tenders/README.md)

owners, affiliate, dirs-history - данные о лицах связанных с контрагентом [подробное описание](doc/affiliate/README.md)

subscriptions/(events, contractors, subscribe, unsubscribe) - данные о событиях, подписка на них [подробное описание](doc/subscriptions/README.md)

pdf - карточка контрагента в формате pdf [подробное описание](doc/pdf/README.md)

finance, cost-business, reliability, market-position, creditworthiness - данные об аналитике [подробное описание](doc/finance/README.md)

statistic-courts, courts, executive-lists - данные о судах контрагента [подробное описание](doc/courts/README.md)

bankruptcy - данные о банкротстве контрагента [подробное описание](doc/bankruptcy/README.md)

fea-stat - статистика о внешнеэкономической деятельности контрагента [подробное описание](doc/fea/README.md)

license/(stat, data) - лицензии и сертификаты контрагента [подробное описание](api/license/README.md)

sro - присутствие контрагента в СРО [подробное описание](doc/sro/README.md)

inspections/(stat, data) - проверки контрагента [подробное описание](doc/inspections/README.md)

vacancies/(stat, data) - вакансии контрагента [подробное описание](doc/vacancies/README.md)

trademarks, trademarks/image - товарные знаки контрагента [подробное описание](spp_api/modules/Patent/README.md)

contractor_history - История изменений контрагента [подробное описание](doc/history/README.md)
