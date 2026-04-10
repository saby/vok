## Кредитоспособность:

Получить аналитические данные по кредитоспособности.

**Ограничения по лицензии**: Функционал доступен только для максимальной лицензии.

**URL** : `/creditworthiness/`

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

**Пример запроса**

```text
https://api.sbis.ru/vok/creditworthiness?inn=7712040126
```

**Пример ответа:**

```json
[
  {
    "amount_current_loans": 43930139000,
    "credit_grade": {
      "absolute_liquidity": {
        "grade": "medium",
        "significance": 5,
        "value": 16.3858207051238
      },
      "activities_profitability": {
        "grade": "low",
        "significance": 10,
        "value": 3.08007724376461
      },
      "critical_appraisal": {
        "grade": "medium",
        "significance": 15,
        "value": 3.32277690282326
      },
      "current_liquidity": {
        "grade": "medium",
        "significance": 40,
        "value": 86.7438255605093
      },
      "independence": {
        "grade": "low",
        "significance": 20,
        "value": -5.10837884334335
      },
      "sales_profitability": {
        "grade": "medium",
        "significance": 10,
        "value": 60.3210824344464
      },
      "value": "common_terms"
    },
    "possible_loan": 173839107000,
    "stop_factors": [
      {
        "key": "term_of_the_company",
        "state": "good",
        "value": 31.7
      },
      {
        "key": "equity_in_the_balance",
        "state": "bad",
        "value": -7
      },
      {
        "key": "claims_exceeding_assets",
        "state": "good",
        "value": 0
      },
      {
        "key": "claims_exceeding_revenue",
        "state": "good",
        "value": 0
      },
      {
        "key": "presence_of_loss",
        "state": "good",
        "value": 21958748000
      },
      {
        "key": "provided_false_information",
        "state": "not_check",
        "value": null
      },
      {
        "key": "hiding_real_revenue",
        "state": "not_check",
        "value": null
      },
      {
        "key": "has_overdue_debts",
        "state": "not_check",
        "value": null
      },
      {
        "key": "share_of_receivables",
        "state": "not_check",
        "value": null
      },
      {
        "key": "repeated_revision_of_loan",
        "state": "not_check",
        "value": null
      }
    ]
  }
]
```
