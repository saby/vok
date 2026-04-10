## Финансы:

Получить финансовые аналитические данные.

**Ограничения по лицензии**: 

В базовой лицензии отсутствуют:
1. Данные о конкурентах по выручке.
2. Описание текущего положения для рентабельности имущества.
3. Описание текущего положения для рентабельности продаж.

В расширенной лицензии отсутствуют:
1. Данные о конкурентах по выручке.



**URL** : `/finance/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента.

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "financial_indicators": {
      "type": "object",
      "description": "Финансовые показатели",
      "properties": {
        "source": {
          "type": "string",
          "description": "Название источника"
        },
        "indicator_name": {
          "type": "object",
          "description": "Данные показателя",
          "properties": {
            "value": {
              "type": "number",
              "description": "Значение показателя"
            },
            "formula": {
              "type": "string",
              "description": "Формула показателя"
            }
          }
        }
      }
    },
    "performance_results": {
      "type": "string",
      "description": "Результаты деятельности"
    },
    "performance_description": {
      "type": "string",
      "description": "Описание результатов"
    },
    "has_debt": {
      "type": "boolean",
      "description": "Признак наличия задолженности"
    },
    "taxes_and_fees": {
      "type": "object",
      "description": "Данные по налогам и сборам",
      "properties": {
        "years": {
          "pattern": "^(19|20)[0-9][0-9]$",
          "type": "object",
          "description": "Данные за отчетный период.",
          "properties": {
            "tax_or_fee_name": {
              "type": "number",
              "description": "Значение налога или сбора"
            }
          }
        }
      }
    },
    "revenue_competitors": {
      "type": "array",
      "description": "Конкуренты по выручке",
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
    },
    "efficiency_state": {
      "type": "string",
      "description": "Краткое описание эффективности",
      "pattern": "^good|bad|normal$"
    },
    "profitability": {
      "type": "object",
      "description": "Информация о доходности",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для доходности"
        }
      }
    },
    "property_profitability": {
      "type": "object",
      "description": "Информация о рентабельности имущества",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для рентабельности имущества"
        }
      }
    },
    "sales_profitability": {
      "type": "object",
      "description": "Информация о рентабельности продаж",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для рентабельности продаж"
        }
      }
    },
    "property_situation_state": {
      "type": "string",
      "description": "Краткое описание имущественного положения",
      "pattern": "^good|bad|normal$"
    },
    "current_assets": {
      "type": "object",
      "description": "Информация о положении для оборотных активов",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для оборотных активов"
        }
      }
    },
    "non_circulating_assets": {
      "type": "object",
      "description": "Информация о положении для внеоборотных активов",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для внеоборотных активов"
        }
      }
    },
    "estate_description": {
      "type": "object",
      "description": "Информация о положении для имущества",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для имущества"
        }
      }
    },
    "financial_position_state": {
      "type": "string",
      "description": "Краткое описание финансового положения",
      "pattern": "^good|bad|normal$"
    },
    "solvency": {
      "type": "object",
      "description": "Информация о положении для платежеспособности",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для платежеспособности"
        }
      }
    },
    "dependence_on_creditors": {
      "type": "object",
      "description": "Информация о положении для зависимости от кредиторов",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для зависимости от кредиторов"
        }
      }
    },
    "security_current_activities": {
      "type": "object",
      "description": "Информация о положении для зависимости от обеспеченности текущей деятельности",
      "properties": {
        "state": {
          "type": "string",
          "description": "Краткое описание",
          "pattern": "^good|bad|normal$"
        },
        "description": {
          "type": "string",
          "description": "Описание текущего положения для зависимости от обеспеченности текущей деятельности"
        }
      }
    }
  }
}
```

**Пример запроса**
```text
https://api.sbis.ru/vok/finance?inn=7712040126
```


**Пример ответа для базовой лицензии:**

```json
[
  {
    "current_assets": {
      "description": "Управление оборотными активами стало более экономным: долги покупателей стали собираться на XX.X% быстрее",
      "state": "good"
    },
    "dependence_on_creditors": {
      "description": "Зависит от кредиторов в значительной степени: доля обязательств в балансе (XX%) больше 50%",
      "state": "bad"
    },
    "efficiency_state": "bad",
    "estate_description": {
      "description": "За последний год имущество выросло на X.X% (с XXX.X млрд ₽ до XXX.X млрд ₽), что увеличило потенциал предприятия",
      "state": "good"
    },
    "financial_indicators": {
      "2004": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 55703336000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 57773919000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6330143000
        },
        "source": "ROSSTAT"
      },
      "2005": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 65752460000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 73397427000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6032405000
        },
        "source": "ROSSTAT"
      },
      "2006": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 73917181000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 82012191000
        },
        "net_profit": {
          "formula": "2400",
          "value": 7981346000
        },
        "source": "ROSSTAT"
      },
      "2007": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 84458602000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 91854353000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6074369000
        },
        "source": "ROSSTAT"
      },
      "2008": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 103031261000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 108508861000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5807312000
        },
        "source": "ROSSTAT"
      },
      "2009": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "source": "ROSSTAT"
      },
      "2010": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "source": "ROSSTAT"
      },
      "2011": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 142863788000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 153803001000
        },
        "net_profit": {
          "formula": "2400",
          "value": 10483665000
        },
        "source": "ROSSTAT"
      },
      "2012": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 188638598000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 191780059000
        },
        "net_profit": {
          "formula": "2400",
          "value": 3040593000
        },
        "source": "ROSSTAT"
      },
      "2013": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 219261483000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 229987457000
        },
        "net_profit": {
          "formula": "2400",
          "value": 11096946000
        },
        "source": "ROSSTAT"
      },
      "2014": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 263135926000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 276109093000
        },
        "net_profit": {
          "formula": "2400",
          "value": 13149221000
        },
        "source": "ROSSTAT"
      },
      "2015": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 430013527000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 412076928000
        },
        "net_profit": {
          "formula": "2400",
          "value": -18927841000
        },
        "source": "ROSSTAT"
      },
      "2016": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 468870022000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 498554300000
        },
        "net_profit": {
          "formula": "2400",
          "value": 30616800000
        },
        "source": "ROSSTAT"
      },
      "2017": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 478943344000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 507386797000
        },
        "net_profit": {
          "formula": "2400",
          "value": 28443453000
        },
        "source": "ROSSTAT"
      },
      "2018": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 570556978000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 573353082000
        },
        "net_profit": {
          "formula": "2400",
          "value": 2796104000
        },
        "source": "ROSSTAT"
      },
      "2019": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 618774449000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 621195631000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5286800000
        },
        "source": "GIRBO"
      },
      "2020": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 362956700000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 266429567000
        },
        "net_profit": {
          "formula": "2400",
          "value": -96527133000
        },
        "source": "GIRBO"
      },
      "2021": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 484200237000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 427799273000
        },
        "net_profit": {
          "formula": "2400",
          "value": -45639139000
        },
        "source": "GIRBO"
      },
      "2023": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 710297531000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 679527743000
        },
        "net_profit": {
          "formula": "2400",
          "value": -29456385000
        },
        "source": "GIRBO"
      },
      "2024": {
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 819183067000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 826215810000
        },
        "net_profit": {
          "formula": "2400",
          "value": 21958748000
        },
        "source": "GIRBO"
      }
    },
    "financial_position_state": "bad",
    "has_debt": false,
    "non_circulating_assets": {
      "description": "Внеоборотные активы увеличились, в том числе за счет налоговых активов",
      "state": "normal"
    },
    "performance_description": "За последний год доходы предприятия увеличились, и оно стало прибыльным",
    "performance_results": "good",
    "profitability": {
      "description": "Доходность не определена, т.к. нет собственного капитала",
      "state": "bad"
    },
    "property_profitability": {
      "description": "Рентабельность имущества (X.X%) ниже среднеотраслевого значения (X.X%)",
      "state": "bad"
    },
    "property_situation_state": "normal",
    "sales_profitability": {
      "description": "Рентабельность затрат (X.X%) выше среднеотраслевого значения (X%)",
      "state": "good"
    },
    "security_current_activities": {
      "description": "Обеспеченность текущей деятельности собственными средствами низкая",
      "state": "bad"
    },
    "solvency": {
      "description": "Платежеспособность низкая: оборотные активы (источники погашения обязательств) на XX% меньше суммы обязательств",
      "state": "bad"
    },
    "taxes_and_fees": {}
  }
]
```

**Пример ответа для расширенной лицензии:**

