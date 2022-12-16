## Суды

Получение списка судов для ЮЛ, где ЮЛ истец или ответчик

**URL** : `/courts/`

**Обязательные параметры**

- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
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
    {
        "date": "2018-12-26",
        "name": "Ответчик",
        "status": "Рассматривается в первой инстанции",
        "category": "экономические споры по гражданским правоотношениям",
        "cost": "5131.14",
        "result": "",
        "list_of_plaintiffs": [
            "Минприроды УР, ГУ"
        ],
        "list_of_defendants": [
            "Газпром, ПАО"
        ],
        "stage": [
            {
                "date": "2018-12-26",
                "authority": "АС Удмуртской Республики",
                "note": "Рассматривается в первой инстанции"
            }
        ],
        "duration": "1 дн.",
        "last_decision": "Рассматривается в первой инстанции"
    },
    {
        "date": "2018-11-20",
        "name": "Ответчик",
        "status": "Рассматривается в первой инстанции",
        "category": "экономические споры по гражданским правоотношениям",
        "cost": "28445425.00",
        "result": "О принятии искового заявления (заявления) к производству",
        "list_of_plaintiffs": [
            "Экострой, ООО"
        ],
        "list_of_defendants": [
            "Газпром, ПАО"
        ],
        "stage": [
            {
                "date": "2018-12-26",
                "authority": "АС Краснодарского края",
                "note": "О принятии искового заявления (заявления) к производству"
            }
        ],
        "duration": "1мес. 6дн.",
        "last_decision": "О принятии искового заявления (заявления) к производству"
    }
]

```
## Исполнительные листы

Получение списка исполнительных листов для ЮЛ

**URL** : `/executive-lists/`

**Обязательные параметры**:

- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
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

**Необязательные параметры**:
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
    {
        "date": "2021-05-19",
        "case_name": "Исполнительный лист",
        "status": "Иные взыскания имущественного характера в пользу физических и юридических лиц",
        "cost": "77128.07"
    },
    {
        "date": "2021-05-14",
        "case_name": "Исполнительный лист",
        "status": "Иные взыскания имущественного характера в пользу физических и юридических лиц",
        "cost": "932534.13"
    }
]
```

## Статистика судов

**URL** : `/statistic-courts/`

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
{
    "all_defendant": 2123,
    "cost_defendant": 17933440503.02,
    "all_plaintiff": 747,
    "cost_plaintiff": 7951941540.31,
    "exec_sheets": 135,
    "cost_exec_sheets": 7057938.82,
    "process_defendant": 405,
    "cost_process_defendant": 3394686762.50,
    "loose_defendant": 382,
    "cost_loose_defendant": 1075186716.39,
    "win_defendant": 270,
    "cost_win_defendant": 4444961918.67,
    "undefined_defendant": 1066,
    "cost_undefined_defendant": 9018605105.46,
    "process_plaintiff": 198,
    "cost_process_plaintiff": 735886107.39,
    "loose_plaintiff": 69,
    "cost_loose_plaintiff": 15280625.99,
    "win_plaintiff": 204,
    "cost_win_plaintiff": 3082560190.20,
    "undefined_plaintiff": 276,
    "cost_undefined_plaintiff": 4118214616.73,
    "actual_exec_sheets": 14,
    "cost_actual_exec_sheets": 1570843.08
}
```