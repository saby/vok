## Контактные данные контрагента:

Получить контактные данные.

**URL** : `/contacts-official`

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
    "phone_numbers": {
      "description": "Телефонные номера",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "sites": {
      "description": "Сайты",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "emails": {
      "description": "Адреса электронной почты",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    }
  }
}
```

**Пример ответа**

```json
{
	"phone_numbers": [
		"74952584601",
		"74957757822"
	],
	"sites": [
		"vtb.ru",
        "broker.vtb.ru"
	],
	"emails": [
		"zakupki@msk.vtb.ru",
		"zakupki@kha.vtb.ru"
	]
}
```