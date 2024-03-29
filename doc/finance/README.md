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
      }
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
      }
    }  
  },
  "performance_results": "normal",
  "performance_description": "За последний год доходы предприятия сократились, и произошло резкое сокращение прибыли",
  "has_debt": true,
  "taxes_and_fees": {
    "2020": {
      "revenue_tax": 124542.0,
      "nds_tax": 124542.0,
      "in_pf": 124542.0
    },
    "2019": {
      "revenue_tax": 0.0,
      "nds_tax": 500.0,
      "in_pf": 300.0
    }
  },
  "revenue_competitors": [
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
    }
  ],
  "efficiency_state": "good",
  "profitability": {
    "state": "good",
    "description": "Доход собственника выше среднего (16 коп. на вложенный рубль)"
  },
  "property_profitability": {
    "state": "good",
    "description": "Рентабельность имущества (4%) соответствует среднеотраслевому значению (4%)"
  },
  "sales_profitability": {
    "state": "good",
    "description": "Рентабельность продаж (5.1%) выше среднеотраслевого значения (2.6%)"
  },
  "property_situation_state": "bad",
  "current_assets": {
    "state": "bad",
    "description": "Управление оборотными активами стало менее экономным: сократилась оборачиваемость запасов на 97%, долги покупателей стали собираться на 100% медленнее"
  },
  "non_circulating_assets": {
    "state": "bad",
    "description": "На долгосрочное развитие средств не выделено"
  },
  "estate_description": {
    "state": "bad",
    "description": "За последний год имущество сократилось на -39% (с 293.7 млн руб. до 178.8 млн руб.), что уменьшило потенциал предприятия"
  },
  "financial_position_state": "normal",
  "solvency": {
    "state": "good",
    "description": "Платежеспособность на приемлемом уровне: оборотные активы (источники погашения обязательств) больше обязательств на 34%"
  },
  "dependence_on_creditors": {
  "state": "bad",
    "description": "Зависимость от кредиторов значительная: доля обязательств в балансе (75%) больше 50%"
  },
  "security_current_activities": {
    "state": "normal",
    "description": "Обеспеченность текущей деятельности собственными средствами средняя (25% > 10% суммы оборотных активов)"
  }
}
```

## Стоимость бизнеса:

Получить аналитические данные по стоимости бизнеса.

Для компаний, акции которых, обращаются на бирже, рыночная стоимость компании рассчитывается исходя из актуальной стоимости акции.

Для остальных - это максимальное из четырех значений, полученных методами: чистых активов, дисконтирования, регрессионного анализа, рынка капитала. Расчет всеми методами производится на основании данных последней отчетности, учитывая возможность применения метода.

**Ограничения по лицензии**: В базовой лицензии отсутствуют конкуренты по стоимости.
Данные по рассчитываемым методам предоставлены только за последний рассчитанный год.

**URL** : `/cost-business/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "market_value": {
      "type": "array",
      "description": "Рыночная стоимость компаниию",
      "items":
      [
        {
          "type": "object",
          "properties": {
            "code": {
              "type": "string",
              "description": "Код ценной бумаги"
            },
            "is_privileged": {
              "type": "boolean",
              "description": "Признак привилегированной бумаги"
            },
            "values": {
              "type": "array",
              "description": "Значения ценной бумаги",
              "items":
              [
                {
                  "type": "object",
                  "properties": {
                    "date": {
                      "type": "string",
                      "description": "Дата ценной бумаги"
                    },
                    "price": {
                      "type": "number",
                      "description": "Ценна на дату"
                    },
                    "counts": {
                      "type": "integer",
                      "description": "Выпуск"
                    }
                  }
                }
              ]
            }
          }
        }
      ]
    },
    "net_assets": {
      "type": "object",
      "description": "Метод чистых активов. Ключ - Год.",
      "properties": {
        "year": {
          "type": "number",
          "description": "Значение на заданный период."
        }
      }
    },
    "discounted_net_flows": {
      "type": "object",
      "description": "Метод дисконтирования денежных потоков. Ключ - Год.",
      "properties": {
        "year": {
          "type": "number",
          "description": "Значение на заданный период."
        }
      }
    },
    "capital_market": {
      "type": "object",
      "description": "Метод рынка капитала. Ключ - Год",
      "properties": {
        "year": {
          "type": "number",
          "description": "Значение на заданный период."
        }
      }
    },
    "regression_analysis": {
      "type": "object",
      "description": "Метод регрессионного анализа. Ключ - Год",
      "properties": {
        "year": {
          "type": "number",
          "description": "Значение на заданный период."
        }
      }
    },
    "cost_competitors": {
      "type": "object",
      "description": "Конкуренты по стоимости",
      "properties": {
        "inn": {
          "type": "string",
          "description": "ИНН контрагента"
        },
        "company_name": {
          "type": "string",
          "description": "Название контрагента"
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
          "description": "Выручка"
        },
        "cost": {
          "type": "number",
          "description": "Стоимость"
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
  }
}
```

**Пример ответа:**

```json
{
  "market_value": [
    {
      "code": "GAZP",
      "is_privileged": false,
      "values": [
        {
          "date": "2021-01-04",
          "price": 212.71,
          "counts": 23673512900
        },
        {
          "date": "2021-01-05",
          "price": 215.32,
          "counts": 23673512900
        }
      ]
    }
  ],
  "net_assets": {
    "2020": 3502.6,
    "2019": 45648.6,
    "2018": 51278.6
  },
  "discounted_net_flows": {
    "2020": 3502.6,
    "2019": 45648.6,
    "2018": 51278.6
  },
  "capital_market": {
    "2020": 3502.6,
    "2019": 45648.6,
    "2018": 51278.6
  },
  "regression_analysis": {
    "2020": 3502.6,
    "2019": 45648.6,
    "2018": 51278.6
  },
  "cost_competitors": {
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
  }
}
```

## Надежность:

Получить аналитические данные по надежности.

**Ограничения по лицензии**: В базовой лицензии показываются только итоговые суммарные значения показателей надежности без расшифровки и описания.

**URL** : `/reliability/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `user_settings(str)` - true если использовать пользовательские настройки. По умолчанию false


**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "additional_sum_value": {
      "type": "number",
      "description": "Сумма баллов по дополнительным аспектам"
    },
    "advantages_sum_value": {
      "type": "number",
      "description": "Суммарное значение положительных аспектов надежности"
    },
    "disadvantages_sum_value": {
      "type": "number",
      "description": "Суммарное значение отрицательных аспектов надежности"
    },
    "has_critical": {
      "type": "boolean",
      "description": "Признак наличия критически отрицательного аспекта"
    },
    "advantages": {
      "type": "array",
      "description": "Список положительных аспектов влияющих на надежность",
      "items": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            },
            "comments": {
              "type": "string",
              "description": "Комментарии к аспекту"
            },
            "links": {
              "type": "array",
              "description": "ссылки",
              "items": [
                {
                  "type": "str"
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            }
          }
        }
      ]
    },
    "disadvantages": {
      "type": "array",
      "description": "Список отрицательных аспектов влияющих на надежность",
      "items": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            },
            "comments": {
              "type": "string",
              "description": "Комментарии к аспекту"
            },
            "links": {
              "type": "array",
              "description": "ссылки",
              "items": [
                {
                  "type": "str"
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            }
          }
        }
      ]
    }
  }
}
```

**Пример ответа:**

```json
{
  "additional_sum_value": 0,
  "advantages_sum_value": 5,
  "disadvantages_sum_value": -7,
  "advantages": [
    {
      "description": "Компания финансово устойчива",
      "links": null,
      "comments": ["Обязательства в балансе составляют значительную долю – 38.3%"],
      "value": 5
    }
  ],
  "disadvantages ": [
    {
      "description": "Компания не отвечает на требования налоговой",
      "links": null,
      "comments": null,
      "value": -7
    }
  ]
}
```

## Надежность блоками:

Получить аналитические данные по надежности.

**Ограничения по лицензии**: В базовой лицензии показываются только итоговые суммарные значения показателей надежности без расшифровки и описания.

**URL** : `/reliability/blocks/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

