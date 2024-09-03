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

**Пример запроса**
```text
https://api.sbis.ru/vok/reliability?inn=7810349385
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
  "additional_sum_value": 50,
  "advantages": [
    {
      "comments": null,
      "description": "Задолженность по налогам, з/п и кредитным платежам не обнаружена",
      "links": null,
      "value": 0
    },
    {
      "comments": null,
      "description": "Компания владеет имуществом на сумму 14.0 млрд ₽",
      "links": null,
      "value": 10
    },
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
  "advantages_sum_value": 94,
  "disadvantages": [
    {
      "comments": null,
      "description": "Отсутствует свежая бухгалтерская отчетность по данным ГИР БО (ФНС)",
      "links": null,
      "value": -20
    },
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
  "disadvantages_sum_value": -21,
  "has_critical": false
}
```
