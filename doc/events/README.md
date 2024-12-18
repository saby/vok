## События

Получить список событий

**Ограничения по лицензии** :

В базовой версии лицензии: последние 5 записи. В расширенной
 лицензии доступно всё для всех организаций.

**URL** : `/events`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 10, максимум 100
- `page(str)` - страница запроса, по умолчанию 0

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "files": {
          "description": "стоимость",
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "file_id": {
                  "description": "идентификатор файла",
                  "type": "int"
                },
                "title": {
                  "description": "назвние файла",
                  "type": "string"
                }
              }
            }
          ]
        },
        "publish_datetime": {
          "description": "дата и время публикации",
          "type": "string"
        },
        "content": {
          "description": "текст события",
          "type": "string"
        },
        "event_id": {
          "description": "идентификатор события на источнике",
          "type": "string"
        },
        "type_title": {
          "description": "тип события",
          "type": "string"
        },
        "url": {
          "description": "ссылка на событие",
          "type": "string"
        },
        "source_name": {
          "description": "название источника",
          "type": "string"
        },
        "event_date": {
          "description": "дата публикации",
          "type": "string"
        },
        "source": {
          "description": "ссылка на источник",
          "type": "string"
        },
        "corrections": {
          "description": "корректировки",
          "type": "array",
          "items": [
            {
              "type": "object"
              "properties": {
                "publish_datetime": {
                 "description": "дата и время публикации",
                 "type": "string"
                },
                "content": {
                 "description": "текст события",
                 "type": "string"
                },
                "event_id": {
                 "description": "идентификатор события на источнике",
                 "type": "string"
                },
                "type_title": {
                 "description": "тип события",
                 "type": "string"
                },
                "url": {
                 "description": "ссылка на событие",
                 "type": "string"
                },
                "source_name": {
                 "description": "название источника",
                 "type": "string"
                },
                "event_date": {
                 "description": "дата публикации",
                 "type": "string"
                },
                "source": {
                 "description": "ссылка на источник",
                 "type": "string"
                },
                "files": {
                  "description": "стоимость",
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "file_id": {
                          "description": "идентификатор файла",
                          "type": "int"
                        },
                        "title": {
                          "description": "назвние файла",
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

**Пример запроса**

```text
https://api.sbis.ru/vok/events?inn=7712040126
```

**Пример ответа**

```json
[
  {
    "files": [
      {
        "file_id": 4162999,
        "title": "Лист записи от 16.06.2021.pdf"
      },
      {
        "file_id": 4163001,
        "title": "Решение №1 от 07.06.2021.pdf"
      }
    ],
    "corrections": [],
    "publish_datetime": "2021-06-21 12:10:10",
    "content": "Общество с ограниченной ответственностью \"СПЕЦТЕХТРАНС\" (ОГРН 1171326004563, ИНН 1310000605, КПП 131001001, место нахождения: 431650, РЕСПУБЛИКА МОРДОВИЯ, ИЧАЛКОВСКИЙ РАЙОН, ОКТЯБРЬСКИЙ ПОСЕЛОК, УЛИЦА СОВЕТСКАЯ, ДОМ 38) уведомляет о том, что единственным участником ООО \"СПЕЦТЕХТРАНС\" (Решение № 1 от 07.06.2021 года) принято решение о ликвидации ООО \"СПЕЦТЕХТРАНС\". Требования кредиторов могут быть заявлены в течение 2 месяцев с момента опубликования настоящего сообщения по адресу: 431650, РЕСПУБЛИКА МОРДОВИЯ, ИЧАЛКОВСКИЙ РАЙОН, ОКТЯБРЬСКИЙ ПОСЕЛОК, УЛИЦА СОВЕТСКАЯ, ДОМ 38.",
    "event_id": "3DA644CEEA7D4C05A345E7A2D5B21E0D",
    "type_title": "Ликвидация юридического лица",
    "url": "https://fedresurs.ru/sfactmessage/3DA644CEEA7D4C05A345E7A2D5B21E0D",
    "source_name": "ФедРесурс",
    "message_number": "08402362",
    "source": "fedresurs.ru"
  }
]
```

***

Получить файл

**Ограничения по лицензии** :

Только для расширенной лицензии

**URL** : `/events/file`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `file_id` - идентификатор файла

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
file
```

**Пример запроса**

```text
https://api.sbis.ru/vok/events/file?inn=7712040126&file_id=100500
```
