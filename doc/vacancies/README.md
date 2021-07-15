## Вакансии

Получить статистику по контрагенту.

**URL** : `/vacancies/stat`

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
    "active_vacancies_count": {
      "description": "Количество активных вакансий",
      "type": "integer"
    },
    "total_vacancies_count": {
      "description": "Общее количество вакансий",
      "type": "integer"
    }
  }
}
```

**Пример ответа**

```json
{
  "active_vacancies_count": 2,
  "total_vacancies_count": 9
}
```

Получить список вакансий по контрагенту.

**URL** : `/vacancies/data`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 10, максимум 100
- `page(str)` - страница запроса, по умолчанию 0
- `is_active(str)` - флаг активности вакансии, по умолчанию отдаются все

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "title": {
          "description": "Название вакансии",
          "type": "string"
        },
        "description": {
          "description": "Описание вакансии",
          "type": "string"
        },
        "salary_from": {
          "description": "Зарплата от",
          "type": "integer"
        },
        "salary_to": {
          "description": "Зарплата до",
          "type": "integer"
        },
        "salary_is_negotiable": {
          "description": "Признак договорной зарплаты",
          "type": "bool"
        },
        "experience": {
          "description": "Необходимый опыт работы",
          "type": "string"
        },
        "address": {
          "description": "Адрес",
          "type": "string"
        },
        "contact_email": {
          "description": "email для связи",
          "type": "string"
        },
        "is_active": {
          "description": "Признак активности вакансии",
          "type": "bool"
        },
        "contact_person": {
          "description": "ФИО контактного человека",
          "type": "string"
        },
        "currency": {
          "description": "валюта зарплаты",
          "type": "string"
        },
        "company_name": {
          "description": "название компании",
          "type": "string"
        },
        "contact_phone": {
          "description": "Контактные телефоны",
          "type": "array",
          "items": [
            {
              "description": "телефон",
              "type": "string"
            }
          ]
        },
        "url": {
          "description": "ссылки на источник",
          "type": "array",
          "items": [
            {
              "description": "ссылка",
              "type": "string"
            }
          ]
        },
        "kladr": {
          "description": "номера КЛАДР",
          "type": "array",
          "items": [
            {
              "description": "КЛАДР",
              "type": "string"
            }
          ]
        },
        "sources_name": {
          "description": "Названия источников",
          "type": "array",
          "items": [
            {
              "description": "название источника",
              "type": "string"
            }
          ]
        },
        "employment_data": {
          "description": "Данные о занятости",
          "type": "array",
          "items": [
            {
              "description": "Данные о занятости",
              "type": "string"
            }
          ]
        },
        "work_type_data": {
          "description": "Данные о типе работы",
          "type": "array",
          "items": [
            {
              "description": "данные о типе работы",
              "type": "string"
            }
          ]
        },
        "schedule_data": {
          "description": "Данные о расписании",
          "type": "array",
          "items": [
            {
              "description": "данные о расписании",
              "type": "string"
            }
          ]
        },
        "category_data": {
          "description": "Данные о категории работы",
          "type": "array",
          "items": [
            {
              "description": "Данные о категории работы",
              "type": "string"
            }
          ]
        },
        "kladr_data": {
          "description": "Данные о КЛАДР",
          "type": "array",
          "items": [
            {
              "description": "Данные о КЛАДР",
              "type": "string"
            }
          ]
        }
      }  
    }
  ]
}
```

**Пример ответа**

```json
[
  {
    "title": "Стропальщик 4 разряда, Ленинградская область",
    "description": "Подтвержден \n \n \n Должностные обязанности: \n \n \n Работы по погрузке-разгрузке материалов, оборудования; строповка и увязка грузов; перемещение грузов по складу и т.п. \n \n \n Требования: \n \n \n Наличие удостоверения стропальщика обязательно! Опыт работы стропальщиком от 1 года. Опыт строповки сложных децентрализованных грузов. \n Образование: \n Среднее профессиональное \n \n \n Мы предлагаем: \n \n Дополнительные бонусы: Социальный пакет \n Доставка на работу \n Дополнительное медицинское страхование \n Предоставление спец.одежды \n Столовая",
    "salary_from": 40000,
    "salary_to": 0,
    "salary_is_negotiable": false,
    "experience": "1 год",
    "address": "188459, волость Вистинская, д Вистино, р-н Кингисеппский, д. 5, ул.Школьная",
    "contact_email": null,
    "is_active": true,
    "contact_phone": [],
    "contact_person": "Захарова Наталья",
    "url": [
      "https://trudvsem.ru/vacancy/card/1074707002457/7d9654a2-44a8-11ea-af61-bf2cfe8c828d"
    ],
    "kladr": [
      "4700000000000000000"
    ],
    "currency": "руб.",
    "company_name": "Новатэк-Усть-ЛУГА, ООО",
    "sources_name": [],
    "employment_data": [
      "Временная"
    ],
    "work_type_data": [],
    "schedule_data": [
      "Полный день"
    ],
    "category_data": [
      "Автомобильный бизнес - Производство"
    ],
    "kladr_data": [
      "Ленинградская обл"
    ]
  }
]
```