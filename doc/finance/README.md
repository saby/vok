## Финансы:

Получить финансовые аналитические данные.

**Ограничения по лицензии**: В базовой лицензии отсутствуют:
1. Прогнозируемые значения показателей отчетности
2. Данные о конкурентах по выручке.
3. Описание текущего положения для рентабельности имущества.
4. Описание текущего положения для рентабельности продаж.

**URL** : `/finance/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```
"financial_indicators" (dict): Финансовые показатели.
    key (int): Отчетный период.
    value (dict): Данные показателей за год.
        "source": Название источника (str).
        key_1 (str): Название показетеля.
        value_1 (dict): Данные показателя
            "value": ЗначениеПоказателя (float),
            "formula": ФормуляПоказателя (str)
        ...
"performance_results" (str): Результаты деятельности
"performance_description" (str): Описание результатов (располагается под результатами)
Данные для диаграмм результатов деятельности будут в financial_indicators

"has_debt" (bool): имеется ли задолженность.
"taxes_and_fees" (dict): Налоги и сборы.
    key (int): Отчетный период.
    value (dict): Данные за отчетный период.
        НазваниеНалога1: Значение1,
        НазваниеНалога2: Значение2
        ...
"revenue_competitors" (list[dict]): Конкуренты по выручке (получаем через Контрагент.СвежиеКонкурентыТорги)
    "inn" (str): ИНН контрагента.
    "company_name" (str): Название контрагента.
    "region" (str): Регион контрагента.
    "director" (str): Фамилия Имя Отчество директора контрагента.
    "activity_kind" (str): Вид деятельности контрагента.
    "revenue" (float): Выручка.
    "cost" (float): Стоимость.
    "trades_intersections" (int): Количество пересечений в торгах с запрашиваемым контрагентом.
    "staff" (int): Штат сотрудников.
    "employees_number" (int): Точное количество сотрудников по данным ФНС.
"efficiency_state" (str): Краткое описание эффективности (bad, normal, good).
"profitability" (dict):
    "state": Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для доходности.
"property_profitability" (dict):
    "state": Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для рентабельности имущества.
"sales_profitability" (dict):
    "state": Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для рентабельности продаж.
"property_situation_state" (str): Краткое описание имущественного положения (bad, normal, good).
"current_assets" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для оборотных активов.
"non_circulating_assets" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для внеоборотных активов.
"estate_description" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для имущества.
"financial_position_state" (str): Краткое описание финансового положения (bad, normal, good).
"solvency" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для платежеспособности.
"dependence_on_creditors" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для зависимости от кредиторов.
"security_current_activities" (dict):
    "state" (str): Краткое описание (bad, normal, good)
    "description" (str): Описание текущего положения для зависимости от обеспеченности текущей деятельности.
