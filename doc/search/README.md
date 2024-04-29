## Поисковые методы

Получить данные по контрагенту.

**Ограничения по лицензии** :

Доступен в базовой версии лицензии

**URL** : `/search`

**Обязательные параметры** :
- `requisites` - реквизиты для поиска одной строкой

**Необязательные параметры** :
- `limit(str)` - количество записей в запросе, по умолчанию 20, максимум 100
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
        "company_name": {
          "description": "название компании",
          "type": "string"
        },
        "ogrn": {
          "description": "ОГРН",
          "type": "string"
        },
        "inn": {
          "description": "ИНН",
          "type": "string"
        },
        "kpp": {
          "description": "КПП",
          "type": "string"
        },
        "state_name": {
          "description": "название состояния",
          "type": "string"
        },
        "state_code": {
          "description": "код состояния",
          "type": "integer"
        }
      }
    }
  ]
}
```

**Пример запроса**

```text
https://api.sbis.ru/vok-demo/search?requisites=Газпром%201027700070518
```

**Пример ответа**

```json
[
  {
    "name": "Газпром, ПАО",
    "ogrn": "1027700070518",
    "inn": "7736050003",
    "kpp": "772801001",
    "state_code": 1,
    "state_name": "действующее"
  }
]
```
