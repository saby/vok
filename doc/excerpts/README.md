## Список выписок ЕГРЮЛ

Получение списка выписок из ЕГРЮЛ для контрагента

**Ограничения по лицензии**: Отсутствуют.

**URL** : `/excerpt/list/`

**Обязательные параметры**
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

  Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.

**Метод** : `GET`

**Формат ответа:**
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "excerpt_hash": {
        "type": "string",
        "description": "Хеш выписки с помощью которого можно ее получить"
      },
      "date_receive": {
        "type": "string",
        "description": "Дата получения выписки"
      },
      "type_of_excerpt": {
        "type": "string",
        "description": "Название источника"
      }
    }
  }
}
```

**Пример запроса**

```text
https://api.sbis.ru/vok/excerpt/list?inn=7712040126
```

**Пример ответа для базовой лицензии:**

```json
[
  {
    "excerpt_hash": "5102bb87dae5c37471933c62158209d1",
    "date_receive": "2024-04-28",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "b313303d0dfdea8807404b6f9b54cc9c",
    "date_receive": "2023-11-20",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "8f9dda249535cad5b2ee0313456d16e9",
    "date_receive": "2023-10-30",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "7bca2b448b563500aa452e48b6056dc3",
    "date_receive": "2023-09-18",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "cf028ceec658cb47cd99190cde7c8718",
    "date_receive": "2023-09-11",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "f969484be336881f2b4ae2da446e7002",
    "date_receive": "2023-07-07",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "cec2b4f846303c83172bfb7237ee29a8",
    "date_receive": "2023-05-29",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "7a6d31167cd972c2f5f30e68eb7d7a60",
    "date_receive": "2023-04-13",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "e55320f3ff7e29b6e625e2975c8a4cef",
    "date_receive": "2023-03-30",
    "type_of_excerpt": "ЕГРЮЛ"
  },
  {
    "excerpt_hash": "4e190253de076c89140599c534a49c98",
    "date_receive": "2023-02-21",
    "type_of_excerpt": "ЕГРЮЛ"
  }
]
```

## Последняя выписка ЕГРЮЛ

Получение последней выписки из ЕГРЮЛ для контрагента

**Ограничения по лицензии**: Отсутствуют.

**URL** : `/excerpt/last`

**Обязательные параметры**

- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**
```json
{
  "type": "object",
  "properties": {
    "excerpt_hash": {
      "type": "string",
      "description": "Хеш выписки с помощью которого можно ее получить"
    },
    "date_receive": {
      "type": "string",
      "description": "Дата получения выписки"
    }
  }
}
```

**Пример запроса**

```text
https://api.sbis.ru/vok/excerpt/last?inn=7712040126
```

**Пример ответа для базовой лицензии:**

```json
{
  "excerpt_hash": "5102bb87dae5c37471933c62158209d1",
  "date_receive": "2023-12-16 02:00:00"
}
```

## Получение выписке по хешу

Получение выписке в виде .xml файла по хешу

**Ограничения по лицензии**: Отсутствуют.

**URL** : `/excerpt/file`

**Обязательные параметры**

- `hash(str)` - хеш выписки

**Метод** : `GET`

**Пример запроса**

```text
https://api.sbis.ru/vok/excerpt/file?hash=5102bb87dae5c37471933c62158209d1
```

**Формат ответа:** `#hash#.xml файл`
