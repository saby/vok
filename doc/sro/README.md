## СРО

Получить список вхождений в саморегулируемые организации.

**Ограничения по лицензии** :

В базовой версии лицензи: если состоит в 1, то полная информация, в нескольких -
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
                  "type": "string"
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

**Пример ответа**

```json
[
  {
    "date_begin": "2017-06-27",
    "date_end": null,
    "activity": "Проектирование",
    "allowances_count": 0,
    "active_insurance_policies_count": 5,
    "inactive_insurance_policies_count": 0,
    "inspection_count": 2,
    "active_certificates_admission_count": 1,
    "inactive_certificates_admission_count": 0,
    "contributions_count": 2,
    "documents_cnt": 0,
    "termination_reason": "",
    "url": "https://reestr.nopriz.ru/reestr?m.ogrnip=1074707002457",
    "allowances": [
      "Работы по подготовке технологических решений",
      "Работы по подготовке технологических решений объектов нефтегазового назначения и их комплексов"
    ],
    "insurances": [
      {
        "date_begin": null,
        "date_end": null,
        "name": null,
        "number": null,
        "type": "Страхование гражданской ответственности",
        "amount": "10000000.00",
        "insurer_name": "СОГАЗ, ОАО, НАО",
        "license_number": "СИ № 1208 от 05.08.2015 г"
      },
      {
        "date_begin": null,
        "date_end": null,
        "name": null,
        "number": null,
        "type": "Страхование гражданской ответственности",
        "amount": "10000000.00",
        "insurer_name": "СОГАЗ, ОАО, НАО",
        "license_number": "СИ № 1208 от 05.08.2015 г"
      }
    ],
    "inspections": [
      {
        "date": "2019-09-24",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      },
      {
        "date": "2018-07-19",
        "type": "Плановая",
        "result": false,
        "comment": null,
        "action": false,
        "troubleshooting": null
      }
    ],
    "certificates": [
      {
        "date": "2017-06-27",
        "name": null,
        "number": "ИП-276-942",
        "protocol": "Протокол заседания Совета № П-08/2017 от 27.06.2017",
        "limit": {
          "limit_str": "не превышает двадцать пять миллионов рублей",
          "sign": "<",
          "value": 25000000
        }
      }
    ],
    "rights": {
      "name": null,
      "date": "2017-06-27",
      "status": true,
      "justification": null,
      "justification_number": "Протокол заседания Совета № П-08/2017 от 27.06.2017",
      "justification_date": "2017-06-27",
      "subjects": [
        {
          "title": "Особо опасных, технически сложных и уникальных объектов капитального строительства (кроме объектов использования атомной энергии)",
          "status": true
        },
        {
          "title": "Объектов капитального строительства (кроме особо опасных, технически сложных и уникальных объектов, объектов использования атомной энергии)",
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
          "status": {}
        },
        {
          "title": {
            "name": "Стоимость работ",
            "text": "по одному договору подряда"
          },
          "status": {
            "sign": "≥",
            "value": 300000000
          }
        }
      ]
    },
    "contributions": [
      {
        "description": "Размер взноса в компенсационный фонд возмещения вреда составляет",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 1000000
      },
      {
        "description": "Размер взноса в компенсационный фонд обеспечения договорных обязательств составляет",
        "limit": null,
        "right": null,
        "responsibility": null,
        "amount": 0
      }
    ],
    "company_in_sro": true,
    "sro_active": true,
    "region": "Москва",
    "sro_name": "Инженер-Проектировщик, НП"
  }
]
```
