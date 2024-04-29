## СРО

Получить список вхождений в саморегулируемые организации.

**Ограничения по лицензии** :

В базовой версии лицензии: если состоит в 1, то полная информация исключая files_id, в нескольких -
название организации, даты включения/исключения, регион, деятельность. В расширенной
 лицензии доступно всё для всех организаций.

**URL** : `/sro`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента
- `limit(str)` - количество записей в запросе, по умолчанию 10, максимум 100
- `page(str)` - страница запроса, по умолчанию 0

**Метод** : `GET`

**Формат ответа**

```json
{
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "sro_name": {
          "description": "название СРО",
          "type": "string"
        },
        "region": {
          "description": "Регион",
          "type": "string"
        },
        "activity": {
          "description": "деятельность",
          "type": "string"
        },
        "date_begin": {
          "description": "дата начала деятельности",
          "type": "string"
        },
        "date_end": {
          "description": "дата окончания деятельности",
          "type": "string"
        },
        "sro_active": {
          "description": "Признак активности СРО",
          "type": "bool"
        },
        "company_in_sro": {
          "description": "Признак нахождения компании в СРО",
          "type": "bool"
        },
        "allowances_count": {
          "description": "количество пособий",
          "type": "integer"
        },
        "active_insurance_policies_count": {
          "description": "количество активных страховых полисов",
          "type": "integer"
        },
        "inactive_insurance_policies_count": {
          "description": "количество не активных страховых полисов",
          "type": "integer"
        },
        "inspection_count": {
          "description": "количество проверок",
          "type": "integer"
        },
        "active_certificates_admission_count": {
          "description": "Количество действующих сертификатов допуска",
          "type": "integer"
        },
        "inactive_certificates_admission_count": {
          "description": "Количество не действующих сертификатов допуска",
          "type": "integer"
        },
        "contributions_count": {
          "description": "Количество взносов",
          "type": "integer"
        },
        "documents_cnt": {
          "description": "Количество документов",
          "type": "integer"
        },
        "termination_reason": {
          "description": "причина прекращения деятельности",
          "type": "string"
        },
        "url": {
          "description": "ссылка на источник",
          "type": "string"
        },
        "allowances": {
          "description": "Доступы по сертификатам",
          "type": "array",
          "items": [
            {
              "description": "Доступ по сертификатам",
              "type": "string"
            }
          ]
        },
        "insurances": {
          "description": "Страховые полисы: либо максимум 5 действующих, либо 1 недействующий",
          "type": "array",
          "items": [
            {
              "description": "Страховой полис",
              "type": "object",
              "properties": {
                "date_begin": {
                  "description": "Дата начала действия",
                  "type": "string"
                },
                "date_end": {
                  "description": "Дата окончания действия",
                  "type": "string"
                },
                "name": {
                  "description": "название",
                  "type": "string"
                },
                "number": {
                  "description": "номер",
                  "type": "string"
                },
                "type": {
                  "description": "тип",
                  "type": "string"
                },
                "amount": {
                  "description": "количество",
                  "type": "number"
                },
                "insurer_name": {
                  "description": "Название страховщика",
                  "type": "string"
                },
                "license_number": {
                  "description": "Номер лицензии",
                  "type": "string"
                }
              }
            }
          ]
        },
        "inspections": {
          "description": "Проверки: максимум 2",
          "type": "array",
          "items": [
            {
              "description": "Проверка",
              "type": "object",
              "properties": {
                "date": {
                  "description": "Дата проверки",
                  "type": "string"
                },
                "type": {
                  "description": "тип",
                  "type": "string"
                },
                "result": {
                  "description": "Результат",
                  "type": "bool"
                },
                "comment": {
                  "description": "комментарий",
                  "type": "string"
                },
                "action": {
                  "description": "действие",
                  "type": "bool"
                },
                "troubleshooting": {
                  "description": "Поиск проблем",
                  "type": "string"
                }
              }
            }
          ]
        },
        "certificates": {
          "description": "Сертификаты доступа",
          "type": "array",
          "items": [
            {
              "description": "Сертификат",
              "type": "object",
              "properties": {
                "date": {
                  "description": "Дата сертификта",
                  "type": "string"
                },
                "name": {
                  "description": "название",
                  "type": "string"
                },
                "number": {
                  "description": "номер",
                  "type": "bool"
                },
                "protocol": {
                  "description": "протокол",
                  "type": "string"
                },
                "limit": {
                  "description": "ограничение",
                  "type": "object",
                  "properties": {
                    "limit_str": {
                      "description": "ограничение строкой",
                      "type": "string"
                    },
                    "sign": {
                      "description": "знак",
                      "type": "string"
                    },
                    "value": {
                      "description": "число ограничения",
                      "type": "integer"
                    }
                  }
                }
              }
            }
          ]
        },
        "rights": {
          "description": "Права члена СРО",
          "type": "array",
          "items": [
            {
              "description": "Право",
              "type": "object",
              "properties": {
                "date": {
                  "description": "Дата",
                  "type": "string"
                },
                "name": {
                  "description": "название",
                  "type": "string"
                },
                "status": {
                  "description": "Признак активности права",
                  "type": "bool"
                },
                "justification": {
                  "description": "обоснование",
                  "type": "string"
                },
                "justification_number": {
                  "description": "номер обоснования",
                  "type": "string"
                },
                "justification_date": {
                  "description": "дата обоснования",
                  "type": "string"
                },
                "subjects": {
                  "description": "предметы прав",
                  "type": "array",
                  "items": [
                    {
                      "description": "предмет",
                      "type": "object",
                      "properties": {
                        "title": {
                          "description": "Описание",
                          "type": "string"
                        },
                        "status": {
                          "description": "Признак активности",
                          "type": "bool"
                        }
                      }
                    }
                  ]
                },
                "limitations": {
                  "description": "ограничения",
                  "type": "array",
                  "items": [
                    {
                      "description": "ограничение",
                      "type": "object",
                      "properties": {
                        "title": {
                          "description": "заголовок ограничения",
                          "type": "object",
                          "properties": {
                            "name": {
                              "description": "Название",
                              "type": "string"
                            },
                            "text": {
                              "description": "текст ограничения",
                              "type": "string"
                            }
                          }
                        },
                        "status": {
                          "description": "статус",
                          "type": "object",
                          "properties": {
                            "sign": {
                              "description": "знак",
                              "type": "string"
                            },
                            "value": {
                              "description": "знак",
                              "type": "integer"
                            }
                          }
                        }
                      }
                    }
                  ]
                }
              }
            }
          ]
        },
       "files_id": {
          "description": "Идентификаторы файла",
          "type": "array",
          "items": [
            {
              "description": "Идентификатор файла",
              "type": "string"
            }
          ]
        },
        "contributions": {
          "description": "взносы",
          "type": "array",
          "items": [
            {
              "description": "взнос",
              "type": "object",
              "properties": {
                "description": {
                  "description": "описание",
                  "type": "string"
                },
                "limit": {
                  "description": "ограничение",
                  "type": "integer"
                },
                "amount": {
                  "description": "стоимость",
                  "type": "integer"
                },
                "right": {
                  "description": "право",
                  "type": "string"
                },
                "responsibility": {
                  "description": "обязательность",
                  "type": "bool"
                }
              }
            }
          ]
        }
      }  
    }
  ]
}
```


