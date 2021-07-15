## Список изменений данных контрагента:

Получить список изменений данных.

**URL** : `/contractor_history/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `datetime_from(str)` - Дата от которой будет строиться список в формате ГГГГ-ММ-ДД
- `limit(int)` - Лимит запроса.

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "datetime": {
          "type": "string",
          "description": "Дата изменений. Пример 2019-06-17T12:50:20.433876"
        },
        "messages": {
          "type": "array",
          "description": "Сообщения об изменениях.",
          "items": [
            {
              "type": "object",
              "properties": {
                "action": {
                  "type": "string",
                  "description": "Описание типа изменений",
                  "pattern": "^changed|added|deleted$"
                },
                "requisite_name": {
                  "type": "string",
                  "description": "Название измененного реквизита"
                },
                "old_value": {
                  "type": "string",
                  "description": "Старое значение"
                },
                "new_value": {
                  "type": "string",
                  "description": "Новое значение"
                }
              }
            }
          ]
        },
        "source": {
          "type": "string",
          "description": "Название источника данных"
        }
      },
      "required": [
        "datetime",
        "messages",
        "source"
      ]
    }
  ]
}
```

**Пример ответа**

```json
[
  {
    "date": "2019-03-10T20:09:39.591716",
    "messages": [
      {
        "action": "changed",
        "new_value": "г.Москва, ул.Арбат, д.10, 119002",
        "old_value": "г.Санкт-Петербург, Рябовское ш., д.145, кв.47, 195043",
        "requisite_name": "юридический адрес"
      },
      {
        "action": "changed",
        "new_value": "45286552000",
        "old_value": "40278565000",
        "requisite_name": "ОКАТО"
      },
      {
        "action": "changed",
        "new_value": "45374000",
        "old_value": "40352000",
        "requisite_name": "ОКТМО"
      }
    ],
  "source": "Администратор системы"}
]
```