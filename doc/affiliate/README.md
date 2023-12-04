## Владельцы:

Список учредителей для ЮЛ.

**URL** : `/owners/`

**Ограничения по лицензии**: Доступен в базовой версии лицензии

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
  Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "face_name": {
          "description": "Название владельца",
          "type": "string"
        },
        "inn": {
          "description": "Название источника",
          "type": "string"
        },
        "private": {
          "description": "Статус лица частное(True) или юридическое(False)",
          "type": "boolean"
        },
        "date_begin": {
          "description": "дата начала владения",
          "type": "string"
        },
        "share": {
          "description": "доля владения",
          "type": "string"
        },
        "cost": {
          "description": "сумма владения",
          "type": "string"
        },
        "region": {
          "description": "регион владельца",
          "type": "string"
        },
        "activity": {
          "description": "вид деятельности владельца",
          "type": "string"
        }
      }
    }
  ]
}
```

## Руководители

Список текущих и бывших руководителей для ЮЛ

**URL** : `/dirs-history/`

**Ограничения по лицензии**: Доступен в базовой версии лицензии

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
  Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "lastname": {
          "description": "Фамилия руководителя (если ЮЛ то отсутствует)",
          "type": "string"
        },
        "firstname": {
          "description": "Имя руководителя (если ЮЛ то отсутствует)",
          "type": "string"
        },
        "patronymic": {
          "description": "Отчество руководителя (если ЮЛ то отсутствует)",
          "type": "string"
        },
        "inn": {
          "description": "инн руководителя",
          "type": "string"
        },
        "position": {
          "description": "должность руководителя",
          "type": "string"
        },
        "fullname": {
          "description": "ФИО или название ЮЛ",
          "type": "string"
        },
        "private": {
          "description": "Статус лица частное(True) или юридическое(False)",
          "type": "boolean"
        },
        "date_begin": {
          "description": "дата начала руководства",
          "type": "string"
        },
        "date_end": {
          "description": "дата конца руководства( если null то текущий руководитель)",
          "type": "string"
        },
        "region": {
          "description": "регион руководителя",
          "type": "string"
        }
      }
    }
  ]
}
```

## Связанные лица

Список связанных компаний через руководителей и учредителей ЮЛ

**URL** : `/affiliate/`

**Ограничения по лицензии**: Доступен в базовой версии лицензии

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `limit (int)` - количество запрашиваемых записей, по умолчанию 10
- `page (int)` - номер страницы

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
  Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "company_name": {
          "description": "название ЮЛ",
          "type": "string"
        },
        "inn": {
          "description": "ИНН связанного ЮЛ",
          "type": "string"
        },
        "kpp": {
          "description": "КПП связанного ЮЛ",
          "type": "string"
        },
        "kladr": {
          "description": "КЛАДР связанного ЮЛ",
          "type": "string"
        },
        "date_reg": {
          "description": "дата регистрации ЮЛ",
          "type": "string"
        },
        "date_dead": {
          "description": "дата ликвидации ЮЛ, если нет то лицо действующее",
          "type": "string"
        },
        "linked_through": {
          "description": "через кого ЮЛ связано с текущим",
          "type": "string"
        },
        "revenue": {
          "description": "выручка ЮЛ",
          "type": "string"
        },
        "cost": {
          "description": "стоимость ЮЛ",
          "type": "string"
        },
        "region": {
          "description": "регион ЮЛ",
          "type": "string"
        },
        "activity": {
          "description": "деятельность ЮЛ",
          "type": "string"
        }
      }
    }
  ]
}
```

## История учредителей

История изменения в учредителях

**URL** : `/founders-history/`

**Ограничения по лицензии**: Доступен в базовой версии лицензии

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Не обязательные параметры**
- `limit (int)` - количество запрашиваемых записей, по умолчанию 10
- `page (int)` - номер страницы, по умолчанию 0

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
  Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "date": {
          "description": "Дата события",
          "type": "string"
        },
        "name": {
          "description": "Название",
          "type": "string"
        },
        "action": {
          "description": "Тип события. 0 - вошел, 1 - изменился, 2 - вышел",
          "type": "int"
        },
        "region": {
          "description": "Регион",
          "type": "string"
        },
        "hide_relations_count": {
          "description": "Количество скрытых учредителей. Если есть name, то значение null",
          "type": "int"
        },
        "previous_state": {
          "description": "Предыдущее состояние",
          "type": "object",
          "properties": {
            "share": {
              "description": "Доля",
              "type": "float"
            },
            "price": {
              "description": "Стоимость",
              "type": "float"
            }
          }
        },
        "new_state": {
          "description": "Новое состояние",
          "type": "object",
          "properties": {
            "share": {
              "description": "Доля",
              "type": "float"
            },
            "price": {
              "description": "Стоимость",
              "type": "float"
            }
          }
        }
      }
    }
  ]
}
```