**Пример запроса**

```text
https://api.sbis.ru/vok/sro?inn=1644003838
```

**Пример ответа для базовой лицензии:**

```json
[
  [
    {
      "sro_name": "Содружество Строителей РТ, АСРО",
      "region": "Татарстан",
      "activity": "Строительство",
      "date_begin": "2009-07-03",
      "date_end": null
    },
    {
      "sro_name": "Ассоциация СРО \"ВКИ\", Ассоциация (союз)",
      "region": "Татарстан",
      "activity": "Изыскания",
      "date_begin": "2010-02-15",
      "date_end": null
    },
    {
      "sro_name": "СРО Союз \"Волга-Кама\", СО",
      "region": "Татарстан",
      "activity": "Проектирование",
      "date_begin": "2010-01-27",
      "date_end": null
    }
  ]
]
```

**Пример ответа для расширенной лицензии:**

```json
[
  {
    "date_begin": "2009-07-03",
    "date_end": null,
    "activity": "Строительство",
    "allowances_count": 0,
    "active_insurance_policies_count": 0,
    "inactive_insurance_policies_count": 0,
    "inspection_count": 8,
    "active_certificates_admission_count": 0,
    "inactive_certificates_admission_count": 0,
    "contributions_count": 2,
    "documents_cnt": 0,
    "termination_reason": null,
    "url": "http://reestr.nostroy.ru/member/4609760",
    "allowances": [],
    "insurances": [],
    "inspections": [
      {
        "date": "2018-06-10",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      },
      {
        "date": "2017-05-05",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      }
    ],
    "certificates": [],
    "rights": {
      "name": null,
      "date": null,
      "status": true,
      "justification": null,
      "justification_number": "Протокол КО №214 от 03.07.2017",
      "justification_date": null,
      "subjects": [
        {
          "title": "Объектов капитального строительства (кроме особо опасных, технически сложных и уникальных объектов, объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Особо опасных, технически сложных и уникальных объектов капитального строительства (кроме объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Объектов использования атомной энергии",
          "status": false
        }
      ],
      "limitations": [
        {
          "title": {
            "name": "Размер обязательств",
            "text": "по договорам подряда с использованием конкурентных способов заключения договоров"
          },
          "status": {
            "sign": "<",
            "value": 10000000000
          }
        },
        {
          "title": {
            "name": "Стоимость работ",
            "text": "по одному договору подряда"
          },
          "status": {
            "sign": "<",
            "value": 10000000000
          }
        }
      ]
    },
    "contributions": [
      {
        "description": "Размер взноса в компенсационный фонд возмещения вреда:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 2000000
      },
      {
        "description": "Размер взноса в компенсационный фонд обеспечения договорных обязательств:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 12714000
      }
    ],
    "company_in_sro": true,
    "sro_active": true,
    "sro_name": "Содружество Строителей РТ, АСРО",
    "region": "Татарстан",
    "files_id": []
  },
  {
    "date_begin": "2010-02-15",
    "date_end": null,
    "activity": "Изыскания",
    "allowances_count": 0,
    "active_insurance_policies_count": 0,
    "inactive_insurance_policies_count": 8,
    "inspection_count": 10,
    "active_certificates_admission_count": 0,
    "inactive_certificates_admission_count": 0,
    "contributions_count": 2,
    "documents_cnt": 0,
    "termination_reason": null,
    "url": "https://reestr.nopriz.ru/member/18879861",
    "allowances": [],
    "insurances": [
      {
        "date_begin": "2017-05-18",
        "date_end": "2017-05-19",
        "name": null,
        "number": "1578/12-0000002",
        "type": "Страхование гражданской ответственности",
        "amount": 1000000,
        "insurer_name": "АО СК \"Чулпан\" Бугульминский филиал",
        "license_number": "С 1216 16"
      }
    ],
    "inspections": [
      {
        "date": "2023-04-13",
        "type": "Плановая",
        "result": true,
        "comment": null,
        "action": false,
        "troubleshooting": null
      },
      {
        "date": "2021-10-26",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      }
    ],
    "certificates": [],
    "rights": {
      "name": null,
      "date": "2010-02-15",
      "status": true,
      "justification": null,
      "justification_number": "б/н от 15.02.2010г.",
      "justification_date": "2010-02-15",
      "subjects": [
        {
          "title": "Объектов капитального строительства (кроме особо опасных, технически сложных и уникальных объектов, объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Особо опасных, технически сложных и уникальных объектов капитального строительства (кроме объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Объектов использования атомной энергии",
          "status": false
        }
      ],
      "limitations": [
        {
          "title": {
            "name": "Размер обязательств",
            "text": "по договорам подряда с использованием конкурентных способов заключения договоров"
          },
          "status": {
            "sign": "<",
            "value": 50000000
          }
        },
        {
          "title": {
            "name": "Стоимость работ",
            "text": "по одному договору подряда"
          },
          "status": {
            "sign": "<",
            "value": 50000000
          }
        }
      ]
    },
    "contributions": [
      {
        "description": "Размер взноса в компенсационный фонд возмещения вреда:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 150000
      },
      {
        "description": "Размер взноса в компенсационный фонд обеспечения договорных обязательств:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 350000
      }
    ],
    "company_in_sro": true,
    "sro_active": true,
    "sro_name": "Ассоциация СРО \"ВКИ\", Ассоциация (союз)",
    "region": "Татарстан",
    "files_id": []
  },
  {
    "date_begin": "2010-01-27",
    "date_end": null,
    "activity": "Проектирование",
    "allowances_count": 0,
    "active_insurance_policies_count": 0,
    "inactive_insurance_policies_count": 15,
    "inspection_count": 10,
    "active_certificates_admission_count": 0,
    "inactive_certificates_admission_count": 0,
    "contributions_count": 2,
    "documents_cnt": 0,
    "termination_reason": null,
    "url": "https://reestr.nopriz.ru/member/18745746",
    "allowances": [],
    "insurances": [
      {
        "date_begin": "2016-12-24",
        "date_end": "2017-12-25",
        "name": null,
        "number": "10-16",
        "type": null,
        "amount": 16000000,
        "insurer_name": "СК \" Чулпан\", АО",
        "license_number": "С №1216 16 ФССН РФ 04.10.2006г."
      }
    ],
    "inspections": [
      {
        "date": "2023-09-04",
        "type": "Плановая",
        "result": true,
        "comment": null,
        "action": false,
        "troubleshooting": null
      },
      {
        "date": "2022-03-29",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      }
    ],
    "certificates": [],
    "rights": {
      "name": null,
      "date": "2010-01-27",
      "status": true,
      "justification": null,
      "justification_number": "Протокол Коллегии №2 от 03.11.2009г.",
      "justification_date": "2010-01-27",
      "subjects": [
        {
          "title": "Объектов капитального строительства (кроме особо опасных, технически сложных и уникальных объектов, объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Особо опасных, технически сложных и уникальных объектов капитального строительства (кроме объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Объектов использования атомной энергии",
          "status": false
        }
      ],
      "limitations": [
        {
          "title": {
            "name": "Размер обязательств",
            "text": "по договорам подряда с использованием конкурентных способов заключения договоров"
          },
          "status": {
            "sign": "<",
            "value": 50000000
          }
        },
        {
          "title": {
            "name": "Стоимость работ",
            "text": "по одному договору подряда"
          },
          "status": {
            "sign": "<",
            "value": 50000000
          }
        }
      ]
    },
    "contributions": [
      {
        "description": "Размер взноса в компенсационный фонд возмещения вреда:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 150000
      },
      {
        "description": "Размер взноса в компенсационный фонд обеспечения договорных обязательств:",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 350000
      }
    ],
    "company_in_sro": true,
    "sro_active": true,
    "sro_name": "СРО Союз \"Волга-Кама\", СО",
    "region": "Татарстан",
    "files_id": []
  }
]
```

***

Получить файл

**Ограничения по лицензии** :

Только для расширенной лицензии

**URL** : `/sro/file`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента
- `file_id` - идентификатор файла

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
file
```

**Пример запроса**

```text
https://api.sbis.ru/vok/sro/file?inn=1644003838&file_id=100500
```
