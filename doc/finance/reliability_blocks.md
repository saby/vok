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

**Пример запроса**
```text
https://api.sbis.ru/vok/reliability/blocks/?inn=7712040126
```

**Пример ответа для базовой лицензии:**

```json
{
  "additional_sum_value": 50,
  "advantages": [],
  "advantages_sum_value": 94,
  "disadvantages": [],
  "disadvantages_sum_value": -21,
  "has_critical": false
}
```

**Пример ответа для расширенной лицензии:**

```json
{
  "additional_sum_value": 50,
  "advantages": {
    "common": {
      "criteria": [
        {
          "comments": [
            "Дата регистрации 21.06.94"
          ],
          "description": "29 лет компания работает на рынке",
          "links": null,
          "value": 7
        },
        {
          "comments": null,
          "description": "Более 10 филиалов в 38 регионах",
          "links": null,
          "value": 1
        },
        {
          "comments": null,
          "description": "Большой уставный капитал (3975.8 млн ₽)",
          "links": null,
          "value": 4
        },
        {
          "comments": [
            "Количество сотрудников 10 000 - 50 000 человек",
            "Годовой доход 427.8 млрд ₽",
            "Активы составляют 262.9 млрд ₽"
          ],
          "description": "Представитель крупного бизнеса",
          "links": null,
          "value": 10
        },
        {
          "comments": null,
          "description": "Имеет 102 товарных знака",
          "links": null,
          "value": 4
        },
        {
          "comments": null,
          "description": "Имеет 9 действующих лицензий",
          "links": null,
          "value": 3
        },
        {
          "comments": null,
          "description": "Является членом СРО",
          "links": null,
          "value": 2
        },
        {
          "comments": null,
          "description": "Компания ищет новых сотрудников",
          "links": null,
          "value": 3
        }
      ],
      "description": "Общие моменты",
      "value": 34
    },
    "critical": {
      "criteria": [
        {
          "comments": null,
          "description": "Задолженность по налогам, з/п и кредитным платежам не обнаружена",
          "links": null,
          "value": 0
        }
      ],
      "description": "Критичные признаки",
      "value": null
    },
    "financial": {
      "criteria": [
        {
          "comments": null,
          "description": "Компания владеет имуществом на сумму 14.0 млрд ₽",
          "links": null,
          "value": 10
        }
      ],
      "description": "Финансовое положение",
      "value": 10
    }
  },
  "advantages_sum_value": 94,
  "disadvantages": {
    "critical": {
      "criteria": [
        {
          "comments": null,
          "description": "Отсутствует свежая бухгалтерская отчетность по данным ГИР БО (ФНС)",
          "links": null,
          "value": -20
        }
      ],
      "description": "Критичные признаки",
      "value": -20
    },
    "financial": {
      "criteria": [
        {
          "comments": [
            "1266.0 тыс ₽"
          ],
          "description": "Существенная сумма задолженности по исполнительным листам",
          "links": null,
          "value": -0.5
        },
        {
          "comments": [
            "93.2 млн ₽"
          ],
          "description": "Существенная сумма судебных дел, в которых компания – ответчик",
          "links": null,
          "value": -0.5
        }
      ],
      "description": "Финансовое положение",
      "value": -1
    }
  },
  "disadvantages_sum_value": -21,
  "has_critical": false,
  "one_day_criteria": []
}
```
