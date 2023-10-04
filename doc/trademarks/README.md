## Товарные знаки

Получить данные по контрагенту.

Метод доступен только в расширенной лицензии

**URL** : `/trademarks`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 5, максимум 10
- `page(str)` - страница запроса, по умолчанию 0
- `is_active(str)` - флаг активности товарного знака, по умолчанию отдаются активные. 

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "image_id": {
          "description": "идентификатор картинки",
          "type": "string"
        },
        "pub_date": {
          "description": "дата публикации",
          "type": "string"
        },
        "patent_date_begin": {
          "description": "дата начала патента",
          "type": "string"
        },
        "patent_date_end": {
          "description": "дата окончания патента",
          "type": "string"
        },
        "url": {
          "description": "ссылка на источник",
          "type": "string"
        },
        "reg_number": {
          "description": "рег номер",
          "type": "string"
        },
        "reg_date": {
          "description": "дата регистрации",
          "type": "string"
        },
        "app_number": {
          "description": "номер заявки на регистрацию",
          "type": "string"
        },
        "app_date": {
          "description": "дата заявки на регистрацию",
          "type": "string"
        },
        "publication_country_code": {
          "description": "Код страны публикации",
          "type": "string"
        },
        "title": {
          "description": "заголовок",
          "type": "string"
        },
        "patent_type_name": {
          "description": "тип патента",
          "type": "string"
        },
        "patent_status": {
          "description": "статус патента",
          "type": "bool"
        },
        "no_image": {
          "description": "отсутствует картинка",
          "type": "bool"
        },
        "contact_address": {
          "description": "адрес контакта",
          "type": "bool"
        },
        "purposes": {
          "description": "назначения",
          "type": "array",
          "items": [
            {
              "description": "назначение",
              "type": "string"
            }
          ]
        },
        "owners": {
          "description": "владельцы",
          "type": "array",
          "items": [
            {
              "description": "владелец",
              "type": "object",
              "properties": {
                "opf": {
                  "description": "ОПФ",
                  "type": "string"
                },
                "name": {
                  "description": "название",
                  "type": "string"
                },
                "address": {
                  "description": "адрес",
                  "type": "string"
                },
                "country_code": {
                  "description": "код страны",
                  "type": "string"
                },
                "contact_address": {
                  "description": "контактный адрес",
                  "type": "string"
                },
                "date_begin": {
                  "description": "дата начала",
                  "type": "string"
                },
                "date_end": {
                  "description": "дата окончания",
                  "type": "string"
                },
                "unique_key": {
                  "description": "уникальный ключ",
                  "type": "string"
                }
              }
            }
          ]
        },
        "notices": {
          "description": "события",
          "type": "array",
          "items": [
            {
              "description": "событие",
              "type": "object",
              "properties": {
                "title": {
                  "description": "Заголовок",
                  "type": "string"
                },
                "pub_date": {
                  "description": "дата публикации",
                  "type": "string"
                },
                "url": {
                  "description": "ссылка на источник",
                  "type": "string"
                },
                "attributes": {
                  "description": "атрибуты",
                  "type": "array",
                  "items": [
                    {
                      "description": "атрибут",
                      "type": "object",
                      "properties": {
                        "name": {
                          "description": "название",
                          "type": "string"
                        },
                        "value": {
                          "description": "значение",
                          "type": "string"
                        }
                      }
                    }
                  ]
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
    "image_id": 2447620,
    "pub_date": "2012-12-25",
    "patent_date_begin": null,
    "patent_date_end": null,
    "url": "http://www1.fips.ru/registers-doc-view/fips_servlet?DB=WKTM&rn=5940&DocNumber=121&TypeFile=html",
    "reg_number": "121",
    "reg_date": null,
    "app_number": null,
    "app_date": null,
    "publication_country_code": "RU",
    "title": "Товарный знак",
    "patent_type_name": "Товарный знак",
    "no_image": false,
    "purposes": [
      "перевозки железнодорожные; перевозки пассажирские железнодорожным транспортом; услуги транспортные, оказываемые железнодорожным транспортом; экспедирование грузов при перевозках железнодорожным транспортом."
    ],
    "contact_address": "Патентно-правовая фирма \"ЮС\", проспект Мира, д.6, Москва, 129090",
    "owners": [
      {
        "opf": "ОАО",
        "name": "РЖД",
        "address": "",
        "country_code": "RU",
        "contact_address": "АО \"РЖД-ЗДОРОВЬЕ\", Большой Златоустинский пер., д. 5, стр. 3, Москва, 101000",
        "date_begin": null,
        "date_end": null,
        "unique_key": "587855.None"
      }
    ],
    "notices": [
      {
        "title": "Исправление очевидных и технических ошибок в публикациях бюллетеня",
        "attributes": [
          {
            "name": "Дата публикации (номер бюллетеня):",
            "value": "25.12.2012 (БТЗ № 24)"
          },
          {
            "name": "Опубликовано:",
            "value": "Адрес для переписки: 107174, Москва, ул. Новая Басманная, д.2, ОАО \"РЖД\", Департамент технической политики"
          },
          {
            "name": "Следует читать:",
            "value": "Адрес для переписки: Патентно-правовая фирма \"ЮС\", проспект Мира, д.6, Москва, 129090"
          },
          {
            "name": "Дата внесения изменений в Перечень:",
            "value": "18.12.2012"
          },
          {
            "name": "Опубликовано:",
            "value": "12.01.2013"
          }
        ],
        "pub_date": "2013-01-12",
        "url": "http://new.fips.ru/Archive/TM/2013FULL/2013.01.12/DOC/DOCURUWK/DOC000V1/D00000D1/00000121/document.pdf"
      }
    ],
    "patent_status": null
  }
]
```

***

Получить картинку по товарному знаку.

Метод доступен только в расширенной лицензии


**URL** : `/trademarks/image`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `image_id(str)` - идентификатор картинки, получается из trademarks

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`
