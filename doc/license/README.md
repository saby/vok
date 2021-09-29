## Лицензии и сертификаты

Получить статистику по контрагенту.

**Ограничения по лицензии** :

Доступен в базовой версии лицензии.

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
[
  {
    "count_active": 0,
    "count_total": 2,
    "doc_type": "лицензия",
    "source": "Росгидромет"
  },
  {
    "count_active": 1,
    "count_total": 6,
    "doc_type": "лицензия",
    "source": "Роскомнадзор"
  },
  {
    "count_active": 2,
    "count_total": 2,
    "doc_type": "лицензия",
    "source": "ФСТЭК"
  },
  {
    "count_active": 14,
    "count_total": 29,
    "doc_type": "лицензия",
    "source": "Другие"
  }
]
```

***

Получить список лицензий по контрагенту.

**Ограничения по лицензии** :

В базовой версии лицензии доступны 3 последние документа по для каждого органа проверки.
В расширенной лицензии достпны все документы.

**URL** : `/license/data`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `source(str)` - название источника, поле source из статистики

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 10, максимум 100
- `page(str)` - страница запроса, по умолчанию 0
- `is_active(str)` - флаг активности лицензии, по умолчанию и при значении false отдаются все. 

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
        "license_kpp": {
          "description": "кпп лицензии",
          "type": "string"
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
          "type": "array",
          "items": [
            {
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
          ]
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
    "places": [
      "188477, Ленинградская область, Кингисеппский район, Вистинское сельское поселение, Морской торговый порт Усть-Луга, Комплекс по перевалке и фракционированию стабильного газового конденсата и продуктов его переработки"
    ],
    "license_kpp": null,
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