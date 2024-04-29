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

**Пример запроса**

```text
https://api.sbis.ru/vok/creditworthiness?inn=7712040126
```

**Пример ответа:**

```json
{
  "amount_current_loans": 122749139000,
  "credit_grade": {
    "absolute_liquidity": {
      "grade": "high",
      "significance": 5,
      "value": 60.4161838543495
    },
    "activities_profitability": {
      "grade": "low",
      "significance": 10,
      "value": -12.0528903376293
    },
    "critical_appraisal": {
      "grade": "low",
      "significance": 15,
      "value": -18.348720442713
    },
    "current_liquidity": {
      "grade": "medium",
      "significance": 40,
      "value": 147.189347844949
    },
    "independence": {
      "grade": "low",
      "significance": 20,
      "value": 5.99343402109892
    },
    "sales_profitability": {
      "grade": "high",
      "significance": 10,
      "value": 133.872583917041
    },
    "value": "not_credited"
  },
  "possible_loan": 82389390000,
  "stop_factors": [
    {
      "key": "term_of_the_company",
      "state": "good",
      "value": 29.8
    },
    {
      "key": "equity_in_the_balance",
      "state": "bad",
      "value": 2
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
      "state": "bad",
      "value": -45639139000
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
```