**Необязательные параметры** :
- `user_settings(str)` - true если использовать пользовательские настройки. По умолчанию false


**Метод** : `GET`

**Формат ответа:**

```json
{
  "type": "object",
  "properties": {
    "additional_sum_value": {
      "type": "number",
      "description": "Сумма баллов по дополнительным аспектам"
    },
    "advantages_sum_value": {
      "type": "number",
      "description": "Суммарное значение положительных аспектов надежности"
    },
    "disadvantages_sum_value": {
      "type": "number",
      "description": "Суммарное значение отрицательных аспектов надежности"
    },
    "has_critical": {
      "type": "boolean",
      "description": "Признак наличия критически отрицательного аспекта"
    },
    "one_day_criteria": {
      "type": "array",
      "description": "Критерии одного дня",
      "items": [
        {
          "type": "object",
          "properties": {
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            },
            "links": {
              "type": "array",
              "description": "ссылки",
              "items": [
                {
                  "type": "str"
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            }
          }
        }
      ]
    },
    "advantages": {
      "type": "object",
      "description": "Список положительных аспектов влияющих на надежность",
      "properties": {
        "common": {
          "type": "object",
          "description": "Общие признаки",
          "properties": {
            "criteria": {
              "type": "array",
              "description": "критерии",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "description": "комментарии",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "description": {
                      "type": "string",
                      "description": "Описание аспекта"
                    },
                    "links": {
                      "type": "array",
                      "description": "ссылки",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "value": {
                      "type": "number",
                      "description": "Значение аспекта"
                    }
                  }
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            },
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            }
          }
        },
        "financial": {
          "type": "object",
          "description": "Финансовые признаки",
          "properties": {
            "criteria": {
              "type": "array",
              "description": "критерии",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "description": "комментарии",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "description": {
                      "type": "string",
                      "description": "Описание аспекта"
                    },
                    "links": {
                      "type": "array",
                      "description": "ссылки",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "value": {
                      "type": "number",
                      "description": "Значение аспекта"
                    }
                  }
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            },
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            }
          }
        }
      }
    },
    "disadvantages": {
      "type": "object",
      "description": "Список отрицательных аспектов влияющих на надежность",
      "properties": {
        "common": {
          "type": "object",
          "description": "Общие признаки",
          "properties": {
            "criteria": {
              "type": "array",
              "description": "критерии",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "description": "комментарии",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "description": {
                      "type": "string",
                      "description": "Описание аспекта"
                    },
                    "links": {
                      "type": "array",
                      "description": "ссылки",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "value": {
                      "type": "number",
                      "description": "Значение аспекта"
                    }
                  }
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            },
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            }
          }
        },
        "critical": {
          "type": "object",
          "description": "Критичные признаки",
          "properties": {
            "criteria": {
              "type": "array",
              "description": "критерии",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "description": "комментарии",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "description": {
                      "type": "string",
                      "description": "Описание аспекта"
                    },
                    "links": {
                      "type": "array",
                      "description": "ссылки",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "value": {
                      "type": "number",
                      "description": "Значение аспекта"
                    }
                  }
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            },
            "description": {
              "type": "string",
              "description": "Описание аспекта"
            }
          }
        },
        "financial": {
          "type": "object",
          "description": "Финансовые признаки",
          "properties": {
            "criteria": {
              "type": "array",
              "description": "критерии",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "description": "комментарии",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "description": {
                      "type": "string",
                      "description": "Описание аспекта"
                    },
                    "links": {
                      "type": "array",
                      "description": "ссылки",
                      "items": [
                        {
                          "type": "str"
                        }
                      ]
                    },
                    "value": {
                      "type": "number",
                      "description": "Значение аспекта"
                    }
                  }
                }
              ]
            },
            "value": {
              "type": "number",
              "description": "Значение аспекта"
            },
            "description": {
              "type": "string",
              "description": "Описание аспекта"
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
  "additional_sum_value": 0,
  "advantages": {
    "common": {
      "criteria": [
        {
          "comments": [
            "Дата регистрации 01.01.18"
          ],
          "description": "5 лет компания работает на рынке",
          "links": null,
          "value": 7
        },
        {
          "comments": null,
          "description": "Более 50 филиалов в 3 регионах",
          "links": null,
          "value": 1
        },
        {
          "comments": null,
          "description": "Большой уставный капитал (350.0 тыс ₽)",
          "links": null,
          "value": 4
        },
        {
          "comments": [
            "Количество сотрудников 100 - 500 человек",
            "Годовой доход 114.7 млрд ₽",
            "Активы составляют 463.6 млрд ₽"
          ],
          "description": "Представитель крупного бизнеса",
          "links": null,
          "value": 10
        },
        {
          "comments": null,
          "description": "Имеет 4 товарных знака",
          "links": null,
          "value": 4
        },
        {
          "comments": null,
          "description": "Имеет 13 действующих лицензий и 6 действующих сертификатов",
          "links": null,
          "value": 3
        },
        {
          "comments": null,
          "description": "Является членом СРО",
          "links": null,
          "value": 2
        }
      ],
      "description": "Общие моменты",
      "value": 31
    },
    "financial": {
      "criteria": [
        {
          "comments": [
            "Оборотные активы превышают текущие долги на 211%"
          ],
          "description": "Компания способна расплатиться с текущими долгами",
          "links": null,
          "value": 2
        },
        {
          "comments": null,
          "description": "Риск задержки платежей низкий (10%)",
          "links": null,
          "value": 1
        },
        {
          "comments": null,
          "description": "Рентабельность (8.6%) выше среднеотраслевой (0%)",
          "links": null,
          "value": 3
        },
        {
          "comments": null,
          "description": "Компания владеет имуществом на сумму 547.8 млн ₽",
          "links": null,
          "value": 10
        }
      ],
      "description": "Финансовое положение",
      "value": 16
    }
  },
  "advantages_sum_value": 47,
  "disadvantages": {
    "common": {
      "criteria": [
        {
          "comments": [
            "8 (4852) 00-01-01 109 компаний"
          ],
          "description": "Телефон более чем у 100 компаний",
          "links": null,
          "value": -7
        }
      ],
      "description": "Общие моменты",
      "value": -7
    },
    "critical": {
      "criteria": [
        {
          "comments": [
            "По данным исполнительного производства №59299003/23/01020-ИП от 01.01.23"
          ],
          "description": "Деятельность компании/филиала приостановлена",
          "links": null,
          "value": -2
        },
        {
          "comments": [
            "По данным исполнительного производства №59299012/23/01020-ИП от 01.01.23"
          ],
          "description": "На имущество компании наложен арест",
          "links": null,
          "value": -0.5
        },
        {
          "comments": [
            "По данным ФНС на 01.01.23"
          ],
          "description": "Компания не сдает налоговую отчетность",
          "links": [
            "https://service.nalog.ru/zd.do"
          ],
          "value": -7
        },
        {
          "comments": [
            "По данным ФНС на 01.01.23"
          ],
          "description": "Имеется задолженность по налогам",
          "links": [
            "https://service.nalog.ru/zd.do"
          ],
          "value": 0
        },
        {
          "comments": [
            "По данным исполнительного производства №59299013/23/01020-ИП от 01.01.23"
          ],
          "description": "Имеется задолженность по з/п",
          "links": null,
          "value": -1
        },
        {
          "comments": [
            "По данным исполнительного производства №59299014/23/01020-ИП от 01.01.23"
          ],
          "description": "Имеется задолженность по кредитным платежам",
          "links": null,
          "value": -1
        },
        {
          "comments": [
            "Тестовый Ю.Т. 151 компания"
          ],
          "description": "Учредитель в 100 и более компаниях",
          "links": null,
          "value": -100
        }
      ],
      "description": "Критичные признаки",
      "value": -111.5
    },
    "financial": {
      "criteria": [
        {
          "comments": [
            "Обязательства в балансе составляют 81%: в долгосрочной перспективе возможны перебои с оплатой"
          ],
          "description": "Риск потери независимости из-за имеющихся обязательств",
          "links": null,
          "value": -1
        },
        {
          "comments": [
            "Найден риск по 1 методике из 5"
          ],
          "description": "Вероятность банкротства",
          "links": null,
          "value": 0
        },
        {
          "comments": null,
          "description": "Продажи в 2022 снизились на 56.5% по сравнению с прошлым годом",
          "links": null,
          "value": -4
        },
        {
          "comments": null,
          "description": "Отсутствует возможность получения кредита",
          "links": null,
          "value": 0
        }
      ],
      "description": "Финансовое положение",
      "value": -5
    }
  },
  "disadvantages_sum_value": -100,
  "has_critical": true,
  "one_day_criteria": [
    {
      "description": "Массовый учредитель",
      "links": null,
      "value": -100
    },
    {
      "description": "Массовый телефон",
      "links": null,
      "value": -7
    },
    {
      "description": "Компания не сдает налоговую отчетность",
      "links": null,
      "value": -7
    }
  ]
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
  }
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
      "type": "number",
      "description": "Сумма текущих займов"
    },
    "possible_loan": {
      "type": "number",
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
        "coefficient_name": {
          "type": "object",
          "description": "Ключ коэффициента",
          "properties": {
            "value": {
              "type": "number",
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
    }
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
