## Надежность блоками:

Получить аналитические данные по надежности.

**Ограничения по лицензии**: В базовой лицензии показываются только итоговые суммарные значения показателей надежности без расшифровки и описания. Так же в базовой лицензии не работает параметр user_settings

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

**Пример запроса**
```text
https://api.sbis.ru/vok/reliability/blocks/?inn=7810349385
```

**Пример ответа для базовой лицензии:**

```json
{
  "additional_sum_value": 0,
  "advantages": [],
  "advantages_sum_value": 71,
  "disadvantages": [],
  "disadvantages_sum_value": -3,
  "has_critical": false
}
```

**Пример ответа для расширенной лицензии:**

```json
{
  "additional_sum_value": 0,
  "advantages": [
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Деятельность компании/филиала приостановлена",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Операции по банковским счетам приостановлены",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Компания не отвечает на требования налоговой",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Компания не сдает налоговую отчетность",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Дисквалифицированные лица в руководстве",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Перевод компании на массового руководителя",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Массовый руководитель",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Массовый учредитель",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Массовый адрес",
      "links": null,
      "value": 1
    },
    {
      "comments": null,
      "description": "Компания владеет имуществом на сумму 27.8 млн ₽",
      "links": null,
      "value": 5
    },
    {
      "comments": null,
      "description": "Чистые активы больше Уставного капитала",
      "links": [
        "755.0 млн ₽ больше 500.0 тыс ₽"
      ],
      "value": 3
    },
    {
      "comments": null,
      "description": "Продажи в 2023 выросли на 100% по сравнению с прошлым годом",
      "links": null,
      "value": 3
    },
    {
      "comments": null,
      "description": "Получена прибыль",
      "links": null,
      "value": 3
    },
    {
      "comments": [
        "Оборотные активы превышают текущие долги на 118.6%"
      ],
      "description": "Компания способна расплатиться с текущими долгами",
      "links": null,
      "value": 1
    },
    {
      "comments": null,
      "description": "Риск задержки платежей низкий (10%)",
      "links": null,
      "value": 2
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
      "comments": [
        "Максимальная сумма кредита 13.3 млрд ₽"
      ],
      "description": "Возможность получения кредита",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Дел о банкротстве не обнаружено",
      "links": null,
      "value": 5
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Существенная сумма судебных дел, в которых компания – ответчик",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Арест имущества не обнаружен",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Не найдены решения об обращении взыскания на заложенное имущество",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Отсутствие задолженности по налогам",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Отсутствие задолженности по заработной плате",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Отсутствие задолженности при обслуживании кредита",
      "links": null,
      "value": 2
    },
    {
      "comments": null,
      "description": "Дел о банкротстве аффилированных компаний не обнаружено",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Миграция между налоговыми органами",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Частая смена руководителя",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Дата регистрации 24.04.15"
      ],
      "description": "9 лет компания работает на рынке",
      "links": null,
      "value": 3
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Массовый телефон",
      "links": null,
      "value": 1
    },
    {
      "comments": null,
      "description": "Большой уставный капитал (500.0 тыс ₽)",
      "links": null,
      "value": 7
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Недобросовестный поставщик",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Нет признаков оплаты труда",
      "links": null,
      "value": 1
    },
    {
      "comments": [
        "Признак отсутствует"
      ],
      "description": "Нет сотрудников",
      "links": null,
      "value": 1
    }
  ],
  "advantages_sum_value": 71,
  "disadvantages": [
    {
      "comments": null,
      "description": "Рентабельность (-0.3%) ниже среднеотраслевой (10.1%)",
      "links": null,
      "value": -2
    },
    {
      "comments": [
        "Обязательства в балансе составляют 88.1%: в долгосрочной перспективе возможны перебои с оплатой"
      ],
      "description": "Риск потери независимости из-за имеющихся обязательств",
      "links": null,
      "value": -1
    }
  ],
  "disadvantages_sum_value": -3,
  "has_critical": false
}
```
