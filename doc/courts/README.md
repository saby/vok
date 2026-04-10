## Суды

Получение списка судов для ЮЛ, где ЮЛ истец или ответчик

**URL** : `/courts/`

**Обязательные параметры**
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `category(str)`: категория. по умолчанию 'all'
    - `all` Все суды 
    - `other` Иные 
    - `contractual` Договорные
    - `corporate` Корпоративные
    - `intellectual` Интеллектуальная собственность
    - `insolvency` О несостоятельности (банкротстве) организаций
    - `property` Споры по имущественным правам и иным вещным правам 
    - `non-contractual` Внедоговорные 
    - `government` Споры с государственными органами 
- `defendant (bool)` Ответчик ли - текущее ЮЛ. По умолчанию true
- `plaintiff (bool)` Истец ли - текущее ЮЛ. По умолчанию true
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы
- `case_source ([int])` - тип подсудности. 0 - Арбитражный суд, 1 - Суд общей юрисдикции, 2- Мировой суд, по дефолту все

**Ограничения по лицензии**:

В базовой версии лицензии доступны последние 5 дел в каждой роли (истец/ответчик) для категории "Все суды".

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "case_name": {
        "type": "string",
        "description": "Название дела (Истец, Ответчик, Исполнительный лист и тд)"
      },
      "date": {
        "type": "string",
        "description": "Дата суда"
      },
      "result": {
        "type": "string",
        "description": "Итог заседания"
      },
      "duration": {
        "type": "string",
        "description": "Продолжительность дела"
      },
      "cost": {
        "type": "number",
        "description": "Сумма"
      },
      "category": {
        "type": "string",
        "description": "Категория дела"
      },
      "status": {
        "type": "string",
        "description": "Статус дела"
      },
      "last_decision": {
        "type": "string",
        "description": "Последнее решение"
      },
      "case_source": {
        "type": "int",
        "description": "Тип подсудности"
      },
      "list_of_plaintiffs": {
        "type": "array",
        "description": "Список всех истцов",
        "items": {
          "type": "string"
        }
      },
      "list_of_defendants": {
        "type": "array",
        "description": "Список всех ответчиков",
        "items": {
          "type": "string"
        }
      },
      "stage": {
        "type": "array",
        "description": "Этапы",
        "items": {
          "type": "object",
          "properties": {
            "date": {
              "type": "string",
              "description": "Дата"
            },
            "authority": {
              "type": "string",
              "description": "Инстанция"
            },
            "note": {
              "type": "string",
              "description": "Примечание"
            }
          }
        }
      }
    }
  }
}
```

### Пример 
**Запрос** 
`/vok/courts?inn=7736050003&category=property&defendant=true`

**Ответ**
```json
[
  [
    {
      "date": "2026-03-12",
      "case_name": "Ответчик",
      "case_source": 0,
      "number_case": "А81-2894/2026",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром Добыча Надым, ООО"
      ],
      "list_of_defendants": [
        "Газпром, ПАО"
      ],
      "stage": [
        {
          "date": "2026-03-12",
          "authority": "АС Ямало-Ненецкого АО",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/ffae68c9-38f9-424f-92b9-48aa1bcdc396"
    },
    {
      "date": "2026-02-13",
      "case_name": "Истец",
      "case_source": 0,
      "number_case": "А50-3207/2026",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром, ПАО"
      ],
      "list_of_defendants": [
        "Министерство Строительства Пермского Края"
      ],
      "stage": [
        {
          "date": "2026-02-13",
          "authority": "АС Пермского края",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/b8b08aba-27a1-45a8-9db5-faa681bd2468"
    },
    {
      "date": "2026-02-13",
      "case_name": "Истец",
      "case_source": 0,
      "number_case": "А50-3207/2026",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром, ПАО"
      ],
      "list_of_defendants": [
        "Министерство Строительства Пермского Края"
      ],
      "stage": [],
      "duration": "1 мес., 24 дн.",
      "last_decision": "",
      "link": null
    },
    {
      "date": "2026-02-06",
      "case_name": "Истец",
      "case_source": 0,
      "number_case": "А56-12207/2026",
      "status": "Рассматривается в первой инстанции",
      "category": "об установлении фактов, имеющих юридическое значение",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром, ПАО"
      ],
      "list_of_defendants": [
        "Рубеж -М, ООО"
      ],
      "stage": [
        {
          "date": "2026-02-06",
          "authority": "АС города Санкт-Петербурга и Ленинградской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/4306d770-d2c8-4ae4-aaae-fd7b76cc380e"
    },
    {
      "date": "2026-01-07",
      "case_name": "Ответчик",
      "case_source": 0,
      "number_case": "А56-566/2026",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Трубичино, ООО"
      ],
      "list_of_defendants": [
        "Газпром Инвест, ООО (Газпром Инвест автотестовый филиал)",
        "Газпром, ПАО",
        "Газпром реконструкция, ООО"
      ],
      "stage": [
        {
          "date": "2026-01-07",
          "authority": "АС города Санкт-Петербурга и Ленинградской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/dc55a04c-d8ea-4578-b1fb-4ecfe10d1eda"
    },
    {
      "date": "2025-11-10",
      "case_name": "Истец",
      "case_source": 0,
      "number_case": "А44-6153/2025",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром, ПАО"
      ],
      "list_of_defendants": [
        "МТУ Росимущества В Псковской И Новгородской Областях, ФГКУ"
      ],
      "stage": [
        {
          "date": "2025-11-10",
          "authority": "АС Новгородской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/34c8b309-89f8-4da9-bc1a-43bf9a9fad6f"
    },
    {
      "date": "2025-09-25",
      "case_name": "Ответчик",
      "case_source": null,
      "number_case": "А13-10922/2025",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Упрдор \"Холмогоры\", ФКУ"
      ],
      "list_of_defendants": [
        "Газпром, ПАО"
      ],
      "stage": [
        {
          "date": "2025-09-25",
          "authority": "АС Вологодской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/7ed5b5c1-17c3-4508-ba43-1d6f79643411"
    },
    {
      "date": "2025-09-04",
      "case_name": "Истец",
      "case_source": 0,
      "number_case": "А47-15470/2025",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром, ПАО"
      ],
      "list_of_defendants": [
        "Администрация Северного Района"
      ],
      "stage": [
        {
          "date": "2025-09-04",
          "authority": "АС Оренбургской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/d5cc2327-e37a-49b3-bc36-0bb89bcc7a10"
    },
    {
      "date": "2025-05-21",
      "case_name": "Ответчик",
      "case_source": null,
      "number_case": "А81-4746/2025",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Газпром Трансгаз Югорск, ООО"
      ],
      "list_of_defendants": [
        "Газпром, ПАО"
      ],
      "stage": [
        {
          "date": "2025-05-21",
          "authority": "АС Ямало-Ненецкого АО",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/98e8e35a-ec0d-4a3f-b05e-cf338bf7f6a8"
    },
    {
      "date": "2025-04-30",
      "case_name": "Ответчик",
      "case_source": null,
      "number_case": "А56-39086/2025",
      "status": "Рассматривается в первой инстанции",
      "category": "экономические споры по гражданским правоотношениям",
      "cost": 0,
      "result": "",
      "list_of_plaintiffs": [
        "Евракон Бизнес, ООО"
      ],
      "list_of_defendants": [
        "Газпром Трансгаз Санкт-Петербург, ООО",
        "Газпром, ПАО"
      ],
      "stage": [
        {
          "date": "2025-04-30",
          "authority": "АС города Санкт-Петербурга и Ленинградской области",
          "note": "Рассматривается в первой инстанции"
        }
      ],
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "link": "http://kad.arbitr.ru/Card/e17fd42b-3dda-484e-b305-bd7c29070b94"
    }
  ]
]
```

## Карточка суда

Получение подробной информации о суде

**URL** : `/courts/get`

**Обязательные параметры**
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `number_case(str)` - Номер дела.

**Необязательные параметры** :
- `kpp(str)`: КПП контрагента

**Ограничения по лицензии**:

Доступно в базовой лицензии

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "case_name": {
        "type": "string",
        "description": "Название дела (Истец, Ответчик, Исполнительный лист и тд)"
      },
      "date": {
        "type": "string",
        "description": "Дата суда"
      },
      "case_source": {
        "type": "int",
        "description": "Тип подсудности"
      },
      "link": {
        "type": "string",
        "description": "Ссылка на суд"
      },
      "result": {
        "type": "string",
        "description": "Итог заседания"
      },
      "duration": {
        "type": "string",
        "description": "Продолжительность дела"
      },
      "number_case": {
        "type": "string",
        "description": "Номер дела"
      },
      "cost": {
        "type": "number",
        "description": "Сумма"
      },
      "category": {
        "type": "string",
        "description": "Категория дела"
      },
      "status": {
        "type": "string",
        "description": "Статус дела"
      },
      "last_decision": {
        "type": "string",
        "description": "Последнее решение"
      },
      "list_of_plaintiffs": {
        "type": "array",
        "description": "Список всех истцов",
        "items": {
          "type": "string"
        }
      },
      "list_of_defendants": {
        "type": "array",
        "description": "Список всех ответчиков",
        "items": {
          "type": "string"
        }
      },
      "stage": {
        "type": "array",
        "description": "Этапы",
        "items": {
          "type": "object",
          "properties": {
            "date": {
              "type": "string",
              "description": "Дата"
            },
            "authority": {
              "type": "string",
              "description": "Инстанция"
            },
            "note": {
              "type": "string",
              "description": "Примечание"
            }
          }
        }
      }
    }
  }
}
```

### Пример 
**Запрос** 
`/vok/courts/get?inn=7707083893&number_case=А04-2314/2026`

**Ответ**
```json
[
  [
    {
      "number_case": "А04-2314/2026",
      "cost": 35400,
      "status": "Рассматривается в первой инстанции",
      "date": "2026-03-25",
      "link": "http://kad.arbitr.ru/Card/c194daf1-5231-4376-adcb-533c3f089d52",
      "list_of_plaintiffs": [
        "Сбербанк, ПАО"
      ],
      "list_of_defendants": [
        "Таежный, ООО"
      ],
      "category": "о неисполнении или ненадлежащем исполнении обязательств по договорам банковского счета, обязательств при осуществлении расчетов",
      "case_source": 0,
      "case_name": "Истец",
      "result": "",
      "duration": "1 дн.",
      "last_decision": "Рассматривается в первой инстанции",
      "stage": [
        {
          "date": "2026-03-25",
          "authority": "АС Амурской области",
          "note": "Рассматривается в первой инстанции"
        }
      ]
    }
  ]
]
```


## Исполнительные листы

Получение списка исполнительных листов для ЮЛ

**URL**: `/executive-lists/`

**Обязательные параметры**:
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `category(str)` Категория исполнительных листов. по умолчанию 'all'
    - `all` - все типы
    - `fines` - штрафы
    - `state_duty` - госпошлина
    - `causing_harm` - причинение вреда
    - `debt` - задолженности
    - `taxes_fees` - налоги и сборы
    - `non-property` - неимущественные исполнения
    - `wages` - заработная плата
    - `court_costs` - судебные издержки
    - `suspension_of_activity` - приостановление деятельности
    - `confiscation` - конфискация
    - `credit_payments` - кредитные платежи
    - `insurance_premiums` - страховые взносы
    - `utility_payments` - коммунальные платежи
    - `release_of_premises` - по освобождению помещения
    - `property` - имущественное исполнение
    - `other` - иные
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы
- `is_active (bool)` - True - только активные листы, False - только архивные, None - все.

**Ограничения по лицензии**: 

В базовой версии лицензии доступна информация о последних 5 актуальных исполнительных делах.

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties":{
      "case_name": {
        "type": "string",
        "description": "Название дела (Истец, Ответчик, Исполнительный лист и тд)"
      },
      "date": {
        "type": "string",
        "description": "Дата суда"
      },
      "cost": {
        "type": "number",
        "description": "Сумма"
      },
      "status": {
        "type": "string",
        "description": "Статус дела"
      },
      "is_active": {
        "type": "boolean",
        "description": "Признак активного документа"
      }
    }
  }
}
```

### Пример 
**Запрос** 
`/vok/executive-lists?inn=7736050003`

**Ответ**
```json
[
  [
    {
      "date": "2025-08-11",
      "case_name": "Акт по делу об административном правонарушении",
      "number_case": "848241/25/78002-ИП",
      "status": "Штраф ГИБДД",
      "cost": 13000,
      "is_active": false
    },
    {
      "date": "2025-05-19",
      "case_name": "Исполнительный лист",
      "number_case": "311469/25/78024-ИП",
      "status": "Иные взыскания имущественного характера в пользу физических и юридических лиц",
      "cost": 543501,
      "is_active": false
    },
    {
      "date": "2025-05-07",
      "case_name": "Исполнительный лист",
      "number_case": "295405/25/78024-ИП",
      "status": "Иные взыскания имущественного характера в пользу физических и юридических лиц",
      "cost": 0,
      "is_active": false
    },
    {
      "date": "2025-04-09",
      "case_name": "Исполнительный лист",
      "number_case": "206737/25/78024-ИП",
      "status": "Госпошлина, присужденная судом",
      "cost": 4000,
      "is_active": false
    },
    {
      "date": "2025-04-03",
      "case_name": "Исполнительный лист",
      "number_case": "167580/25/89007-ИП",
      "status": "Госпошлина, присужденная судом",
      "cost": 0,
      "is_active": false
    },
    {
      "date": "2025-04-03",
      "case_name": "Исполнительный лист",
      "number_case": "167581/25/89007-ИП",
      "status": "Госпошлина, присужденная судом",
      "cost": 0,
      "is_active": false
    },
    {
      "date": "2025-03-14",
      "case_name": "Исполнительный лист",
      "number_case": "159194/25/78024-ИП",
      "status": "Госпошлина, присужденная судом",
      "cost": 0,
      "is_active": false
    },
    {
      "date": "2025-03-14",
      "case_name": "Исполнительный лист",
      "number_case": "145301/25/78024-ИП",
      "status": "Иные взыскания имущественного характера в пользу физических и юридических лиц",
      "cost": 10000,
      "is_active": false
    },
    {
      "date": "2025-03-07",
      "case_name": "Исполнительный лист",
      "number_case": "143510/25/78024-ИП",
      "status": "",
      "cost": 0,
      "is_active": false
    },
    {
      "date": "2025-03-03",
      "case_name": "Исполнительный лист",
      "number_case": "124259/25/78024-ИП",
      "status": "Госпошлина, присужденная судом",
      "cost": 0,
      "is_active": false
    }
  ]
]
```

## Статистика судов

**URL** : `/statistic-courts/`

**Ограничения по лицензии**: Отсутствуют.

**Обязательные параметры**

- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "all_defendant": {
      "type": "number",
      "description": "Всего Как Ответчик"
    },
    "process_defendant": {
      "type": "number",
      "description": "В Процессе Как Ответчик"
    },
    "loose_defendant": {
      "type": "number",
      "description": "Проигранных Как Ответчик"
    },
    "win_defendant": {
      "type": "number",
      "description": "Выигранных Как Ответчик"
    },
    "undefined_defendant": {
      "type": "number",
      "description": "Неопределенных Как Ответчик"
    },
    "cost_defendant": {
      "type": "number",
      "description": "Сумма Всего Как Ответчик"
    },
    "all_plaintiff": {
      "type": "number",
      "description": "Всего Как Истец"
    },
    "process_plaintiff": {
      "type": "number",
      "description": "В Процессе Как Истец"
    },
    "loose_plaintiff": {
      "type": "number",
      "description": "Проигранных Как Истец"
    },
    "win_plaintiff": {
      "type": "number",
      "description": "Выигранных Как Истец"
    },
    "undefined_plaintiff": {
      "type": "number",
      "description": "Неопределенных Как Истец"
    },
    "cost_plaintiff": {
      "type": "number",
      "description": "Сумма Всего Как Истец"
    },
    "exec_sheets": {
      "type": "number",
      "description": "Исполнительных Листов"
    },
    "actual_exec_sheets": {
      "type": "number",
      "description": "Актуальных Исполнительных Листов"
    },
    "cost_exec_sheets": {
      "type": "number",
      "description": "Сумма Исполнительных Листов"
    },
    "cost_actual_exec_sheets": {
      "type": "number",
      "description": "Сумма Актуальных Исполнительных Листов"
    },
    "cost_process_defendant": {
      "type": "number",
      "description": "Сумма ВПроцессе Как Ответчик"
    },
    "cost_loose_defendant": {
      "type": "number",
      "description": "Сумма Проигранных Как Ответчик"
    },
    "cost_win_defendant": {
      "type": "number",
      "description": "Сумма Выигранных Как Ответчик"
    },
    "cost_undefined_defendant": {
      "type": "number",
      "description": "Сумма Неопределенных Как Ответчик"
    },
    "cost_process_plaintiff": {
      "type": "number",
      "description": "Сумма В Процессе Как Истец"
    },
    "cost_loose_plaintiff": {
      "type": "number",
      "description": "Сумма Проигранных Как Истец"
    },
    "cost_win_plaintiff": {
      "type": "number",
      "description": "Сумма Выигранных Как Истец"
    },
    "cost_undefined_plaintiff": {
      "type": "number",
      "description": "Сумма Неопределенных Как Истец"
    }
  }
}
```

### Пример

**Запрос** `/vok/statistic-courts?inn=7736050003`

```json
[
  {
    "win_defendant": 58,
    "cost_win_defendant": 93114743,
    "loose_defendant": 62,
    "cost_loose_defendant": 143264350.11,
    "undefined_defendant": 5815,
    "cost_undefined_defendant": 36317688478.1,
    "process_defendant": 238,
    "cost_process_defendant": 2695168628.94,
    "all_defendant": 6173,
    "cost_defendant": 39249236200.15,
    "win_plaintiff": 60,
    "cost_win_plaintiff": 946960736.33,
    "loose_plaintiff": 17,
    "cost_loose_plaintiff": 2997.01,
    "undefined_plaintiff": 2524,
    "cost_undefined_plaintiff": 29153856532.08,
    "process_plaintiff": 85,
    "cost_process_plaintiff": 487844613.11,
    "all_plaintiff": 2686,
    "cost_plaintiff": 30588664878.53,
    "exec_sheets": 396,
    "cost_exec_sheets": 2438068.14,
    "actual_exec_sheets": 0,
    "cost_actual_exec_sheets": 0
  }
]
```