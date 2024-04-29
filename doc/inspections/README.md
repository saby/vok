## Проверки

Получить статистику по контрагенту.

**Ограничения по лицензии** :

В базовой версии лицензии доступно только 5 лидирующих служб проверок.
В расширенной версии доступны все службы проверки.

**URL** : `/inspections/stat`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(int)` - количество записей, дефолтно 10, максимум 20
- `page(int)` - страница, дефолтно 0
- `year_begin(int)` - год начала проверок, по умолчанию текущий -2
- `year_end(int)` - год окончания проверок, по умолчанию текущий, максимальная разница с year_begin - 10 лет

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "control_authority_name": {
          "description": "Название контролирующего органа",
          "type": "string"
        },
        "year_data": {
          "description": "годовая информация",
          "type": "object",
          "properties": {
            "year": {
              "description": "Запрашиваемый год, количество проверок",
              "type": "integer"
            }
          }
        }
      }
    }
  ]
}
```


**Пример запроса**

```text
https://api.sbis.ru/vok/inspections/stat?inn=7712040126
```

**Пример ответа для базовой лицензии:**

```json
[
  {
    "control_authority_name": "Ространснадзор",
    "year_data": {
      "2022": 4,
      "2023": 23,
      "2024": 12
    }
  },
  {
    "control_authority_name": "Роструд",
    "year_data": {
      "2022": 7,
      "2023": 9,
      "2024": 8
    }
  },
  {
    "control_authority_name": "Роспотребнадзор",
    "year_data": {
      "2022": 4,
      "2023": 19,
      "2024": 7
    }
  },
  {
    "control_authority_name": "Росприроднадзор",
    "year_data": {
      "2022": null,
      "2023": null,
      "2024": 1
    }
  },
  {
    "control_authority_name": "МЧС",
    "year_data": {
      "2022": null,
      "2023": null,
      "2024": 1
    }
  }
]
```

**Пример ответа для расширенной лицензии:**

```json
[
  {
    "control_authority_name": "Ространснадзор",
    "year_data": {
      "2022": 4,
      "2023": 23,
      "2024": 12
    }
  },
  {
    "control_authority_name": "Роструд",
    "year_data": {
      "2022": 7,
      "2023": 9,
      "2024": 8
    }
  },
  {
    "control_authority_name": "Роспотребнадзор",
    "year_data": {
      "2022": 4,
      "2023": 19,
      "2024": 7
    }
  },
  {
    "control_authority_name": "Росприроднадзор",
    "year_data": {
      "2022": null,
      "2023": null,
      "2024": 1
    }
  },
  {
    "control_authority_name": "МЧС",
    "year_data": {
      "2022": null,
      "2023": null,
      "2024": 1
    }
  },
  {
    "control_authority_name": "ФНС",
    "year_data": {
      "2022": null,
      "2023": 1,
      "2024": null
    }
  },
  {
    "control_authority_name": "Администрация, Органы местного самоуправления",
    "year_data": {
      "2022": null,
      "2023": 1,
      "2024": null
    }
  },
  {
    "control_authority_name": "Прочие",
    "year_data": {
      "2022": 3,
      "2023": null,
      "2024": null
    }
  }
]
```

***

##Данные по проверкам.

Получить данные по проверкам.

**Ограничения по лицензии** : 

В базовой версии лицензии доступны только 5 последних проверок.
В расширенной версии доступны все проверки

