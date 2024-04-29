## Общее о торгах:

Общая статистика по торгам контрагента

**Ограничения по лицензии** : Отсутствуют

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

**Пример запроса**

```text
https://api.sbis.ru/vok/tenders-info?inn=7712040126
```

**Пример ответа:**

```json
{
  "tender_count": 147,
  "win_count": 114,
  "win_price": 5580629000,
  "win_percent": 78,
  "lose_cnt": 14,
  "lose_price": 53844280,
  "sum_price": 5650616000,
  "rejected_count": 1,
  "rejected_price": 657200,
  "no_reduce_count": 107,
  "no_reduce_price": 5568162000,
  "customer_count": 2699
}
```

## Торги:

Список торгов в которых участвовало ЮЛ

**URL** : `/tenders/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
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
    "currency_brief": {
      "type": "str",
      "description": "символьный код валюты"
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


**Пример запроса**

```text
https://api.sbis.ru/vok/tenders?inn=7712040126
```

**Пример ответа:**

```json
[
  {
    "publish_date": "2024-03-13 07:47:09",
    "amount": 2700000,
    "lot_name": "Оказание услуг по перевозке пенсионеров, проживающих в районах Крайнего Севера и приравненных к ним местностях, воздушным транспортом по маршрутам Анадырь - Москва, Москва - Анадырь",
    "end_offer_date": "2024-03-20 02:00:00",
    "region": "Чукотский АО",
    "tp_brief": "РТС-тендер",
    "proc_type": "Запрос котировок в электронной форме",
    "currency_brief": "RUB",
    "winner_name": "Аэрофлот, ПАО",
    "company_name": "Осфр по Чукотскому Автономному Округу, ФГКУ",
    "tp_type_name": "44-ФЗ",
    "industry": [
      "Перевозки, логистика, таможня",
      "Перевозки пассажирские"
    ]
  },
  {
    "publish_date": "2024-03-06 04:09:26",
    "amount": 1000000,
    "lot_name": "Оказание услуг по перевозке авиационным транспортом граждан-получателей государственной социальной помощи и сопровождающих их лиц к месту санаторно-курортного лечения по маршрутам: Анадырь-Москва, Москва-Анадырь, Магадан – Москва, Москва - Магадан",
    "end_offer_date": "2024-03-14 02:00:00",
    "region": "Чукотский АО",
    "tp_brief": "РТС-тендер",
    "proc_type": "Электронный аукцион",
    "currency_brief": "RUB",
    "winner_name": "Аэрофлот, ПАО",
    "company_name": "Осфр по Чукотскому Автономному Округу, ФГКУ",
    "tp_type_name": "44-ФЗ",
    "industry": [
      "Перевозки, логистика, таможня",
      "Перевозки пассажирские"
    ]
  },
  {
    "publish_date": "2023-12-26 09:30:38.489000",
    "amount": 6500000,
    "lot_name": "Оказание услуг по перевозке авиационным транспортом граждан-получателей государственной социальной помощи и сопровождающих их лиц к месту лечения и обратно по маршрутам Анадырь-Москва, Москва-Анадырь, Магадан – Москва, Москва-Магадан",
    "end_offer_date": "2024-01-10 02:00:00",
    "region": "Чукотский АО",
    "tp_brief": "РТС-тендер",
    "proc_type": "Запрос котировок в электронной форме",
    "currency_brief": "RUB",
    "winner_name": "Аэрофлот, ПАО",
    "company_name": "Осфр по Чукотскому Автономному Округу, ФГКУ",
    "tp_type_name": "44-ФЗ",
    "industry": [
      "Перевозки, логистика, таможня",
      "Перевозки пассажирские"
    ]
  }
]
```

## Заказ торгов:

Список заказчиков у контрагента

**URL** : `/customers/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
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


**Пример запроса**

```text
https://api.sbis.ru/vok/customers?inn=7712040126
```

**Пример ответа:**

```json
[
  {
    "company_name": "СЛО \"Россия\", ФГБУ",
    "region": "Москва",
    "contact_name": "Терещенко К.Э.",
    "dir_name": "Терещенко К.Э.",
    "area": "Перевозки, логистика, таможня",
    "count_try": 1,
    "count_win": 1,
    "contract_count": 1,
    "price_win": 4530240000,
    "win_percent": 100,
    "contract_price": 4530239
  },
  {
    "company_name": "ГФС России",
    "region": "Москва",
    "contact_name": "Тихонов В.В.",
    "dir_name": "Тихонов В.В.",
    "area": "Услуги государственных органов",
    "count_try": 2,
    "count_win": 2,
    "contract_count": 2,
    "price_win": 421034600,
    "win_percent": 100,
    "contract_price": 389716
  },
  {
    "company_name": "Шереметьево Безопасность, АО",
    "region": "Московская обл",
    "contact_name": "Ипатов Н.А.",
    "dir_name": "Ипатов Н.А.",
    "area": "Транспортные услуги прочие",
    "count_try": 1,
    "count_win": 1,
    "contract_count": 0,
    "price_win": 225998600,
    "win_percent": 100,
    "contract_price": 0
  }
]
```

## Конкуренты:

Пересечение с конкурентами по торгам у ЮЛ

**URL** : `/rivals/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
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


**Пример запроса**

```text
https://api.sbis.ru/vok/rivals?inn=7712040126
```

**Пример ответа:**

```json
[
  {
    "company_name": "Холидеймакс, ООО",
    "count_try": 1,
    "count_win": 1,
    "price_win": 3675535,
    "region": "Москва",
    "count_all": 142,
    "price_win_all": 554153700,
    "dir_name": "Брагин А.А.",
    "area": "Услуги туристических агентств"
  },
  {
    "company_name": "Ата \"Сахалин Трэвел\", ООО",
    "count_try": 1,
    "count_win": 1,
    "price_win": 1462170,
    "region": "Сахалинская обл",
    "count_all": 196,
    "price_win_all": 154362000,
    "dir_name": "Ганчина Е.В.",
    "area": "Транспортные услуги прочие"
  },
  {
    "company_name": "АК Смартавиа, АО",
    "count_try": 4,
    "count_win": 3,
    "price_win": 810010,
    "region": "Архангельская обл",
    "count_all": 89,
    "price_win_all": 64237860,
    "dir_name": "Чернышев С.Е.",
    "area": "Перевозки пассажирские"
  }
]
```
