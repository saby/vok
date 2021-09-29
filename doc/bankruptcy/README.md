## Данные о банкротстве контрагента:

Получить данные о банкротстве.

**URL** : `/bankruptcy`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "object",
  "properties": {
    "date": {
      "description": "Дата решения",
      "type": "string"
    },
    "status": {
      "description": "Статус решения",
      "type": "string"
    },
    "date_publication": {
      "description": "Дата публикации",
      "type": "string"
    },
    "type_decision": {
      "description": "Тип решения",
      "type": "string"
    },
    "debt_sum": {
      "description": "сумма долга",
      "type": "integer"
    },
    "manager_inn": {
      "description": "ИНН управляющего",
      "type": "string"
    },
    "publisher_data": {
      "description": "Данные издателя",
      "type": "string"
    },
    "all_creditors": {
      "description": "Все кредиторы",
      "type": "integer"
    },
    "all_chronology": {
      "description": "Вся хронология",
      "type": "integer"
    },
    "case_number": {
      "description": "номер дела",
      "type": "string"
    },
    "message_link": {
      "description": "Ссылка на сообщение",
      "type": "string"
    },
    "debtor_link": {
      "description": "Ссылка на решение",
      "type": "string"
    },
    "has_more_creditors": {
      "description": "Ещё кредиторы",
      "type": "bool"
    },
    "pre_bankrupt_message": {
      "description": "Сообщение",
      "type": "string"
    },
    "pre_bankrupt_message_header": {
      "description": "Заголовок сообщения",
      "type": "string"
    },
    "debtor_status": {
      "description": "текстовый статус",
      "type": "string"
    },
    "creditors": {
      "description": "Кредиторы",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "name": {
              "description": "Имя/Название",
              "type": "string"
            },
            "kind_activity": {
              "description": "код активности",
              "type": "string"
            },
            "sum": {
              "description": "Сумма",
              "type": "float"
            },
            "region": {
              "description": "Регион",
              "type": "string"
            },
            "head": {
              "description": "Управляющий",
              "type": "string"
            }
          }
        }
      ]
    },
    "tenders": {
      "description": "Торги",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "amount": {
              "description": "Стоимость",
              "type": "string"
            },
            "industry": {
              "description": "код активности",
              "type": "array",
              "items": {
                  "type": "string"
              }
            },
            "lot_name": {
              "description": "Название лота",
              "type": "string"
            },
            "region": {
              "description": "Регион",
              "type": "string"
            },
            "company_name": {
              "description": "Название компании",
              "type": "string"
            }
          }
        }
      ]
    }
}
```

**Пример ответа**

```json
{
  "date": "2015-08-14",
  "status": "Рассматривается в первой инстанции",
  "date_publication": null,
  "type_decision": null,
  "creditors": [
    {
      "party": 5581467,
      "region": "Москва",
      "name": "Сбербанк, ПАО",
      "head": "Греф Герман Оскарович",
      "kind_activity": "Банковские и финансовые услуги, кредит",
      "sum": 0
    }
  ],
  "tenders": [
    {
      "amount": "3693266.00",
      "region": null,
      "industry": [
        "Недвижимость",
        "Аренда и лизинг недвижимости, обмен, приватизация"
      ],
      "lot_name": "Голландский аукцион на право заключения договора аренды нежилых помещений общей площадью 427,5 кв. м, расположенных по адресу: Иркутская область, г. Иркутск, ул. Байкальская, д.8",
      "company_name": "Сбербанк, филиал"
    }
  ],
  "debt_sum": 0,
  "publisher_data": null,
  "all_creditors": 1,
  "all_chronology": 1,
  "case_number": "А46-9589/2015",
  "message_link": null,
  "pre_bankrupt_message_header": null,
  "pre_bankrupt_message": null,
  "debtor_link": "http://bankrot.fedresurs.ru/OrganizationCard.aspx?ID=None",
  "has_more_creditors": false,
  "inn": "7707083893",
  "manager_inn": "550514330813",
  "debtor_status": ""
}
```