## Положение на рынке:

Получить данные по положению на рынке.

**Ограничения по лицензии**: Функционал доступен только в максимальной лицензии.

**URL** : `/market-position/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `sort (str)` - Параметр сортировки. Возможные значения: "cost" - по стоимости, "revenue" - по выручке.

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента.

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
  [
    {
      "revenue": 760401133000,
      "cost": 302655583741.875,
      "inn": "7712040126",
      "company_name": "Аэрофлот, ПАО",
      "region": "Москва",
      "director": "Александровский Сергей Владимирович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 16085,
      "employees_number": null
    },
    {
      "revenue": 36944240000,
      "cost": 209278579000,
      "inn": "7736046504",
      "company_name": "Авиапредприятие \"Газпром Авиа\", ООО",
      "region": "Санкт-Петербург",
      "director": "Овчаренко Андрей Станиславович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 3533,
      "employees_number": null
    },
    {
      "revenue": 81242806000,
      "cost": 125785243659.24,
      "inn": "7204002873",
      "company_name": "Авиакомпания \"Ютэйр\", ПАО",
      "region": "Ханты-Мансийск",
      "director": "Мартиросов Андрей Зарменович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 2983,
      "employees_number": null
    },
    {
      "revenue": 110975687000,
      "cost": 32215958000,
      "inn": "6608003013",
      "company_name": "\"Уральские Авиалинии\" АК, ОАО",
      "region": "Екатеринбург",
      "director": "  ",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 2,
      "staff": 4424,
      "employees_number": null
    },
    {
      "revenue": 52070209000,
      "cost": 10349812000,
      "inn": "7732107883",
      "company_name": "РЕД Вингс, АО",
      "region": "Жуковский",
      "director": "Лебедев Александр Валентинович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 1527,
      "employees_number": null
    },
    {
      "revenue": 314221000,
      "cost": 281011000,
      "inn": "7714797539",
      "company_name": "Холидеймакс, ООО",
      "region": "Москва",
      "director": "Брагин Андрей Алексеевич",
      "activity_kind": "Услуги туристических агентств",
      "trades_intersections": 1,
      "staff": 51,
      "employees_number": 51
    },
    {
      "revenue": 6989898000,
      "cost": 117117000,
      "inn": "7219006479",
      "company_name": "АО \"А247\", АО",
      "region": "Тюмень",
      "director": "Зайцев Сергей Викторович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 350,
      "employees_number": 350
    },
    {
      "revenue": 40247000,
      "cost": 14434000,
      "inn": "7715430999",
      "company_name": "Алтай-Авиа, ООО",
      "region": "Москва",
      "director": "Игитов Андрей Леонидович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 4,
      "employees_number": 4
    },
    {
      "revenue": 268527000,
      "cost": 12142000,
      "inn": "7719802542",
      "company_name": "Русаэрологистик, ООО",
      "region": "Москва",
      "director": "Волнистов Александр Викторович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 11,
      "employees_number": 11
    },
    {
      "revenue": 52119000,
      "cost": 6659000,
      "inn": "7736608136",
      "company_name": "Прайдлид, ООО",
      "region": "Москва",
      "director": "Хаматханова Лидия Мунтаевна",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 19,
      "employees_number": 19
    },
    {
      "revenue": 262130000,
      "cost": 1560000,
      "inn": "9715482550",
      "company_name": "Аэромедицина, ООО",
      "region": "Москва",
      "director": "Беляков Александр Александрович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 15,
      "employees_number": 15
    },
    {
      "revenue": 59121000,
      "cost": 671000,
      "inn": "7731463670",
      "company_name": "Хелипарк Подушкино, ООО",
      "region": "Москва",
      "director": "Бобков Алексей Юрьевич",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 1,
      "employees_number": 1
    },
    {
      "revenue": 145868000,
      "cost": -15377000,
      "inn": "7704363765",
      "company_name": "Транстехперевозки, ООО",
      "region": "Москва",
      "director": "Клепов Денис Владимирович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 0,
      "employees_number": null
    },
    {
      "revenue": 23958157000,
      "cost": -3235424000,
      "inn": "2459007621",
      "company_name": "Азур Эйр, ООО",
      "region": "Красноярск",
      "director": "Королев Евгений Борисович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 2106,
      "employees_number": null
    },
    {
      "revenue": 10556303000,
      "cost": -12175529000,
      "inn": "1435149030",
      "company_name": "Авиакомпания \"Якутия\", АО",
      "region": "Якутск",
      "director": "Николаев Владимир Рудольфович",
      "activity_kind": "Перевозки пассажирские",
      "trades_intersections": 0,
      "staff": 856,
      "employees_number": null
    }
  ]
]
```