**URL** : `/inspections/data`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(int)` - количество записей, дефолтно 5, максимум 10
- `page(int)` - страница
- `year(int)` - год проверки
- `is_completed(bool)` - признак завершенности проверки, по умолчанию все
- `control_authorities(list of str)` - Названия контролирующих органов. Значения из статистики, поле control_authority_name


**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "region": {
          "description": "Регион",
          "type": "string"
        },
        "activity_category": {
          "description": "категория деятельности",
          "type": "string"
        },
        "activity_code": {
          "description": "код деятельности",
          "type": "string"
        },
        "inspection_body_main": {
          "description": "Проверяющий орган",
          "type": "string"
        },
        "inspection_body_additional": {
          "description": "Список проверяющих органов с которыми проверка проводится совместно",
          "type": "string"
        },
        "inspection_objective": {
          "description": "цель проведения проверки",
          "type": "string"
        },
        "inspection_objective_other": {
          "description": "Иные основания проведения проверки",
          "type": "string"
        },
        "type": {
          "description": "Тип проверки",
          "type": "string"
        },
        "form": {
          "description": "форма проверки",
          "type": "string"
        },
        "date_check": {
          "description": "дата проверки",
          "type": "string"
        },
        "duration": {
          "description": "Длительность проверки",
          "type": "string"
        },
        "status": {
          "description": "статус",
          "type": "string"
        },
        "inspection_address": {
          "description": "адрес инспекции",
          "type": "string"
        },
        "last_inspection_date": {
          "description": "дата проведения последней проверки",
          "type": "string"
        },
        "number": {
          "description": "номер проверки",
          "type": "string"
        },
        "act_number": {
          "description": "номер приказа о проведении проверки",
          "type": "string"
        },
        "act_date": {
          "description": "дата приказа о проведении проверки",
          "type": "string"
        },
        "is_scheduled": {
          "description": "является ли проверка плановой",
          "type": "bool"
        },
        "is_field_audit": {
          "description": "является ли проверка выездной",
          "type": "bool"
        },
        "is_documentary_audit": {
          "description": "Является ли проверка документарной",
          "type": "bool"
        },
        "url": {
          "description": "ссылка на источник",
          "type": "string"
        },
        "inspection_result.act_datetime": {
          "description": "Дата, время составления акта",
          "type": "string"
        },
        "inspection_result.act_place": {
          "description": "Место составления акта",
          "type": "string"
        },
        "inspection_result.inspectors": {
          "description": "ФИО, должность проверяющих",
          "type": "string"
        },
        "inspection_result.authorised_representative": {
          "description": "ФИО, должность уполномоченного представителя проверяемой компании",
          "type": "string"
        },
        "inspection_result.has_violation": {
          "description": "Флаг о наличии нарушений по итогам проверки",
          "type": "bool"
        },
        "inspection_result.is_canceled": {
          "description": "Флаг указывающий на что проверка отменена, из-за невозможности проведения",
          "type": "bool"
        },
        "inspection_result.cancel_reason": {
          "description": "Информация об отмене проверки",
          "type": "string"
        },
        "inspection_result.injunctions_total": {
          "description": "Всего предписаний",
          "type": "integer"
        },
        "inspection_result.injunctions_current": {
          "description": "Неустраненных предписаний",
          "type": "integer"
        },
        "inspection_result.injunctions_executed": {
          "description": "судебные запреты выполнены",
          "type": "string"
        },
        "inspection_result.result_published": {
          "description": "результаты опубликованы",
          "type": "string"
        },
        "violations_data": {
          "description": "данные о нарушениях",
          "type": "object",
          "properties": {
            "violation_desc": {
              "description": "Характер нарушения",
              "type": "string"
            },
            "violation_act": {
              "description": "Обоснование нарушения. Ссылка на правовой акт",
              "type": "string"
            },
            "violation_responsible": {
              "description": "Лица ответственные за нарушение",
              "type": "string"
            },
            "injunction_details": {
              "description": "Реквизиты предписания",
              "type": "string"
            },
            "injunction_content": {
              "description": "Содержание предписания",
              "type": "string"
            },
            "injunction_date": {
              "description": "Дата предписания",
              "type": "string"
            },
            "injunction_deadline": {
              "description": "Дата до которой должно быть исполнено предписание",
              "type": "string"
            },
            "injunction_execution_date": {
              "description": "Срок исполнения предписания",
              "type": "string"
            },
            "injunction_executed": {
              "description": "флаг исполнения предписания",
              "type": "string"
            }
          }
        }
      }
    }
  ]
}
```


**Пример запроса**

```text
https://api.sbis.ru/vok/inspections/data?inn=7712040126
```

**Пример ответа:**

