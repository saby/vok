## Статистика вызова клиента

Получить статистику вызовов.

**URL** : `/client/stat`

**Параметров запроса нет**

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "object",
  "properties": {
    "requests_count_limit": {
      "description": "Лимит запросов за день",
      "type": "string"
    },
    "requests_count": {
      "description": "Текущее количество запросов за сегодня",
      "type": "string"
    },
    "unique_value_limit": {
      "description": "Лимит запросов по контрагентам",
      "type": "string"
    },
    "unique_value_count": {
      "description": "Текущее количество запрошенных контрагентов",
      "type": "string"
    }
  }
}
```

**Пример ответа**

```json
{
  "requests_count_limit": 30000,
  "requests_count": 5,
  "unique_value_limit": 5000,
  "unique_value_count": 5
}
```
