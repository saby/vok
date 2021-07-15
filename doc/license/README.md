## Лицензии и сертификаты

Получить статистику по контрагенту.

**URL** : `/license/stat`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "doc_type": {
          "description": "Тип документа",
          "type": "string"
        },
        "source": {
          "description": "Название источника",
          "type": "string"
        },
        "count_active": {
          "description": "Количество активных документов",
          "type": "integer"
        },
        "count_total": {
          "description": "общее количество документов",
          "type": "integer"
        }
      }
    }
  ]
}
```

**Пример ответа**

```json
{
  "active_vacancies_count": 2,
  "total_vacancies_count": 9
}
```

Получить список лицензий по контрагенту.

**URL** : `/license/data`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `source(str)` - название источника, поле source из статистики

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 10, максимум 100
- `page(str)` - страница запроса, по умолчанию 0
- `is_active(str)` - флаг активности вакансии, по умолчанию и при значении false отдаются все. 

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "number": {
          "description": "Название документа",
          "type": "string"
        },
        "place": {
          "description": "место",
          "type": "string"
        },
        "license_address": {
          "description": "адрес лицензии",
          "type": "string"
        },
        "object_of_issue": {
          "description": "объект выдачи",
          "type": "string"
        },
        "cert_count": {
          "description": "количество сертификата",
          "type": "integer"
        },
        "license_kpp": {
          "description": "кпп лицензии",
          "type": "string"
        },
        "total_count": {
          "description": "общее количество",
          "type": "integer"
        },
        "expired_count": {
          "description": "количество просроченных",
          "type": "integer"
        },
        "reg_number": {
          "description": "рег номер",
          "type": "string"
        },
        "product_common_name": {
          "description": "общее название продукта",
          "type": "string"
        },
        "data_type": {
          "description": "тип данных",
          "type": "string"
        },
        "is_user_edited": {
          "description": "отредактировано пользователем",
          "type": "bool"
        },
        "description": {
          "description": "описание",
          "type": "string"
        },
        "date_status_change": {
          "description": "дата изменения лицензии",
          "type": "string"
        },
        "product_name": {
          "description": "название сертификата",
          "type": "string"
        },
        "date_end": {
          "description": "дата окончания",
          "type": "string"
        },
        "date_begin": {
          "description": "дата начала",
          "type": "string"
        },
        "status": {
          "description": "признак активности статуса",
          "type": "bool"
        },
        "descriptions": {
          "description": "описания",
          "type": "array",
          "items": [
            {
              "description": "описание",
              "type": "string"
            }
          ]
        },
        "places": {
          "description": "места действия",
          "type": "array",
          "items": [
            {
              "description": "место",
              "type": "string"
            }
          ]
        },
        "change_status_details": {
          "description": "Детали изменения статуса",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "date_end": {
              "description": "Дата окончания",
              "type": "string"
            },
            "status": {
              "description": "Статус",
              "type": "bool"
            }
          }
        }
      }
    }
  ]
}
```

**Пример ответа**

```json
[
  {
    "number": "Приказ № 324",
    "place": "188477, Ленинградская область, Кингисеппский район, Вистинское сельское поселение, Морской торговый порт Усть-Луга, Комплекс по перевалке и фракционированию стабильного газового конденсата и продуктов его переработки",
    "object_of_issue": null,
    "license_address": null,
    "descriptions": [
      "Деятельность по монтажу, техническому обслуживанию и ремонту средств обеспечения пожарной безопасности зданий и сооружений"
    ],
    "cert_count": null,
    "places": [
      "188477, Ленинградская область, Кингисеппский район, Вистинское сельское поселение, Морской торговый порт Усть-Луга, Комплекс по перевалке и фракционированию стабильного газового конденсата и продуктов его переработки"
    ],
    "license_kpp": null,
    "total_count": null,
    "expired_count": null,
    "reg_number": null,
    "product_common_name": null,
    "change_status_details": null,
    "date_status_change": null,
    "data_type": "Лицензия",
    "is_user_edited": null,
    "description": null,
    "date_state_change": null,
    "product_name": null,
    "date_end": "",
    "date_begin": "",
    "status": true
  }
]
```