```json
[
  {
    "date_check": "2024-11-21",
    "region": "77",
    "activity_category": "3502000000",
    "activity_code": "51.10.1",
    "inspection_body_main": "ГЛАВНОЕ УПРАВЛЕНИЕ МИНИСТЕРСТВА РОССИЙСКОЙ ФЕДЕРАЦИИ ПО ДЕЛАМ ГРАЖДАНСКОЙ ОБОРОНЫ, ЧРЕЗВЫЧАЙНЫМ СИТУАЦИЯМ И ЛИКВИДАЦИИ ПОСЛЕДСТВИЙ СТИХИЙНЫХ БЕДСТВИЙ ПО МОСКОВСКОЙ ОБЛАСТИ",
    "inspection_body_additional": "Федеральный государственный пожарный надзор",
    "inspection_objective": null,
    "inspection_objective_other": null,
    "type": "Плановая",
    "form": "Выездная",
    "duration": "13 раб.дн., 0 раб.ч.",
    "status": "Ожидает проведения",
    "inspection_address": null,
    "last_inspection_date": null,
    "number": "50240061000207655571",
    "act_number": null,
    "act_date": null,
    "is_scheduled": true,
    "is_field_audit": true,
    "is_documentary_audit": null,
    "url": "https://proverki.gov.ru/",
    "inspection_result.act_datetime": null,
    "inspection_result.act_place": null,
    "inspection_result.inspectors": null,
    "inspection_result.authorised_representative": null,
    "inspection_result.has_violation": false,
    "inspection_result.is_canceled": false,
    "inspection_result.cancel_reason": null,
    "inspection_result.injunctions_total": null,
    "inspection_result.injunctions_current": null,
    "inspection_result.injunctions_executed": null,
    "inspection_result.result_published": false,
    "violations_data": null
  },
  {
    "date_check": "2024-04-26",
    "region": "77",
    "activity_category": "3502000000",
    "activity_code": "51.10.1",
    "inspection_body_main": "ГОСУДАРСТВЕННАЯ ИНСПЕКЦИЯ ТРУДА В ГОРОДЕ МОСКВЕ",
    "inspection_body_additional": "Федеральный государственный контроль (надзор) за соблюдением трудового законодательства и иных нормативных правовых актов, содержащих нормы трудового права",
    "inspection_objective": null,
    "inspection_objective_other": null,
    "type": null,
    "form": "Документарная",
    "duration": null,
    "status": "Предостережение объявлено",
    "inspection_address": null,
    "last_inspection_date": null,
    "number": "77241373165510417385",
    "act_number": null,
    "act_date": null,
    "is_scheduled": null,
    "is_field_audit": null,
    "is_documentary_audit": true,
    "url": "https://proverki.gov.ru/",
    "inspection_result.act_datetime": null,
    "inspection_result.act_place": null,
    "inspection_result.inspectors": null,
    "inspection_result.authorised_representative": null,
    "inspection_result.has_violation": false,
    "inspection_result.is_canceled": false,
    "inspection_result.cancel_reason": null,
    "inspection_result.injunctions_total": null,
    "inspection_result.injunctions_current": null,
    "inspection_result.injunctions_executed": null,
    "inspection_result.result_published": false,
    "violations_data": null
  },
  {
    "date_check": "2024-04-18",
    "region": "77",
    "activity_category": "3502000000",
    "activity_code": "51.10.1",
    "inspection_body_main": "Управление Роспотребнадзора по Московской области",
    "inspection_body_additional": "Федеральный государственный контроль (надзор) в области защиты прав потребителей",
    "inspection_objective": null,
    "inspection_objective_other": null,
    "type": null,
    "form": "Документарная",
    "duration": null,
    "status": "Предостережение объявлено",
    "inspection_address": null,
    "last_inspection_date": null,
    "number": "50240791000110322570",
    "act_number": null,
    "act_date": null,
    "is_scheduled": null,
    "is_field_audit": null,
    "is_documentary_audit": true,
    "url": "https://proverki.gov.ru/",
    "inspection_result.act_datetime": null,
    "inspection_result.act_place": null,
    "inspection_result.inspectors": null,
    "inspection_result.authorised_representative": null,
    "inspection_result.has_violation": false,
    "inspection_result.is_canceled": false,
    "inspection_result.cancel_reason": null,
    "inspection_result.injunctions_total": null,
    "inspection_result.injunctions_current": null,
    "inspection_result.injunctions_executed": null,
    "inspection_result.result_published": false,
    "violations_data": null
  },
  {
    "date_check": "2024-04-16",
    "region": "77",
    "activity_category": "3502000000",
    "activity_code": "51.10.1",
    "inspection_body_main": "МЕЖРЕГИОНАЛЬНОЕ ТЕРРИТОРИАЛЬНОЕ УПРАВЛЕНИЕ ФЕДЕРАЛЬНОЙ СЛУЖБЫ ПО НАДЗОРУ В СФЕРЕ ТРАНСПОРТА ПО СИБИРСКОМУ ФЕДЕРАЛЬНОМУ ОКРУГУ",
    "inspection_body_additional": "Федеральный государственный контроль (надзор) в области гражданской авиации",
    "inspection_objective": null,
    "inspection_objective_other": null,
    "type": null,
    "form": "Документарная",
    "duration": null,
    "status": "Предостережение объявлено",
    "inspection_address": null,
    "last_inspection_date": null,
    "number": "54240814274310277283",
    "act_number": null,
    "act_date": null,
    "is_scheduled": null,
    "is_field_audit": null,
    "is_documentary_audit": true,
    "url": "https://proverki.gov.ru/",
    "inspection_result.act_datetime": null,
    "inspection_result.act_place": null,
    "inspection_result.inspectors": null,
    "inspection_result.authorised_representative": null,
    "inspection_result.has_violation": false,
    "inspection_result.is_canceled": false,
    "inspection_result.cancel_reason": null,
    "inspection_result.injunctions_total": null,
    "inspection_result.injunctions_current": null,
    "inspection_result.injunctions_executed": null,
    "inspection_result.result_published": false,
    "violations_data": null
  },
  {
    "date_check": "2024-04-12",
    "region": "77",
    "activity_category": "3502000000",
    "activity_code": "51.10.1",
    "inspection_body_main": "Управление Роспотребнадзора по Красноярскому краю",
    "inspection_body_additional": "Федеральный государственный контроль (надзор) в области защиты прав потребителей",
    "inspection_objective": null,
    "inspection_objective_other": null,
    "type": null,
    "form": "Документарная",
    "duration": null,
    "status": "Предостережение объявлено",
    "inspection_address": null,
    "last_inspection_date": null,
    "number": "24240791000110240593",
    "act_number": null,
    "act_date": null,
    "is_scheduled": null,
    "is_field_audit": null,
    "is_documentary_audit": true,
    "url": "https://proverki.gov.ru/",
    "inspection_result.act_datetime": null,
    "inspection_result.act_place": null,
    "inspection_result.inspectors": null,
    "inspection_result.authorised_representative": null,
    "inspection_result.has_violation": false,
    "inspection_result.is_canceled": false,
    "inspection_result.cancel_reason": null,
    "inspection_result.injunctions_total": null,
    "inspection_result.injunctions_current": null,
    "inspection_result.injunctions_executed": null,
    "inspection_result.result_published": false,
    "violations_data": null
  }
]
```


***
**Весь список control_authorities** :

Прочие, Главтехнадзор, ФМБА, Росрыболовство, Росгидромет, Рособрнадзор, ФСКН, Росалкогольрегулирование, Ространснадзор,
Роскомнадзор, Казначейство, ГИБДД, Ростехнадзор, Росприроднадзор, Рослесхоз, Россельхознадзор, Росздравнадзор, Роструд,
Росстандарт, ФАС, ФНС, ФМС, ФСБ, МВД, ФТС, Роспатент, Минюст, Роскосмос, Росфиннадзор, Военный комиссариат,
Росохранкультура, Росимущество, Росреестр, Росаккредитация, Роспотребнадзор, ФСТЭК, МЧС, Прокуратура, Архивный надзор,
Лицензионный контроль, Пожарный надзор и гражданская защита, Контроль производства и энергетики,
Строительный и жилищный контроль, Охрана окружающей среды, Контроль в сельском хозяйстве, Контроль здравоохранения,
Контроль торговли и услуг, Контроль труда и занятости, Соцзащита, Имущественный и земельный контроль,
Охрана культурного наследия, Администрация, Органы местного самоуправления.