```

**Пример ответа:**

```json
{
    "financial_indicators": {
        "2020": {
            "source": "GIRBO",
            "revenue": {
                "value": 123.0,
                "formula": "2211+2210"
            },
            "cost": {
                "value": 321.0,
                "formula": "2220+2221"
            },
            ...
        },
        "2019": {
            "source": "ROSSTAT",
            "revenue": {
                "value": 0.0,
                "formula": "2211+2210"
            },
            "cost": {
                "value": 400.0,
                "formula": "2220+2221"
            },
            ...
        }  
    },
    "performance_results": "normal",
    "perfomance_description": "За последний год доходы предприятия сократились, и произошло резкое сокращение прибыли",
    "has_debt": true,
    "taxes_and_fees": {
        "2020": {
            "revenue_tax": 124542.0,
            "nds_tax": 124542.0,
            "in_pf": 124542.0,
            ...
        },
        "2019": {
            "revenue_tax": 0.0,
            "nds_tax": 500.0,
            "in_pf": 300.0,
            ...
        },
        ...
    },
    revenue_competitors: [
        {
            "inn": "7712040126",
            "company_name": "Аэрофлот, ПАО",
            "region": "Москва",
            "director": "Савельев Виталий Геннадьевич",
            "activity_kind": "Перевозки пассажирские",
            "revenue": 551767420000.0,
            "cost": 123927009107.6,
            "trades_intersections": 0,
            "staff": 20325,
            "employees_number": 20325
        },
        ...
    ],
    "efficiency_state": "good",
    "profitability": {
        "state": "good",
        "description": "Доход собственника выше среднего (16 коп. на вложенный рубль)",
    },
    "property_profitability": {
        "state": "good",
        "description": "Рентабельность имущества (4%) соответствует среднеотраслевому значению (4%)",
    },
    "sales_profitability": {
        "state": "good",
        "description": "Рентабельность продаж (5.1%) выше среднеотраслевого значения (2.6%)",
    },
    "property_situation_state": "bad",
    "current_assets": {
        "state": "bad",
        "description": "Управление оборотными активами стало менее экономным: сократилась оборачиваемость запасов на 97%, долги покупателей стали собираться на 100% медленнее",
    },
    "non_circulating_assets": {
        "state": "bad",
        "description": "На долгосрочное развитие средств не выделено",
    },
    "estate_description": {
        "state": "bad",
        "description": "За последний год имущество сократилось на -39% (с 293.7 млн руб. до 178.8 млн руб.), что уменьшило потенциал предприятия",
    },
    "financial_position_state": "normal",
    "solvency": {
        "state": "good",
        "description": "Платежеспособность на приемлемом уровне: оборотные активы (источники погашения обязательств) больше обязательств на 34%",
    },
    "dependence_on_creditors": {
        "state": "bad",
        "description": "Зависимость от кредиторов значительная: доля обязательств в балансе (75%) больше 50%",
    },
    "security_current_activities": {
        "state": "normal",
        "description": "Обеспеченность текущей деятельности собственными средствами средняя (25% > 10% суммы оборотных активов)",
    }
}
```

## Стоимость бизнеса:

Получить аналитические данные по стоимости бизнеса.

**Ограничения по лицензии**: В базовой лицензии отсутствуют конкуренты по стоимости.
Данные по рассчитываемым методам предоставлены только за последний рассчитанный год.

**URL** : `/cost-business/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```
"market_value" (list[dict]): Рыночная стоимость компаниию (получаем через ЦеннаяБумага.ПолучитьПоКонтрагентуЗаПериод)
    "code" (str): Код ценной бумаги.
    "is_privileged" (bool): Является ли бумага привилегированной
    "values" (list[dict]): Значения ценной бумаги
    "date" (str): Дата ценной бумаги.
    "price" (float): Ценна на дату.
    "counts" (int): Выпуск.
"net_assets" (dict): Метод чистых активов
    Год: Значение (value)
"discounted_net_flows" (dict): Метод дисконтирования денежных потоков.
    Год: Значение (value)
"capital_market" (dict): Метод рынка капитала.
    Год: Значение (value)
"regression_analysis" (dict): Метод регрессионного анализа.
    Год: Значение (value)
"cost_competitors" (list[dict]): Конкуренты по стоимости(получаем через Контрагент.СвежиеКонкурентыТорги)
    "inn" (str): ИНН контрагента.
    "company_name" (str): Название контрагента.
    "region" (str): Регион контрагента.
    "director" (str): Фамилия Имя Отчество директора контрагента.
    "activity_kind" (str): Вид деятельности контрагента.
    "revenue" (float): Выручка.
    "cost" (float): Стоимость.
    "trades_intersections" (int): Количество пересечений в торгах с запрашиваемым контрагентом.
    "staff" (int): Штат сотрудников.
    "employees_number" (int): Точное количество сотрудников по данным ФНС.
```

**Пример ответа:**

