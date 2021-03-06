## Филиалы

Получить филиалы контрагента.

**Ограничения по лицензии** :

Доступен в базовой версии лицензии

**URL** : `/branches`

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
        "branch_name": {
          "description": "Название филиала ",
          "type": "string"
        },
        "kpp": {
          "description": "КПП филиала",
          "type": "string"
        },
        "address": {
          "description": "адрес филиала",
          "type": "string"
        },
        "state_name": {
          "description": "назване состояния филиала",
          "type": "string"
        },
        "state_code": {
          "description": "состояние филиала",
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
    "kpp": "616143002",
    "branch_name": "Сбербанк, ПАО, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "616143001",
    "branch_name": "Сбербанк, ПАО, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "667102008",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "745302001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "027802001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "301502001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "231043001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "550502001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  {
    "kpp": "380843001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее"
  },
  ...
]
```