```json
[
  {
    "current_assets": {
      "description": "Управление оборотными активами стало более экономным: долги покупателей стали собираться на 28.9% быстрее",
      "state": "good"
    },
    "dependence_on_creditors": {
      "description": "Зависит от кредиторов в значительной степени: доля обязательств в балансе (93%) больше 50%",
      "state": "bad"
    },
    "efficiency_state": "bad",
    "estate_description": {
      "description": "За последний год имущество выросло на 2.4% (с 934.3 млрд ₽ до 957.1 млрд ₽), что увеличило потенциал предприятия",
      "state": "good"
    },
    "financial_indicators": {
      "2004": {
        "accounts_payable": {
          "formula": "1520",
          "value": 6430286000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3492079000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2162703000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 24295701000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 8266483000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 222196000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1029422000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 11771184000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 16331005000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3404826000
        },
        "cost_price": {
          "formula": "2120",
          "value": 46495617000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 55703336000
        },
        "current assets": {
          "formula": "1200",
          "value": 16908626000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 33
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 302120000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2296070000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 7387075000
        },
        "funds": {
          "formula": "1250",
          "value": 1435166000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 9970000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 9881564000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 57773919000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1977379000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 58325000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 463131000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 463131000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3734614000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6330143000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 240935000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 1622199000
        },
        "other_income": {
          "formula": "2340",
          "value": 1195619000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 131204000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 16340975000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 81651000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 69915000
        },
        "profit": {
          "formula": "2200",
          "value": 4314035000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 38.8
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 63
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 37000
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 56377181000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 8.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 7459708000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 7501565000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 127
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2998698000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 987000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 11450693000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 401458000
        }
      },
      "2005": {
        "accounts_payable": {
          "formula": "1520",
          "value": 7488783000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3374528000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2297863000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 32753649000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 8365934000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 1960536000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1727967000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 18479142000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 20732824000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3522691000
        },
        "cost_price": {
          "formula": "2120",
          "value": 53737902000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 65752460000
        },
        "current assets": {
          "formula": "1200",
          "value": 25112416000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 37
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 1539207000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2385594000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 7641233000
        },
        "funds": {
          "formula": "1250",
          "value": 1647535000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 28914000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 9111376000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 73397427000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1667588000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 52682000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 2766817000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 2766817000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3935343000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6032405000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 5242770000
        },
        "other_income": {
          "formula": "2340",
          "value": 10100289000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 206807000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 20761738000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 230267000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 241053000
        },
        "profit": {
          "formula": "2200",
          "value": 3290822000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 29.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 68
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 62849278000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 5.5
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 9216750000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 9254008000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 172
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2939607000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 141327000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 806281000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 15970026000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 506925000
        }
      },
      "2006": {
        "accounts_payable": {
          "formula": "1520",
          "value": 7397459000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3141650000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2249884000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 36729604000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 11432633000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1734889000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 17511329000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 26722298000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3894878000
        },
        "cost_price": {
          "formula": "2120",
          "value": 57608388000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 73917181000
        },
        "current assets": {
          "formula": "1200",
          "value": 25819379000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 27
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 628627000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 5778379000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 10910225000
        },
        "funds": {
          "formula": "1250",
          "value": 4218281000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 115026000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 13744658000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 82012191000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3450987000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 44359000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 749449000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 749449000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3855756000
        },
        "net_profit": {
          "formula": "2400",
          "value": 7981346000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 6669661000
        },
        "other_income": {
          "formula": "2340",
          "value": 10270678000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 208077000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 26837324000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 156747000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 180390000
        },
        "profit": {
          "formula": "2200",
          "value": 7599896000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 29.9
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 69
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 71353046000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 11.9
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 9132348000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 9257857000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 183
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3057965000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 197858000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 749449000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 22192378000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 403177000
        }
      },
      "2007": {
        "accounts_payable": {
          "formula": "1520",
          "value": 12444745000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 2901411000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2927214000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 44871557000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 10747893000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1703484000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 24661472000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 30441623000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 4982897000
        },
        "cost_price": {
          "formula": "2120",
          "value": 61460691000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 84458602000
        },
        "current assets": {
          "formula": "1200",
          "value": 33369162000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 32
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 87473000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 4801493000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 11502395000
        },
        "funds": {
          "formula": "1250",
          "value": 1789870000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 172302000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 15634194000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 91854353000
        },
        "income_tax": {
          "formula": "2410",
          "value": 4030688000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 69718000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 88758000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 88758000
        },
        "main_assets": {
          "formula": "1150",
          "value": 4774144000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6074369000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 6503000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 11656678000
        },
        "other_income": {
          "formula": "2340",
          "value": 14367075000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 283398000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 30613925000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 78980000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 108995000
        },
        "profit": {
          "formula": "2200",
          "value": 7724083000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 20
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 69
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 77094885000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 11.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 14148229000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 14341176000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 114
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3604371000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 215713000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 88758000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 26151942000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 181292000
        }
      },
      "2008": {
        "accounts_payable": {
          "formula": "1520",
          "value": 15265188000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 1811440000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 3750176000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 50339789000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 9386025000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1820409000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 26737015000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 33084790000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 5389762000
        },
        "cost_price": {
          "formula": "2120",
          "value": 79322627000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 103031261000
        },
        "current assets": {
          "formula": "1200",
          "value": 37480108000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 34
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 181515000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 4401371000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 12859681000
        },
        "funds": {
          "formula": "1250",
          "value": 3014335000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 119213000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 15691333000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 108508861000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3712171000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 94064000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 43736000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 43736000
        },
        "main_assets": {
          "formula": "1150",
          "value": 5085152000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5807312000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 13898000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 10550142000
        },
        "other_income": {
          "formula": "2340",
          "value": 13201306000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 219715000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 33204003000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 110129000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 73880000
        },
        "profit": {
          "formula": "2200",
          "value": 6551395000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 17.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 71
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 405967000
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 95013960000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 7.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 17085597000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 17211263000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 96
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3205803000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 64481000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 43736000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 30291047000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 254062000
        }
      },
      "2009": {
        "accounts_payable": {
          "formula": "1520",
          "value": 0
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 0
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 0
        },
        "balance": {
          "formula": "1600",
          "value": 0
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 0
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 0
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 0
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 0
        },
        "cost_price": {
          "formula": "2120",
          "value": 0
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "current assets": {
          "formula": "1200",
          "value": 0
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 100
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 0
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 0
        },
        "funds": {
          "formula": "1250",
          "value": 0
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 0
        },
        "gross_profit": {
          "formula": "2100",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 0
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 0
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 0
        },
        "main_assets": {
          "formula": "1150",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 0
        },
        "other_income": {
          "formula": "2340",
          "value": 0
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 0
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 0
        },
        "profit": {
          "formula": "2200",
          "value": 0
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 0
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 0
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 0
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 0
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 0
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 0
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 0
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 0
        }
      },
      "2010": {
        "accounts_payable": {
          "formula": "1520",
          "value": 0
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 0
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 0
        },
        "balance": {
          "formula": "1600",
          "value": 0
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 0
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 0
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 0
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 0
        },
        "cost_price": {
          "formula": "2120",
          "value": 0
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "current assets": {
          "formula": "1200",
          "value": 0
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 100
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 0
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 0
        },
        "funds": {
          "formula": "1250",
          "value": 0
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 0
        },
        "gross_profit": {
          "formula": "2100",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 0
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 0
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 0
        },
        "main_assets": {
          "formula": "1150",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 0
        },
        "other_income": {
          "formula": "2340",
          "value": 0
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 0
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 0
        },
        "profit": {
          "formula": "2200",
          "value": 0
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 0
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 0
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 0
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 0
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 0
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 0
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 0
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 0
        }
      },
      "2011": {
        "accounts_payable": {
          "formula": "1520",
          "value": 25475220000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 6166879000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 96725423000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 13924557000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 12000000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 4304902000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 44824272000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 49610609000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 15954667000
        },
        "cost_price": {
          "formula": "2120",
          "value": 111050208000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 142863788000
        },
        "current assets": {
          "formula": "1200",
          "value": 59651907000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 46
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 373513000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1733749000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 8019002000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 10147225000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 37073516000
        },
        "funds": {
          "formula": "1250",
          "value": 3616956000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 224443000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 24751270000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 153803001000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3247809000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 81973000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 15002987000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 15376500000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10663075000
        },
        "net_profit": {
          "formula": "2400",
          "value": 10483665000
        },
        "other": {
          "formula": "2460",
          "value": 130058000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 179137000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 2556625000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 5794897000
        },
        "other_income": {
          "formula": "2340",
          "value": 16773992000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 116254000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 51942314000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 911793000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1111277000
        },
        "profit": {
          "formula": "2200",
          "value": 2629724000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 21.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 77
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 287729000
        },
        "research_results": {
          "formula": "1120",
          "value": 21451000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 792979000
        },
        "revenue": {
          "formula": "2110",
          "value": 135801478000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 29780122000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 31738314000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 100
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2296160000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 446362000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 47717089000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 716380000
        }
      },
      "2012": {
        "accounts_payable": {
          "formula": "1520",
          "value": 33298003000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 6310998000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 106811408000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 6351063000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 1350999000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 12951229000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 46662687000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 46811977000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 23106863000
        },
        "cost_price": {
          "formula": "2120",
          "value": 143276289000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 188638598000
        },
        "current assets": {
          "formula": "1200",
          "value": 66943317000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 54
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 411708000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1741294000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2589864000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 8477928000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 39868091000
        },
        "funds": {
          "formula": "1250",
          "value": 13080297000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 167617000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 33307904000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 191780059000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3375684000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1186784000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 11429580000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 11841288000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13051698000
        },
        "net_profit": {
          "formula": "2400",
          "value": 3040593000
        },
        "other": {
          "formula": "2460",
          "value": -360364000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 197729000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 9221421000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 11733083000
        },
        "other_income": {
          "formula": "2340",
          "value": 14548136000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 16854909000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 190247000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 49132596000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 1001763000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 457483000
        },
        "profit": {
          "formula": "2200",
          "value": 3890043000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 6.5
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 31
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 53964000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 705108000
        },
        "revenue": {
          "formula": "2110",
          "value": 176584193000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 2.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 46249232000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 48158143000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 45
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3077494000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 242808000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 857160000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 44718599000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1335246000
        }
      },
      "2013": {
        "accounts_payable": {
          "formula": "1520",
          "value": 36164508000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 7045426000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 108874045000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 16298936000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 5669121000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 892834000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 46655928000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 55822487000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 27270173000
        },
        "cost_price": {
          "formula": "2120",
          "value": 165571125000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 219261483000
        },
        "current assets": {
          "formula": "1200",
          "value": 67115025000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 47
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 396111000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1207559000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2717266000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 41759020000
        },
        "funds": {
          "formula": "1250",
          "value": 15615766000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 265098000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 40706012000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 229987457000
        },
        "income_tax": {
          "formula": "2410",
          "value": 5825753000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1041755000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 10776987000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 6384938000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 14521559000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10365895000
        },
        "net_profit": {
          "formula": "2400",
          "value": 11096946000
        },
        "other": {
          "formula": "2460",
          "value": -44143000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 164583000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 13174009000
        },
        "other_income": {
          "formula": "2340",
          "value": 23108821000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 173430000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 57691255000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 627788000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 428069000
        },
        "profit": {
          "formula": "2200",
          "value": 6390413000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 19.9
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 681085000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 57
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 12118000
        },
        "research_results": {
          "formula": "1120",
          "value": 359513000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 611894000
        },
        "revenue": {
          "formula": "2110",
          "value": 206277137000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 37057342000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 38529999000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 81
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3406072000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 715817000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 53834441000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1272676000
        }
      },
      "2014": {
        "accounts_payable": {
          "formula": "1520",
          "value": 53565168000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 8087529000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 145880279000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 19728316000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 5000000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 13268749000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 56680604000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 63283028000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 36421541000
        },
        "cost_price": {
          "formula": "2120",
          "value": 194444448000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 263135926000
        },
        "current assets": {
          "formula": "1200",
          "value": 85297184000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 55
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 396625000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1363973000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 805000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2668252000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 60583095000
        },
        "funds": {
          "formula": "1250",
          "value": 22824357000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 261582000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 45863277000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 276109093000
        },
        "income_tax": {
          "formula": "2410",
          "value": 6256222000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 715330000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 11417161000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 5786902000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 14137779000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13282594000
        },
        "net_profit": {
          "formula": "2400",
          "value": 13149221000
        },
        "other": {
          "formula": "2460",
          "value": -159112000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 228013000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 16877066000
        },
        "other_income": {
          "formula": "2340",
          "value": 34888137000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 220126000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 65305208000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 550193000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 693105000
        },
        "profit": {
          "formula": "2200",
          "value": 1354207000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 20.8
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 270185000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 50
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 503475000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 518371000
        },
        "revenue": {
          "formula": "2110",
          "value": 240307725000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0.6
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 66833917000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 68459472000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 28
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 4173369000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 786902000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 61376387000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 585841000
        }
      },
      "2015": {
        "accounts_payable": {
          "formula": "1520",
          "value": 63445547000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 8839644000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 186544805000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -17457060000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 12580636000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 50529235000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 69767754000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 49344061000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 29198182000
        },
        "cost_price": {
          "formula": "2120",
          "value": 316312246000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 430013527000
        },
        "current assets": {
          "formula": "1200",
          "value": 110013886000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 72
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 391401000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1614304000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 3416577000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 3078231000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 76530919000
        },
        "funds": {
          "formula": "1250",
          "value": 28946377000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 410688000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 49995239000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 412076928000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1584163000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 554779000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 11502405000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 13221102000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 21200970000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13980027000
        },
        "net_profit": {
          "formula": "2400",
          "value": -18927841000
        },
        "other": {
          "formula": "2460",
          "value": 495621000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 318268000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 72855755000
        },
        "other_income": {
          "formula": "2340",
          "value": 42097386000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 58135000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 51760454000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 2328161000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 3613922000
        },
        "profit": {
          "formula": "2200",
          "value": 11957413000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -38.4
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 1083468000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 31
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 522000000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 19069000
        },
        "revenue": {
          "formula": "2110",
          "value": 366307485000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 113974782000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 115999774000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -3
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 7081886000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 640466000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 47936722000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 483024000
        }
      },
      "2016": {
        "accounts_payable": {
          "formula": "1520",
          "value": 68138395000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 11135614000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 177285662000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 42081308000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 7862898000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 9308668000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 65744175000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 79963737000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 32332287000
        },
        "cost_price": {
          "formula": "2120",
          "value": 371562923000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 468870022000
        },
        "current assets": {
          "formula": "1200",
          "value": 100491279000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 53
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 387520000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1707450000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 926304000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 7220480000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 76794383000
        },
        "funds": {
          "formula": "1250",
          "value": 26229302000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 427717000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 56337604000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 498554300000
        },
        "income_tax": {
          "formula": "2410",
          "value": 11723479000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 50345000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 10687759000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 8451519000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 17739695000
        },
        "main_assets": {
          "formula": "1150",
          "value": 12073089000
        },
        "net_profit": {
          "formula": "2400",
          "value": 30616800000
        },
        "other": {
          "formula": "2460",
          "value": -414416000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 916620000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 38397719000
        },
        "other_income": {
          "formula": "2340",
          "value": 65945641000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 41025000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 82486424000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 3044449000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 4667107000
        },
        "profit": {
          "formula": "2200",
          "value": 12869703000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 38.3
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 876178000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 59
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 546964000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 72628000
        },
        "revenue": {
          "formula": "2110",
          "value": 427900527000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 77447063000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 79582230000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 30
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 6269546000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 636050000
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 588621000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 78502839000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 405332000
        }
      },
      "2017": {
        "accounts_payable": {
          "formula": "1520",
          "value": 82553305000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12742294000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 184506224000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 35224139000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 92169373000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 78721585000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 35171689000
        },
        "cost_price": {
          "formula": "2120",
          "value": 400268600000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 478943344000
        },
        "current assets": {
          "formula": "1200",
          "value": 134616278000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 49
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 2604138000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 11768160000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 18544406000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 49889946000
        },
        "funds": {
          "formula": "1250",
          "value": 34094269000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 408807000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 46380842000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 507386797000
        },
        "income_tax": {
          "formula": "2410",
          "value": 8723470000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 69825000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 550750000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 11054367000
        },
        "main_assets": {
          "formula": "1150",
          "value": 11072450000
        },
        "net_profit": {
          "formula": "2400",
          "value": 28443453000
        },
        "other": {
          "formula": "2460",
          "value": 685225000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 790457000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 23179506000
        },
        "other_income": {
          "formula": "2340",
          "value": 52915005000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 5289909000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 3586256000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 93502690000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 800569000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 4236094000
        },
        "profit": {
          "formula": "2200",
          "value": -1533141000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 36.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 566919000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 41
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 570130000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 61951000
        },
        "revenue": {
          "formula": "2110",
          "value": 446649442000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -0.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 82553305000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 94730272000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 63
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 7242830000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 3168364000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 550750000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 77271364000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 319349000
        }
      },
      "2018": {
        "accounts_payable": {
          "formula": "1520",
          "value": 93992946000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 13810326000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 171651899000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 4082708000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 82150336000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 60256178000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 29815806000
        },
        "cost_price": {
          "formula": "2120",
          "value": 499683382000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 570556978000
        },
        "current assets": {
          "formula": "1200",
          "value": 105434016000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 59
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 401439000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 9159956000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2500000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 17722982000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 66217883000
        },
        "funds": {
          "formula": "1250",
          "value": 9871604000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 359042000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 5013407000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 573353082000
        },
        "income_tax": {
          "formula": "2410",
          "value": 2755346000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 40946000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 564056000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 7883777000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13031367000
        },
        "net_profit": {
          "formula": "2400",
          "value": 2796104000
        },
        "other": {
          "formula": "2460",
          "value": 801488000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1111559000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 25960860000
        },
        "other_income": {
          "formula": "2340",
          "value": 63556751000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 3795427000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 2213828000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 70176615000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 2885714000
        },
        "profit": {
          "formula": "2200",
          "value": -38612725000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 4.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 800729000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 29
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 7039736000
        },
        "research_results": {
          "formula": "1120",
          "value": 436462000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 58974000
        },
        "revenue": {
          "formula": "2110",
          "value": 504696789000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -7.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 93992946000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 103511944000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 12
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 9363819000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 3848924000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 564056000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 65848670000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 436698000
        }
      },
      "2019": {
        "accounts_payable": {
          "formula": "1520",
          "value": 95785513000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 13074276000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 198931740000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 2317013000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 12524022000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 104635508000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 69726232000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 32512519000
        },
        "cost_price": {
          "formula": "2120",
          "value": 542976396000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 618774449000
        },
        "current assets": {
          "formula": "1200",
          "value": 124624352000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 59
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 458786000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 10404752000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 144669000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 19960050000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 74307388000
        },
        "funds": {
          "formula": "1250",
          "value": 7336914000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1082083000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 8791024000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 621195631000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 543413000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 8950352000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 9409138000
        },
        "main_assets": {
          "formula": "1150",
          "value": 12346077000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5286800000
        },
        "other": {
          "formula": "2460",
          "value": 104169000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1376892000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 7570486000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 30128901000
        },
        "other_income": {
          "formula": "2340",
          "value": 61357368000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 32854188000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 6824260000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 81671853000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 186526000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1246583000
        },
        "profit": {
          "formula": "2200",
          "value": -36795771000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 7.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 756791000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 13
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 316517000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53961000
        },
        "revenue": {
          "formula": "2110",
          "value": 551767420000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -6.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 108309535000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 119796370000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 15
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 10204179000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 7530352000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 1379866000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 68284001000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 926190000
        }
      },
      "2020": {
        "accounts_payable": {
          "formula": "1520",
          "value": 107355565000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 78701230000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12839436000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 2444535000
        },
        "balance": {
          "formula": "1600",
          "value": 271035127000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -123149777000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 53200000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 25536113000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 81570945000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 53276490000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 15794465000
        },
        "cost_price": {
          "formula": "2120",
          "value": 331733965000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 362956700000
        },
        "current assets": {
          "formula": "1200",
          "value": 173492749000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 26622644000
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 77
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 548174000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 6756514000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 360507000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 14292604000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 97542378000
        },
        "funds": {
          "formula": "1250",
          "value": 76194693000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1136272000
        },
        "gross_profit": {
          "formula": "2100",
          "value": -101967600000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 266429567000
        },
        "income_tax": {
          "formula": "2410",
          "value": 26622644000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 486263000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 76425999000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 76974173000
        },
        "main_assets": {
          "formula": "1150",
          "value": 11512554000
        },
        "net_profit": {
          "formula": "2400",
          "value": -96527133000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1042241000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 22826243000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 25331524000
        },
        "other_income": {
          "formula": "2340",
          "value": 34780671000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 37100675000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 61717450000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 3879954000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1882531000
        },
        "profit": {
          "formula": "2200",
          "value": -130601501000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -181.2
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 721487000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 23
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 255909000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53801000
        },
        "revenue": {
          "formula": "2110",
          "value": 229766365000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -36.2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 132891678000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 140784464000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 31
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 13226345000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 33172886000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 399756000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -28200730000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1098018000
        }
      },
      "2021": {
        "accounts_payable": {
          "formula": "1520",
          "value": 100062394000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12921502000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 2444535000
        },
        "balance": {
          "formula": "1600",
          "value": 262918603000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -56400964000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 105750000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 16999139000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 83489186000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 7669394000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 20901191000
        },
        "cost_price": {
          "formula": "2120",
          "value": 414313277000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 484200237000
        },
        "current assets": {
          "formula": "1200",
          "value": 172302107000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 94
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 573234000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 6930698000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2500002000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 12010532000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 90616496000
        },
        "funds": {
          "formula": "1250",
          "value": 70724111000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1157761000
        },
        "gross_profit": {
          "formula": "2100",
          "value": -35656061000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 427799273000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 443944000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 129525983000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 130099217000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10418368000
        },
        "net_profit": {
          "formula": "2400",
          "value": -45639139000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 615693000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 23313418000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 28821460000
        },
        "other_income": {
          "formula": "2340",
          "value": 45474799000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 20008502000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 25769000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 16331087000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 7242807000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 3641489000
        },
        "profit": {
          "formula": "2200",
          "value": -69478754000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -595.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 3537762000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 32
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 199868000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 53756000
        },
        "revenue": {
          "formula": "2110",
          "value": 378657216000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -15.5
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 117061533000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 125149992000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 47
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 13960819000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 43997520000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 462565000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -73807781000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1012296000
        }
      },
      "2023": {
        "accounts_payable": {
          "formula": "1520",
          "value": 226321375000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 10592527000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 3975771000
        },
        "balance": {
          "formula": "1600",
          "value": 934268135000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -30769788000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 43775000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 40362449000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 109809373000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": -97298540000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 6438807000
        },
        "cost_price": {
          "formula": "2120",
          "value": 490237089000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 710297531000
        },
        "current assets": {
          "formula": "1200",
          "value": 236738444000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 97
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 107368610000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 14904130000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 187000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 15319712000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 697529691000
        },
        "funds": {
          "formula": "1250",
          "value": 75903472000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 776178000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 7274226000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 679527743000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1907339000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 641833933000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 749202543000
        },
        "main_assets": {
          "formula": "1150",
          "value": 477261820000
        },
        "net_profit": {
          "formula": "2400",
          "value": -29456385000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 883225000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 498936182000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 156868027000
        },
        "other_income": {
          "formula": "2340",
          "value": 172079035000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 23707546000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 575584000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 25750378000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 46161081000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 9361809000
        },
        "profit": {
          "formula": "2200",
          "value": -9757108000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 3882657000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": -13
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 146389000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 53366000
        },
        "revenue": {
          "formula": "2110",
          "value": 497511315000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -1.9
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 266683824000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 282364132000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -11
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 49502996000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 175304228000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 99122751000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -231281399000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 452378000
        }
      },
      "2024": {
        "accounts_payable": {
          "formula": "1520",
          "value": 271974598000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 129676068000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 11859081000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 3975771000
        },
        "balance": {
          "formula": "1600",
          "value": 957079369000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 7533277000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 24650000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 19280139000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 123813531000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": -75339792000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 9312510000
        },
        "cost_price": {
          "formula": "2120",
          "value": 668067870000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 819183067000
        },
        "current assets": {
          "formula": "1200",
          "value": 252645501000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 93
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 113364529000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 25781920000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 4150000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 12116830000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 704433868000
        },
        "funds": {
          "formula": "1250",
          "value": 47724479000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 666632000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 44860614000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 826215810000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 20818151000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 601351343000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 714715872000
        },
        "main_assets": {
          "formula": "1150",
          "value": 440922424000
        },
        "net_profit": {
          "formula": "2400",
          "value": 21958748000
        },
        "other": {
          "formula": "2460",
          "value": -500534000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 126708000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 464347632000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 92317826000
        },
        "other_income": {
          "formula": "2340",
          "value": 90095644000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 15759990000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 10482511000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 64473289000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 37125246000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 12709171000
        },
        "profit": {
          "formula": "2200",
          "value": 23689023000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 4321024000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": -15
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 132576000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53252000
        },
        "revenue": {
          "formula": "2110",
          "value": 712928484000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 291254737000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 317703289000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -13
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 76590269000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 210362873000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 112353711000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -209322537000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 240514000
        }
      }
    },
    "financial_position_state": "bad",
    "has_debt": false,
    "non_circulating_assets": {
      "description": "Внеоборотные активы увеличились, в том числе за счет налоговых активов",
      "state": "normal"
    },
    "performance_description": "За последний год доходы предприятия увеличились, и оно стало прибыльным",
    "performance_results": "good",
    "profitability": {
      "description": "Доходность не определена, т.к. нет собственного капитала",
      "state": "bad"
    },
    "property_profitability": {
      "description": "Рентабельность имущества (2.3%) ниже среднеотраслевого значения (3.1%)",
      "state": "bad"
    },
    "property_situation_state": "normal",
    "sales_profitability": {
      "description": "Рентабельность затрат (3.4%) выше среднеотраслевого значения (0%)",
      "state": "good"
    },
    "security_current_activities": {
      "description": "Обеспеченность текущей деятельности собственными средствами низкая",
      "state": "bad"
    },
    "solvency": {
      "description": "Платежеспособность низкая: оборотные активы (источники погашения обязательств) на 13% меньше суммы обязательств",
      "state": "bad"
    },
    "taxes_and_fees": {}
  }
]
```


