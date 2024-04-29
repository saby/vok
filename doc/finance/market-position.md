## Положение на рынке:

Получить данные по положению на рынке.

**Ограничения по лицензии**: Функционал недоступен в базовой лицензии.

**URL** : `/market-position/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `sort (str)` - Параметр сортировки. Возможные значения: "cost" - по стоимости, "revenue" - по выручке.

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
          "type": "string",
          "description": "Название компании"
        },
        "inn": {
          "type": "string",
          "description": "ИНН компании"
        },
        "region": {
          "type": "string",
          "description": "Регион контрагента"
        },
        "director": {
          "type": "string",
          "description": "Фамилия Имя Отчество директора контрагента"
        },
        "activity_kind": {
          "type": "string",
          "description": "Вид деятельности контрагента"
        },
        "revenue": {
          "type": "number",
          "description": "Выручка контрагента"
        },
        "cost": {
          "type": "number",
          "description": "Стоимость контрагента"
        },
        "trades_intersections": {
          "type": "integer",
          "description": "Количество пересечений в торгах с запрашиваемым контрагентом"
        },
        "staff": {
          "type": "integer",
          "description": "Штат сотрудников"
        },
        "employees_number": {
          "type": "integer",
          "description": "Точное количество сотрудников по данным ФНС"
        }
      }
    }
  ]
}
```

**Пример запроса**
```text
https://api.sbis.ru/vok/market-position?inn=7712040126&sort=cost
```


**Пример ответа:**

```json
[
  {
    "revenue": 378657216000,
    "cost": 238009543785.975,
    "inn": "7712040126",
    "company_name": "Аэрофлот, ПАО",
    "region": "Москва",
    "director": "Александровский Сергей Владимирович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 15539,
    "employees_number": null
  },
  {
    "revenue": 22918527000,
    "cost": 40455564000,
    "inn": "7736046504",
    "company_name": "Авиапредприятие \"Газпром Авиа\", ООО",
    "region": "Санкт-Петербург",
    "director": "Овчаренко Андрей Станиславович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 4239,
    "employees_number": null
  },
  {
    "revenue": 155963762000,
    "cost": 22504125203,
    "inn": "5448100656",
    "company_name": "Авиакомпания \"Сибирь\", АО",
    "region": "Обь",
    "director": "Клебанов Вадим Анатольевич",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 2,
    "staff": 8744,
    "employees_number": null
  },
  {
    "revenue": 17754778000,
    "cost": 13801335000,
    "inn": "6501161401",
    "company_name": "Авиакомпания \"Аврора\", АО",
    "region": "Южно-Сахалинск",
    "director": "Сухоребрик Константин Петрович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 2699,
    "employees_number": null
  },
  {
    "revenue": 95664065000,
    "cost": 7770185600,
    "inn": "6608003013",
    "company_name": "АК \"Уральские Авиалинии\", ОАО",
    "region": "Екатеринбург",
    "director": "Скуратов Сергей Николаевич",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 2,
    "staff": 5308,
    "employees_number": null
  },
  {
    "revenue": 7193890000,
    "cost": 4523951409,
    "inn": "7710697928",
    "company_name": "Авиационная Компания \"Ямал\", ООО",
    "region": "Москва",
    "director": "Величко Денис Николаевич",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 4,
    "employees_number": 4
  },
  {
    "revenue": 15508992000,
    "cost": 3181233000,
    "inn": "8401008386",
    "company_name": "АК \"Нордстар\", АО",
    "region": "Красноярск",
    "director": "Мохов Леонид Витальевич",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 1528,
    "employees_number": null
  },
  {
    "revenue": 13581612000,
    "cost": 869299745,
    "inn": "3808091156",
    "company_name": "Авиакомпания \"Ираэро\", АО",
    "region": "Иркутск",
    "director": "Лапин Юрий Владимирович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 1155,
    "employees_number": 1155
  },
  {
    "revenue": 195073000,
    "cost": 177843000,
    "inn": "7714797539",
    "company_name": "Холидеймакс, ООО",
    "region": "Москва",
    "director": "Брагин Андрей Алексеевич",
    "activity_kind": "Услуги туристических агентств",
    "trades_intersections": 1,
    "staff": 53,
    "employees_number": 53
  },
  {
    "revenue": 281264000,
    "cost": 177436000,
    "inn": "7724719890",
    "company_name": "Эстар Аэро, ООО",
    "region": "Москва",
    "director": "Хуснутдинова Миляуша Рашитовна",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 5,
    "employees_number": 5
  },
  {
    "revenue": 12541093000,
    "cost": 103342000,
    "inn": "2312218415",
    "company_name": "Авиакомпания Азимут, АО",
    "region": "Ростов-на-Дону",
    "director": "Екжанов Павел Александрович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 841,
    "employees_number": 841
  },
  {
    "revenue": 158950000,
    "cost": 57648743,
    "inn": "7707705181",
    "company_name": "ТМК Логистик, ООО",
    "region": "Москва",
    "director": "Грачевский Владимир Владимирович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 11,
    "employees_number": 11
  },
  {
    "revenue": 52489000,
    "cost": 39658624,
    "inn": "7736608136",
    "company_name": "Прайдлид, ООО",
    "region": "Москва",
    "director": "Хаматханова Лидия Мунтаевна",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 31,
    "employees_number": 31
  },
  {
    "revenue": 263436000,
    "cost": 10286000,
    "inn": "7719802542",
    "company_name": "Русаэрологистик, ООО",
    "region": "Москва",
    "director": "Волнистов Александр Викторович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 14,
    "employees_number": 14
  },
  {
    "revenue": 23323095000,
    "cost": -4144917000,
    "inn": "7732107883",
    "company_name": "РЕД Вингс, АО",
    "region": "Москва",
    "director": "Солодилин Евгений Александрович",
    "activity_kind": "Перевозки пассажирские",
    "trades_intersections": 0,
    "staff": 1738,
    "employees_number": null
  }
]
```
