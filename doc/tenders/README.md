## Общее о торгах:

Общая статистика по торгам контрагента

**URL** : `/tenders-info/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

 
**Метод** : `GET`

**Формат ответа:**
```json
{
  "type": "object",
  "properties": {
    "lose_price": {
      "type": "number",
      "description": "Общая сумма проигранных торгов"
    },
    "lose_cnt": {
      "type": "number",
      "description": "Количество проигранных торгов"
    },
    "customer_count": {
      "type": "number",
      "description": "Количество организованных торгов"
    },
    "rejected_count": {
      "type": "number",
      "description": "Количество не допущенных торгов"
    },
    "sum_price": {
      "type": "number",
      "description": "общая сумма всех торгов"
    },
    "tender_count": {
      "type": "number",
      "description": "общее количество участия в торгах"
    },
    "win_count": {
      "type": "number",
      "description": "общее количество побед в торгах"
    },
    "win_price": {
      "type": "number",
      "description": "общая сумма побед"
    },
    "no_reduce_count": {
      "type": "number",
      "description": "количество побед без снижение цен"
    },
    "no_reduce_price": {
      "type": "number",
      "description": "общая сумма побед без снижения"
    }
  }
}
```

## Торги:

Список торгов в которых участвовало ЮЛ

**URL** : `/tenders/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

**Ограничения по лицензии**: 

В базовой версии лицензии недоступно более 3-х последних торгов.

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "название ЮЛ организовавшей торг"
    },
    "lot_name": {
      "type": "string",
      "description": "имя лота"
    },
    "tp_type_name": {
      "type": "string",
      "description": "имя группы торга"
    },
    "winner_name": {
      "type": "string",
      "description": "название победившей ЮЛ"
    },
    "region": {
      "type": "string",
      "description": "регион торга"
    },
    "tp_brief": {
      "type": "string",
      "description": "название процедуры"
    },
    "proc_type": {
      "type": "string",
      "description": "тип процедуры"
    },
    "amount": {
      "type": "number",
      "description": "цена торга"
    },
    "endofferdate": {
      "type": "str",
      "description": "дата окончания торга"
    },
    "publishdate": {
      "type": "str",
      "description": "дата публикации торга"
    },
    "industry": {
      "type": "array",
      "items": [
        {
          "description": "сфера деятельности торга"
          "type": "str"
        }
      ]
    }
  }
}
```

## Заказ торгов:

Список организованных ЮЛ торгов 

**URL** : `/customers/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

**Ограничения по лицензии**: 

В базовой версии лицензии недоступно более 3-х последних торгов.

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "название ЮЛ заказчика"
    },
    "region": {
      "type": "string",
      "description": "регион заказчика"
    },
    "dir_name": {
      "type": "string",
      "description": "ФИО или название руководителя"
    },
    "area": {
      "type": "string",
      "description": "сфера деятельности заказчика"
    },
    "count_try": {
      "type": "number",
      "description": "общее количество участников"
    },
    "count_win": {
      "type": "number",
      "description": "выигранных заявок"
    },
    "contract_count": {
      "type": "number",
      "description": "контрактов"
    },
    "price_win": {
      "type": "number",
      "description": "сумма побед"
    },
    "win_percent": {
      "type": "number",
      "description": "процент побед"
    },
    "contract_price": {
      "type": "number",
      "description": "цена контрактов"
    }
  }
}
```

## Конкуренты:

Пересечение с конкурентами по торгам у ЮЛ

**URL** : `/rivals/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количество запрашиваемых записей
- `page (int)` - номер страницы

**Ограничения по лицензии**: 

В базовой версии лицензии недоступно более 3-х конкурентов

Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. 
Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "название конкурента ЮЛ"
    },
    "count_try": {
      "type": "number",
      "description": "сколько было пересечений"
    },
    "count_win": {
      "type": "number",
      "description": "сколько победил в пересекающихся торгах"
    },
    "price_win": {
      "type": "number",
      "description": " сумма при победе"
    },
    "region": {
      "type": "string",
      "description": "регион проведения пересекающегося торга"
    },
    "count_all": {
      "type": "number",
      "description": "Общее количество участников"
    },
    "price_win_all": {
      "type": "number",
      "description": "общая сумма побед"
    },
    "dir_name": {
      "type": "string",
      "description": "ФИО или название руководителя"
    },
    "area": {
      "type": "string",
      "description": "сфера деятельности"
    }
  }
}
```