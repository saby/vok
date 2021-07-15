## Статистика внешнеэкономической активности:

Получить статистику по контрагенту.

**URL** : `/fea-stat`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "object",
  "properties": {
    "export_count": {
      "description": "Количество кодов экспорта",
      "type": "integer"
    },
    "c": {
      "description": "Количество кодов импорта",
      "type": "integer"
    },
    "markets": {
      "description": "Присутствие на рынках",
      "type": "array",
      "items": {
          "type": "string"
      },
      "minItems": 0
    }
  },
  "required": [ "export_count", "import_count", "markets" ]
}
```

**Пример ответа**

```json
{
  "export_count": 10,
  "import_count": 0,
  "markets": []
}
```