```json
{
    "market_value": [
        {"code": "GAZP",
        "is_privileged": False,
        "values": [
            {"date": "2021-01-04",
            "price": 212.71,
            "counts": 23673512900},
            {"date": "2021-01-05",
            "price": 215.32,
            "counts": 23673512900},
            ...
        ]},
        ...
    ],
    "net_assets": {
        "2020": 3502.6,
        "2019": 45648.6,
        "2018": 51278.6,
        ...
    },
    "discounted_net_flows": {
        "2020": 3502.6,
        "2019": 45648.6,
        "2018": 51278.6,
        ...
    },
    "capital_market": {
        "2020": 3502.6,
        "2019": 45648.6,
        "2018": 51278.6,
        ...
    },
    "regression_analysis": {
        "2020": 3502.6,
        "2019": 45648.6,
        "2018": 51278.6,
        ...
    },
    "cost_competitors": 
        {
            "inn": "7712040126",
            "company_name": "Аэрофлот, ПАО",
            "region": "Москва",
            "director": "Савельев Виталий Геннадьевич",
            "activity_kind": "Перевозки пассажирские",
            "revenue": 551767420000.0,
            "cost": 123927009107.6,
            "trades_intersections": 0,
            "staff": 20325,
            "employees_number": 20325
        },
        ...
    ],
}
```

## Надежность:

Получить аналитические данные по надежности.

**URL** : `/reliability/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```
"advantages" (list[str]): Список положительных моментов влияющих на надежность
"disadvantages" (list[str]): Список отрицательных моментов влияющих на надежность
```

**Пример ответа:**

```json
{
    "advantages": [
        "Задолженность по налогам, з/п и кредитным платежам не обнаружена",
        "Компания способна расплатиться с текущими долгами",
        ...
    ],
    "disadvantages ": [
        "Риск потери независимости из-за имеющихся обязательств",
        "Вероятность банкротства",
        ...
    ],
}
```

## Положение на рынке:

Получить данные по положению рынке.

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
          "type": "float",
          "description": "Выручка контрагента"
        },
        "cost": {
          "type": "float",
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
      },
      "required": [
        "company_name",
        "inn"
      ]
    }
  ]
}
```

**Пример ответа:**

```json
[
    {
        "inn": "7712040126",
        "company_name": "Аэрофлот, ПАО",
        "region": "Москва",
        "director": "Савельев Виталий Геннадьевич",
        "activity_kind": "Перевозки пассажирские",
        "revenue": 551767420000.0,
        "cost": 123927009107.6,
        "trades_intersections": 0,
        "staff": 20325,
        "employees_number": 20325
    },
    ...
]
```

## Кредитоспособность:

Получить аналитические данные по кредитоспособности.

**Ограничения по лицензии**: Функционал недоступен для базовой лицензии.

**URL** : `/creditworthiness/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "amount_current_loans": {
      "type": "float",
      "description": "Сумма текущих займов"
    },
    "possible_loan": {
      "type": "float",
      "description": "Возможный кредит"
    },
    "stop_factors": {
      "type": "array",
      "description": "Стоп факторы",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "string",
            "description": "Ключ стоп фактора"
          },
          "state": {
            "type": "string",
            "pattern": "^good|bad|not_check$",
            "description": "Значение стоп фактора"
          }
        }
      }
    },
    "credit_grade": {
      "type": "object",
      "description": "Класс кредитоспособности",
      "properties": {
        "value": {
          "type": "string",
          "pattern": "not credited|common terms|preferential terms",
          "description": "Класс кредитоспособности"
        },
        КлючКоэффициента: {
          "type": "object",
          "description": "Ключ коэффициента",
          "properties": {
            "value": {
              "type": "float",
              "description": "Значение коэффициента"
            },
            "grade": {
              "type": "string",
              "pattern": "low|medium|high",
              "description": "Итоговая оценка"
            },
            "significance": {
              "type": "integer",
              "description": "Значимость коэффициента"
            }
          }
        } 
      }
    }
  }
}
```

**Пример ответа:**

```json
{
    "amount_current_loans": null,
    "possible_loan": 1548324831.0,
    "stop_factors": [
        {
            "key": "term_of_the_company",
            "state": "good"
        },
        ...
    ],
    "credit_grade": {
        "value": "common_terms",
        "current_liquidity": {
            "value": 133,
            "grade": "normal",
            "significance": 40
        },
        "absolute_liquidity": {
            "value": 0,
            "grade": "bad",
            "significance": 5
        }
    }
}
```
