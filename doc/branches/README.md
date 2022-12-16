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
        "branch_code": {
          "description": "код филиала",
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
    "state_name": "действующее",
    "branch_code": 1
  },
  {
    "kpp": "616143001",
    "branch_name": "Сбербанк, ПАО, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 2
  },
  {
    "kpp": "667102008",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 3
  },
  {
    "kpp": "745302001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 4
  },
  {
    "kpp": "027802001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 125
  },
  {
    "kpp": "301502001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 112
  },
  {
    "kpp": "231043001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 110
  },
  {
    "kpp": "550502001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 55
  },
  {
    "kpp": "380843001",
    "branch_name": "Сбербанк, филиал",
    "address": "117997, г. Москва, ул. Вавилова, д. 19",
    "state_code": 1,
    "state_name": "действующее",
    "branch_code": 15
  },
  ...
]
```