**Пример ответа для максимальной лицензии:**

```json
[
  {
    "current_assets": {
      "description": "Управление оборотными активами стало более экономным: долги покупателей стали собираться на 28.9% быстрее",
      "state": "good"
    },
    "dependence_on_creditors": {
      "description": "Зависит от кредиторов в значительной степени: доля обязательств в балансе (93%) больше 50%",
      "state": "bad"
    },
    "efficiency_state": "bad",
    "estate_description": {
      "description": "За последний год имущество выросло на 2.4% (с 934.3 млрд ₽ до 957.1 млрд ₽), что увеличило потенциал предприятия",
      "state": "good"
    },
    "financial_indicators": {
      "2004": {
        "accounts_payable": {
          "formula": "1520",
          "value": 6430286000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3492079000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2162703000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 24295701000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 8266483000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 222196000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1029422000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 11771184000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 16331005000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3404826000
        },
        "cost_price": {
          "formula": "2120",
          "value": 46495617000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 55703336000
        },
        "current assets": {
          "formula": "1200",
          "value": 16908626000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 33
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 302120000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2296070000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 7387075000
        },
        "funds": {
          "formula": "1250",
          "value": 1435166000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 9970000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 9881564000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 57773919000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1977379000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 58325000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 463131000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 463131000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3734614000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6330143000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 240935000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 1622199000
        },
        "other_income": {
          "formula": "2340",
          "value": 1195619000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 131204000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 16340975000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 81651000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 69915000
        },
        "profit": {
          "formula": "2200",
          "value": 4314035000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 38.8
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 63
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 37000
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 56377181000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 8.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 7459708000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 7501565000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 127
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2998698000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 987000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 11450693000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 401458000
        }
      },
      "2005": {
        "accounts_payable": {
          "formula": "1520",
          "value": 7488783000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3374528000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2297863000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 32753649000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 8365934000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 1960536000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1727967000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 18479142000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 20732824000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3522691000
        },
        "cost_price": {
          "formula": "2120",
          "value": 53737902000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 65752460000
        },
        "current assets": {
          "formula": "1200",
          "value": 25112416000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 37
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 1539207000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2385594000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 7641233000
        },
        "funds": {
          "formula": "1250",
          "value": 1647535000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 28914000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 9111376000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 73397427000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1667588000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 52682000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 2766817000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 2766817000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3935343000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6032405000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 5242770000
        },
        "other_income": {
          "formula": "2340",
          "value": 10100289000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 206807000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 20761738000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 230267000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 241053000
        },
        "profit": {
          "formula": "2200",
          "value": 3290822000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 29.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 68
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 62849278000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 5.5
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 9216750000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 9254008000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 172
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2939607000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 141327000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 806281000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 15970026000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 506925000
        }
      },
      "2006": {
        "accounts_payable": {
          "formula": "1520",
          "value": 7397459000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 3141650000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2249884000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 36729604000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 11432633000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1734889000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 17511329000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 26722298000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 3894878000
        },
        "cost_price": {
          "formula": "2120",
          "value": 57608388000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 73917181000
        },
        "current assets": {
          "formula": "1200",
          "value": 25819379000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 27
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 628627000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 5778379000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 10910225000
        },
        "funds": {
          "formula": "1250",
          "value": 4218281000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 115026000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 13744658000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 82012191000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3450987000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 44359000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 749449000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 749449000
        },
        "main_assets": {
          "formula": "1150",
          "value": 3855756000
        },
        "net_profit": {
          "formula": "2400",
          "value": 7981346000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 6669661000
        },
        "other_income": {
          "formula": "2340",
          "value": 10270678000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 208077000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 26837324000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 156747000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 180390000
        },
        "profit": {
          "formula": "2200",
          "value": 7599896000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 29.9
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 69
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 71353046000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 11.9
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 9132348000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 9257857000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 183
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3057965000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 197858000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 749449000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 22192378000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 403177000
        }
      },
      "2007": {
        "accounts_payable": {
          "formula": "1520",
          "value": 12444745000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 2901411000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 2927214000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 44871557000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 10747893000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1703484000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 24661472000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 30441623000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 4982897000
        },
        "cost_price": {
          "formula": "2120",
          "value": 61460691000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 84458602000
        },
        "current assets": {
          "formula": "1200",
          "value": 33369162000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 32
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 87473000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 4801493000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 11502395000
        },
        "funds": {
          "formula": "1250",
          "value": 1789870000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 172302000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 15634194000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 91854353000
        },
        "income_tax": {
          "formula": "2410",
          "value": 4030688000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 69718000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 88758000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 88758000
        },
        "main_assets": {
          "formula": "1150",
          "value": 4774144000
        },
        "net_profit": {
          "formula": "2400",
          "value": 6074369000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 6503000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 11656678000
        },
        "other_income": {
          "formula": "2340",
          "value": 14367075000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 283398000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 30613925000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 78980000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 108995000
        },
        "profit": {
          "formula": "2200",
          "value": 7724083000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 20
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 69
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 77094885000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 11.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 14148229000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 14341176000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 114
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3604371000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 215713000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 88758000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 26151942000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 181292000
        }
      },
      "2008": {
        "accounts_payable": {
          "formula": "1520",
          "value": 15265188000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 1811440000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 3750176000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 50339789000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 9386025000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 1820409000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 26737015000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 33084790000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 5389762000
        },
        "cost_price": {
          "formula": "2120",
          "value": 79322627000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 103031261000
        },
        "current assets": {
          "formula": "1200",
          "value": 37480108000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 34
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 181515000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 4401371000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 12859681000
        },
        "funds": {
          "formula": "1250",
          "value": 3014335000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 119213000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 15691333000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 108508861000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3712171000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 94064000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 43736000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 43736000
        },
        "main_assets": {
          "formula": "1150",
          "value": 5085152000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5807312000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 13898000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 10550142000
        },
        "other_income": {
          "formula": "2340",
          "value": 13201306000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 6000000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 219715000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 33204003000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 110129000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 73880000
        },
        "profit": {
          "formula": "2200",
          "value": 6551395000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 17.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 71
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 405967000
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 95013960000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 7.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 17085597000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 17211263000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 96
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3205803000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 64481000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 43736000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 30291047000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 254062000
        }
      },
      "2009": {
        "accounts_payable": {
          "formula": "1520",
          "value": 0
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 0
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 0
        },
        "balance": {
          "formula": "1600",
          "value": 0
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 0
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 0
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 0
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 0
        },
        "cost_price": {
          "formula": "2120",
          "value": 0
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "current assets": {
          "formula": "1200",
          "value": 0
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 100
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 0
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 0
        },
        "funds": {
          "formula": "1250",
          "value": 0
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 0
        },
        "gross_profit": {
          "formula": "2100",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 0
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 0
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 0
        },
        "main_assets": {
          "formula": "1150",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 0
        },
        "other_income": {
          "formula": "2340",
          "value": 0
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 0
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 0
        },
        "profit": {
          "formula": "2200",
          "value": 0
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 0
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 0
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 0
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 0
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 0
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 0
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 0
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 0
        }
      },
      "2010": {
        "accounts_payable": {
          "formula": "1520",
          "value": 0
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 0
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 0
        },
        "balance": {
          "formula": "1600",
          "value": 0
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 0
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 0
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 0
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 0
        },
        "cost_price": {
          "formula": "2120",
          "value": 0
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 0
        },
        "current assets": {
          "formula": "1200",
          "value": 0
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 100
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 0
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 0
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 0
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 0
        },
        "funds": {
          "formula": "1250",
          "value": 0
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 0
        },
        "gross_profit": {
          "formula": "2100",
          "value": 0
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 0
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 0
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 0
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 0
        },
        "main_assets": {
          "formula": "1150",
          "value": 0
        },
        "net_profit": {
          "formula": "2400",
          "value": 0
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 0
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 0
        },
        "other_income": {
          "formula": "2340",
          "value": 0
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 0
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 0
        },
        "profit": {
          "formula": "2200",
          "value": 0
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 0
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 0
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 0
        },
        "revenue": {
          "formula": "2110",
          "value": 0
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 0
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 0
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 0
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 0
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 0
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 0
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 0
        }
      },
      "2011": {
        "accounts_payable": {
          "formula": "1520",
          "value": 25475220000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 6166879000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 96725423000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 13924557000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 12000000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 4304902000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 44824272000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 49610609000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 15954667000
        },
        "cost_price": {
          "formula": "2120",
          "value": 111050208000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 142863788000
        },
        "current assets": {
          "formula": "1200",
          "value": 59651907000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 46
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 373513000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1733749000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 8019002000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 10147225000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 37073516000
        },
        "funds": {
          "formula": "1250",
          "value": 3616956000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 224443000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 24751270000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 153803001000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3247809000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 81973000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 15002987000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 15376500000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10663075000
        },
        "net_profit": {
          "formula": "2400",
          "value": 10483665000
        },
        "other": {
          "formula": "2460",
          "value": 130058000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 179137000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 2556625000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 5794897000
        },
        "other_income": {
          "formula": "2340",
          "value": 16773992000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 116254000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 51942314000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 911793000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1111277000
        },
        "profit": {
          "formula": "2200",
          "value": 2629724000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 21.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 77
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 287729000
        },
        "research_results": {
          "formula": "1120",
          "value": 21451000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 792979000
        },
        "revenue": {
          "formula": "2110",
          "value": 135801478000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 29780122000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 31738314000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 100
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 2296160000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 446362000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 47717089000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 716380000
        }
      },
      "2012": {
        "accounts_payable": {
          "formula": "1520",
          "value": 33298003000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 6310998000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 106811408000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 6351063000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 1350999000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 12951229000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 46662687000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 46811977000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 23106863000
        },
        "cost_price": {
          "formula": "2120",
          "value": 143276289000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 188638598000
        },
        "current assets": {
          "formula": "1200",
          "value": 66943317000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 54
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 411708000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1741294000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2589864000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 8477928000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 39868091000
        },
        "funds": {
          "formula": "1250",
          "value": 13080297000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 167617000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 33307904000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 191780059000
        },
        "income_tax": {
          "formula": "2410",
          "value": 3375684000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1186784000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 11429580000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 11841288000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13051698000
        },
        "net_profit": {
          "formula": "2400",
          "value": 3040593000
        },
        "other": {
          "formula": "2460",
          "value": -360364000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 197729000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 9221421000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 11733083000
        },
        "other_income": {
          "formula": "2340",
          "value": 14548136000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 16854909000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 190247000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 49132596000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 1001763000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 457483000
        },
        "profit": {
          "formula": "2200",
          "value": 3890043000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 6.5
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 0
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 31
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 53964000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 705108000
        },
        "revenue": {
          "formula": "2110",
          "value": 176584193000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 2.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 46249232000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 48158143000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 45
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3077494000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 242808000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 857160000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 44718599000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1335246000
        }
      },
      "2013": {
        "accounts_payable": {
          "formula": "1520",
          "value": 36164508000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 7045426000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 108874045000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 16298936000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 5669121000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 892834000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 46655928000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 55822487000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 27270173000
        },
        "cost_price": {
          "formula": "2120",
          "value": 165571125000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 219261483000
        },
        "current assets": {
          "formula": "1200",
          "value": 67115025000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 47
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 396111000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1207559000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2717266000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 41759020000
        },
        "funds": {
          "formula": "1250",
          "value": 15615766000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 265098000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 40706012000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 229987457000
        },
        "income_tax": {
          "formula": "2410",
          "value": 5825753000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1041755000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 10776987000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 6384938000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 14521559000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10365895000
        },
        "net_profit": {
          "formula": "2400",
          "value": 11096946000
        },
        "other": {
          "formula": "2460",
          "value": -44143000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 164583000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 13174009000
        },
        "other_income": {
          "formula": "2340",
          "value": 23108821000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 173430000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 57691255000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 627788000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 428069000
        },
        "profit": {
          "formula": "2200",
          "value": 6390413000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 19.9
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 681085000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 57
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 12118000
        },
        "research_results": {
          "formula": "1120",
          "value": 359513000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 611894000
        },
        "revenue": {
          "formula": "2110",
          "value": 206277137000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 37057342000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 38529999000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 81
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 3406072000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 715817000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 53834441000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1272676000
        }
      },
      "2014": {
        "accounts_payable": {
          "formula": "1520",
          "value": 53565168000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 8087529000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 145880279000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 19728316000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 5000000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 13268749000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 56680604000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 63283028000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 36421541000
        },
        "cost_price": {
          "formula": "2120",
          "value": 194444448000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 263135926000
        },
        "current assets": {
          "formula": "1200",
          "value": 85297184000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 55
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 396625000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1363973000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 805000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 2668252000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 60583095000
        },
        "funds": {
          "formula": "1250",
          "value": 22824357000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 261582000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 45863277000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 276109093000
        },
        "income_tax": {
          "formula": "2410",
          "value": 6256222000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 715330000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 11417161000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 5786902000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 14137779000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13282594000
        },
        "net_profit": {
          "formula": "2400",
          "value": 13149221000
        },
        "other": {
          "formula": "2460",
          "value": -159112000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 228013000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 16877066000
        },
        "other_income": {
          "formula": "2340",
          "value": 34888137000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 220126000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 65305208000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 550193000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 693105000
        },
        "profit": {
          "formula": "2200",
          "value": 1354207000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 20.8
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 270185000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 50
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 503475000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 518371000
        },
        "revenue": {
          "formula": "2110",
          "value": 240307725000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 0.6
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 66833917000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 68459472000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 28
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 4173369000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 786902000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 61376387000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 585841000
        }
      },
      "2015": {
        "accounts_payable": {
          "formula": "1520",
          "value": 63445547000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 8839644000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 186544805000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -17457060000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 12580636000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 50529235000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 69767754000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 49344061000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 29198182000
        },
        "cost_price": {
          "formula": "2120",
          "value": 316312246000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 430013527000
        },
        "current assets": {
          "formula": "1200",
          "value": 110013886000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 72
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 391401000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1614304000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 3416577000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 3078231000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 76530919000
        },
        "funds": {
          "formula": "1250",
          "value": 28946377000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 410688000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 49995239000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 412076928000
        },
        "income_tax": {
          "formula": "2410",
          "value": 1584163000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 554779000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 11502405000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 13221102000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 21200970000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13980027000
        },
        "net_profit": {
          "formula": "2400",
          "value": -18927841000
        },
        "other": {
          "formula": "2460",
          "value": 495621000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 318268000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 72855755000
        },
        "other_income": {
          "formula": "2340",
          "value": 42097386000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 58135000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 51760454000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 2328161000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 3613922000
        },
        "profit": {
          "formula": "2200",
          "value": 11957413000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -38.4
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 1083468000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 31
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 522000000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 19069000
        },
        "revenue": {
          "formula": "2110",
          "value": 366307485000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 113974782000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 115999774000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -3
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 7081886000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 640466000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 47936722000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 483024000
        }
      },
      "2016": {
        "accounts_payable": {
          "formula": "1520",
          "value": 68138395000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 11135614000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 177285662000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 42081308000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 7862898000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 9308668000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 65744175000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 79963737000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 32332287000
        },
        "cost_price": {
          "formula": "2120",
          "value": 371562923000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 468870022000
        },
        "current assets": {
          "formula": "1200",
          "value": 100491279000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 53
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 387520000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 1707450000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 926304000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 7220480000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 76794383000
        },
        "funds": {
          "formula": "1250",
          "value": 26229302000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 427717000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 56337604000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 498554300000
        },
        "income_tax": {
          "formula": "2410",
          "value": 11723479000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 50345000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 10687759000
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 8451519000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 17739695000
        },
        "main_assets": {
          "formula": "1150",
          "value": 12073089000
        },
        "net_profit": {
          "formula": "2400",
          "value": 30616800000
        },
        "other": {
          "formula": "2460",
          "value": -414416000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 916620000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 38397719000
        },
        "other_income": {
          "formula": "2340",
          "value": 65945641000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 0
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 41025000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 82486424000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 3044449000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 4667107000
        },
        "profit": {
          "formula": "2200",
          "value": 12869703000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 38.3
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 876178000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 59
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 546964000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 72628000
        },
        "revenue": {
          "formula": "2110",
          "value": 427900527000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 77447063000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 79582230000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 30
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 6269546000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 636050000
        },
        "tax_assets": {
          "formula": "1180",
          "value": 0
        },
        "tax_duties": {
          "formula": "1420",
          "value": 588621000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 78502839000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 405332000
        }
      },
      "2017": {
        "accounts_payable": {
          "formula": "1520",
          "value": 82553305000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12742294000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 184506224000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 35224139000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 92169373000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 78721585000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 35171689000
        },
        "cost_price": {
          "formula": "2120",
          "value": 400268600000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 478943344000
        },
        "current assets": {
          "formula": "1200",
          "value": 134616278000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 49
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 2604138000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 11768160000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 0
        },
        "financial_investments": {
          "formula": "1170",
          "value": 18544406000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 49889946000
        },
        "funds": {
          "formula": "1250",
          "value": 34094269000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 408807000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 46380842000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 507386797000
        },
        "income_tax": {
          "formula": "2410",
          "value": 8723470000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 69825000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 550750000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 11054367000
        },
        "main_assets": {
          "formula": "1150",
          "value": 11072450000
        },
        "net_profit": {
          "formula": "2400",
          "value": 28443453000
        },
        "other": {
          "formula": "2460",
          "value": 685225000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 790457000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 23179506000
        },
        "other_income": {
          "formula": "2340",
          "value": 52915005000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 5289909000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 3586256000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 93502690000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 800569000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 4236094000
        },
        "profit": {
          "formula": "2200",
          "value": -1533141000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 36.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 566919000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 41
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 570130000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 61951000
        },
        "revenue": {
          "formula": "2110",
          "value": 446649442000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -0.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 82553305000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 94730272000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 63
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 7242830000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 3168364000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 550750000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 77271364000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 319349000
        }
      },
      "2018": {
        "accounts_payable": {
          "formula": "1520",
          "value": 93992946000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 13810326000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 171651899000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 4082708000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 0
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 82150336000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 60256178000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 29815806000
        },
        "cost_price": {
          "formula": "2120",
          "value": 499683382000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 570556978000
        },
        "current assets": {
          "formula": "1200",
          "value": 105434016000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 59
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 401439000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 9159956000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2500000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 17722982000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 66217883000
        },
        "funds": {
          "formula": "1250",
          "value": 9871604000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 359042000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 5013407000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 573353082000
        },
        "income_tax": {
          "formula": "2410",
          "value": 2755346000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 40946000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 564056000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 7883777000
        },
        "main_assets": {
          "formula": "1150",
          "value": 13031367000
        },
        "net_profit": {
          "formula": "2400",
          "value": 2796104000
        },
        "other": {
          "formula": "2460",
          "value": 801488000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1111559000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 0
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 25960860000
        },
        "other_income": {
          "formula": "2340",
          "value": 63556751000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 3795427000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 2213828000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 70176615000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 0
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 2885714000
        },
        "profit": {
          "formula": "2200",
          "value": -38612725000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 4.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 800729000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 29
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 7039736000
        },
        "research_results": {
          "formula": "1120",
          "value": 436462000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 58974000
        },
        "revenue": {
          "formula": "2110",
          "value": 504696789000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -7.1
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 93992946000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 103511944000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 12
        },
        "source": "ROSSTAT",
        "stocks": {
          "formula": "1210",
          "value": 9363819000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 3848924000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 564056000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 65848670000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 436698000
        }
      },
      "2019": {
        "accounts_payable": {
          "formula": "1520",
          "value": 95785513000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 13074276000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 1110616000
        },
        "balance": {
          "formula": "1600",
          "value": 198931740000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 2317013000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 0
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 12524022000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 104635508000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 69726232000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 32512519000
        },
        "cost_price": {
          "formula": "2120",
          "value": 542976396000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 618774449000
        },
        "current assets": {
          "formula": "1200",
          "value": 124624352000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 59
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 458786000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 10404752000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 144669000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 19960050000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 74307388000
        },
        "funds": {
          "formula": "1250",
          "value": 7336914000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1082083000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 8791024000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 621195631000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 543413000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 8950352000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 9409138000
        },
        "main_assets": {
          "formula": "1150",
          "value": 12346077000
        },
        "net_profit": {
          "formula": "2400",
          "value": 5286800000
        },
        "other": {
          "formula": "2460",
          "value": 104169000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1376892000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 7570486000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 30128901000
        },
        "other_income": {
          "formula": "2340",
          "value": 61357368000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 32854188000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 6824260000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 81671853000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 186526000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1246583000
        },
        "profit": {
          "formula": "2200",
          "value": -36795771000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 7.6
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 756791000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 13
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 316517000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53961000
        },
        "revenue": {
          "formula": "2110",
          "value": 551767420000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -6.3
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 108309535000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 119796370000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 15
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 10204179000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 7530352000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 1379866000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": 68284001000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 926190000
        }
      },
      "2020": {
        "accounts_payable": {
          "formula": "1520",
          "value": 107355565000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 78701230000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12839436000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 2444535000
        },
        "balance": {
          "formula": "1600",
          "value": 271035127000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -123149777000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 53200000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 25536113000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 81570945000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 53276490000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 15794465000
        },
        "cost_price": {
          "formula": "2120",
          "value": 331733965000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 362956700000
        },
        "current assets": {
          "formula": "1200",
          "value": 173492749000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 26622644000
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 77
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 548174000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 6756514000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 360507000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 14292604000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 97542378000
        },
        "funds": {
          "formula": "1250",
          "value": 76194693000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1136272000
        },
        "gross_profit": {
          "formula": "2100",
          "value": -101967600000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 266429567000
        },
        "income_tax": {
          "formula": "2410",
          "value": 26622644000
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 486263000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 76425999000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 76974173000
        },
        "main_assets": {
          "formula": "1150",
          "value": 11512554000
        },
        "net_profit": {
          "formula": "2400",
          "value": -96527133000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 1042241000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 22826243000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 25331524000
        },
        "other_income": {
          "formula": "2340",
          "value": 34780671000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 37100675000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 0
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 61717450000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 3879954000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 1882531000
        },
        "profit": {
          "formula": "2200",
          "value": -130601501000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -181.2
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 721487000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 23
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 255909000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53801000
        },
        "revenue": {
          "formula": "2110",
          "value": 229766365000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -36.2
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 132891678000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 140784464000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 31
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 13226345000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 33172886000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 399756000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -28200730000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1098018000
        }
      },
      "2021": {
        "accounts_payable": {
          "formula": "1520",
          "value": 100062394000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 12921502000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 2444535000
        },
        "balance": {
          "formula": "1600",
          "value": 262918603000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -56400964000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 105750000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 16999139000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 83489186000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": 7669394000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 20901191000
        },
        "cost_price": {
          "formula": "2120",
          "value": 414313277000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 484200237000
        },
        "current assets": {
          "formula": "1200",
          "value": 172302107000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 94
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 573234000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 6930698000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 2500002000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 12010532000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 90616496000
        },
        "funds": {
          "formula": "1250",
          "value": 70724111000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 1157761000
        },
        "gross_profit": {
          "formula": "2100",
          "value": -35656061000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 427799273000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 443944000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 129525983000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 130099217000
        },
        "main_assets": {
          "formula": "1150",
          "value": 10418368000
        },
        "net_profit": {
          "formula": "2400",
          "value": -45639139000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 615693000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 23313418000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 28821460000
        },
        "other_income": {
          "formula": "2340",
          "value": 45474799000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 20008502000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 25769000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 16331087000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 7242807000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 3641489000
        },
        "profit": {
          "formula": "2200",
          "value": -69478754000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": -595.1
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 3537762000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": 32
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 199868000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 53756000
        },
        "revenue": {
          "formula": "2110",
          "value": 378657216000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -15.5
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 117061533000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 125149992000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": 47
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 13960819000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 43997520000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 462565000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -73807781000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 1012296000
        }
      },
      "2023": {
        "accounts_payable": {
          "formula": "1520",
          "value": 226321375000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 0
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 10592527000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 3975771000
        },
        "balance": {
          "formula": "1600",
          "value": 934268135000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": -30769788000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 43775000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 40362449000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 109809373000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": -97298540000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 6438807000
        },
        "cost_price": {
          "formula": "2120",
          "value": 490237089000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 710297531000
        },
        "current assets": {
          "formula": "1200",
          "value": 236738444000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 97
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 107368610000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 14904130000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 187000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 15319712000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 697529691000
        },
        "funds": {
          "formula": "1250",
          "value": 75903472000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 776178000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 7274226000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 679527743000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 1907339000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 641833933000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 749202543000
        },
        "main_assets": {
          "formula": "1150",
          "value": 477261820000
        },
        "net_profit": {
          "formula": "2400",
          "value": -29456385000
        },
        "other": {
          "formula": "2460",
          "value": 0
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 883225000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 498936182000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 156868027000
        },
        "other_income": {
          "formula": "2340",
          "value": 172079035000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 23707546000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 575584000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 25750378000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 46161081000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 9361809000
        },
        "profit": {
          "formula": "2200",
          "value": -9757108000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 3882657000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": -13
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 146389000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 0
        },
        "revaluation": {
          "formula": "1340",
          "value": 53366000
        },
        "revenue": {
          "formula": "2110",
          "value": 497511315000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": -1.9
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 266683824000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 282364132000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -11
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 49502996000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 175304228000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 99122751000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -231281399000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 452378000
        }
      },
      "2024": {
        "accounts_payable": {
          "formula": "1520",
          "value": 271974598000
        },
        "additional_capital": {
          "formula": "1350",
          "value": 129676068000
        },
        "administrative_expenses": {
          "formula": "2220",
          "value": 11859081000
        },
        "authorized_capital": {
          "formula": "1310",
          "value": 3975771000
        },
        "balance": {
          "formula": "1600",
          "value": 957079369000
        },
        "before_taxation_profit": {
          "formula": "2300",
          "value": 7533277000
        },
        "borrowed_funds_long": {
          "formula": "1410",
          "value": 24650000000
        },
        "borrowed_funds_short": {
          "formula": "1510",
          "value": 19280139000
        },
        "buyers_debts": {
          "formula": "1230",
          "value": 123813531000
        },
        "capital_and_reserves": {
          "formula": "1300",
          "value": -75339792000
        },
        "commercial_expenses": {
          "formula": "2210",
          "value": 9312510000
        },
        "cost_price": {
          "formula": "2120",
          "value": 668067870000
        },
        "costs": {
          "formula": "2120 + 2210 + 2220 + 2330 + 2350 - 2410 - 2460",
          "value": 819183067000
        },
        "current assets": {
          "formula": "1200",
          "value": 252645501000
        },
        "current_income_tax": {
          "formula": "2411",
          "value": 0
        },
        "deferred_income_tax": {
          "formula": "2412",
          "value": 0
        },
        "dependency": {
          "formula": "(Обязательства - Прочие обязательства) / (Баланс - Прочие обязательства) * 100%",
          "value": 93
        },
        "estimated_duties_long": {
          "formula": "1430",
          "value": 113364529000
        },
        "estimated_duties_short": {
          "formula": "1540",
          "value": 25781920000
        },
        "financial_deposits": {
          "formula": "1240",
          "value": 4150000000
        },
        "financial_investments": {
          "formula": "1170",
          "value": 12116830000
        },
        "fixed_assets": {
          "formula": "1100",
          "value": 704433868000
        },
        "funds": {
          "formula": "1250",
          "value": 47724479000
        },
        "future_periods_revenue": {
          "formula": "1530",
          "value": 666632000
        },
        "gross_profit": {
          "formula": "2100",
          "value": 44860614000
        },
        "income": {
          "formula": "2110 + 2320 + 2310 + 2340",
          "value": 826215810000
        },
        "income_tax": {
          "formula": "2410",
          "value": 0
        },
        "intangible_assets": {
          "formula": "1110",
          "value": 20818151000
        },
        "intangible_search_assets": {
          "formula": "1130",
          "value": 0
        },
        "long_term_duties": {
          "formula": "1410 + 1420 + 1450",
          "value": 601351343000
        },
        "long_term_liabilities": {
          "formula": "1400",
          "value": 714715872000
        },
        "main_assets": {
          "formula": "1150",
          "value": 440922424000
        },
        "net_profit": {
          "formula": "2400",
          "value": 21958748000
        },
        "other": {
          "formula": "2460",
          "value": -500534000
        },
        "other_current_assets": {
          "formula": "1260",
          "value": 126708000
        },
        "other_duties_long": {
          "formula": "1450",
          "value": 464347632000
        },
        "other_duties_short": {
          "formula": "1550",
          "value": 0
        },
        "other_expenses": {
          "formula": "2350",
          "value": 92317826000
        },
        "other_income": {
          "formula": "2340",
          "value": 90095644000
        },
        "other_noncurrent_assets": {
          "formula": "1190",
          "value": 15759990000
        },
        "other_organizations_participation_income": {
          "formula": "2310",
          "value": 10482511000
        },
        "own_funds": {
          "formula": "1310 - 1320 + 1340 + 1350 + 1360 + 1370 + 1430 + 1530 + 1540 + 1550 или 1300 + 1430 + 1530 + 1540 + 1550 (при наличии строки 1300)",
          "value": 64473289000
        },
        "percent_payable": {
          "formula": "2330",
          "value": 37125246000
        },
        "percent_receivable": {
          "formula": "2320",
          "value": 12709171000
        },
        "profit": {
          "formula": "2200",
          "value": 23689023000
        },
        "profitability": {
          "formula": "Чистая прибыль / Собственный капитал * 100%",
          "value": 0
        },
        "profitable_deposits": {
          "formula": "1160",
          "value": 4321024000
        },
        "provision": {
          "formula": "(Собственные средства - Внеоборотные активы + Долгосрочные обязательства) / Оборотные активы * 100%",
          "value": -15
        },
        "repurchased_shares": {
          "formula": "1320",
          "value": 0
        },
        "research_results": {
          "formula": "1120",
          "value": 132576000
        },
        "reserve_capital": {
          "formula": "1360",
          "value": 277654000
        },
        "revaluation": {
          "formula": "1340",
          "value": 53252000
        },
        "revenue": {
          "formula": "2110",
          "value": 712928484000
        },
        "sales_profitability": {
          "formula": "Прибыль от продаж / Выручка * 100%",
          "value": 3.4
        },
        "short_term_duties": {
          "formula": "1510 + 1520 + 1550",
          "value": 291254737000
        },
        "short_term_liabilities": {
          "formula": "1500",
          "value": 317703289000
        },
        "solvency": {
          "formula": "(Оборотные средства - Прочие обязательства - Текущие обязательства) / Текущие обязательства * 100%",
          "value": -13
        },
        "source": "GIRBO",
        "stocks": {
          "formula": "1210",
          "value": 76590269000
        },
        "tangible_search_assets": {
          "formula": "1140",
          "value": 0
        },
        "tax_assets": {
          "formula": "1180",
          "value": 210362873000
        },
        "tax_duties": {
          "formula": "1420",
          "value": 112353711000
        },
        "undistributed_profits": {
          "formula": "1370",
          "value": -209322537000
        },
        "value_added_tax": {
          "formula": "1220",
          "value": 240514000
        }
      }
    },
    "financial_position_state": "bad",
    "has_debt": false,
    "non_circulating_assets": {
      "description": "Внеоборотные активы увеличились, в том числе за счет налоговых активов",
      "state": "normal"
    },
    "performance_description": "За последний год доходы предприятия увеличились, и оно стало прибыльным",
    "performance_results": "good",
    "profitability": {
      "description": "Доходность не определена, т.к. нет собственного капитала",
      "state": "bad"
    },
    "property_profitability": {
      "description": "Рентабельность имущества (2.3%) ниже среднеотраслевого значения (3.1%)",
      "state": "bad"
    },
    "property_situation_state": "normal",
    "sales_profitability": {
      "description": "Рентабельность затрат (3.4%) выше среднеотраслевого значения (0%)",
      "state": "good"
    },
    "security_current_activities": {
      "description": "Обеспеченность текущей деятельности собственными средствами низкая",
      "state": "bad"
    },
    "solvency": {
      "description": "Платежеспособность низкая: оборотные активы (источники погашения обязательств) на 13% меньше суммы обязательств",
      "state": "bad"
    },
    "taxes_and_fees": {},
    "revenue_competitors": [
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
      }
    ]
  }
]
```