## Реквизиты контрагента:

Получить логотип контрагента. 
Можно определить есть ли она по ключу has_logo в методе req.

**Ограничения по лицензии**:

Доступен в базовой версии лицензии

**URL** : `/logo`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
File/null
```

***

Получить информацию о регистрации контрагента.

**Ограничения по лицензии**:

Доступен в базовой версии лицензии

**URL** : `/registration-information`

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
    "pfr": {
      "description": "Информация о ПФР",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "registration_date": {
              "description": "Дата регистрации",
              "type": "string"
            },
            "name": {
              "description": "Названеи организации",
              "type": "string"
            },
            "withdrawal_date": {
              "description": "Дата снятия",
              "type": "string"
            }
          }
        }
      ]
    },
    "fss": {
      "description": "Информация о ФСС",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "registration_date": {
              "description": "Дата регистрации",
              "type": "string"
            },
            "name": {
              "description": "Названеи организации",
              "type": "string"
            },
            "withdrawal_date": {
              "description": "Дата снятия",
              "type": "string"
            }
          }
        }
      ]
    },
    "registration": {
      "description": "Информация о регистрации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "date": {
              "description": "Дата",
              "type": "string"
            },
            "name": {
              "description": "Названеи организации",
              "type": "string"
            },
            "way": {
              "description": "способо",
              "type": "string"
            }
          }
        }
      ]
    },
    "liquidation": {
      "description": "Информация о ликвидации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "date": {
              "description": "Дата",
              "type": "string"
            },
            "name": {
              "description": "Названеи организации",
              "type": "string"
            },
            "way": {
              "description": "способо",
              "type": "string"
            }
          }
        }
      ]
    },
    "accreditation": {
      "description": "Информация о аккредитации",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "accreditation_date": {
              "description": "Дата аккредитации",
              "type": "string"
            },
            "accreditation_record_number": {
              "description": "Номер записи аккредитации",
              "type": "string"
            },
            "name": {
              "description": "Названеи организации",
              "type": "string"
            },
            "termination_date": {
              "description": "Дата прекращения аккредитации",
              "type": "string"
            },
            "renewal_date": {
              "description": "Дата продления",
              "type": "string"
            }
          }
        }
      ]
    }
  }
}
```

***Пример ответа***
```json
{
  "pfr": [
    {
      "registration_date": "1992-04-13",
      "withdrawal_date": null,
      "name": "ПФР №5 по МО (Одинцовский р-н)2-5, ГУ"
    }
  ],
  "fss": [
    {
      "registration_date": "2000-02-18",
      "withdrawal_date": null,
      "name": "Филиал №29 Государственного учреждения - Московского регионального отделения Фонда социального страхования Российской Федерации"
    }
  ],
  "registration": [
    {
      "date": "2019-01-31",
      "name": "Администрация Одинцовского района Московской области ",
      "way": "Создание юридического лица до 01.07.2002"
    }
  ],
  "liquidation": [
    {
      "date": "2012-08-27",
      "name": "Межрайонная инспекция ФНС России №46 по г.Москве",
      "way": "Прекращение деятельности ЮЛ на основании п.2 ст.21.1 ФЗ от 08.08.2001 №129-ФЗ"
    }
  ],
  "accreditation": [
    {
      "name": "МИ ФНС №47 по г.Москве",
      "accreditation_record_number": "10160001214",
      "accreditation_date": "2016-09-07",
      "termination_date": null,
      "renewal_date": null
    }
  ]
}
```

***

Получить реквизиты по контрагенту.

**Ограничения по лицензии** :

В базовой версии лицензии недоступна информация о количестве работников,
средней зарплате, форме налогообложения (ключи amount_of_employees,
taxation_form_code, taxation_form_name)

**URL** : `/req`

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
    "inn": {
      "description": "ИНН",
      "type": "string"
    },
    "kpp": {
      "description": "КПП",
      "type": "string"
    },
    "multi_kpp": {
      "description": "Множественное КПП",
      "type": "array",
      "items": [
        "type": "object",
        "properties": {
          "is_default": {
            "description": "Признак дефолтного КПП",
            "type": "bool"
          },
          "kpp": {
            "description": "КПП контрагента",
            "type": "string"
          },
          "date_start": {
            "description": "Дата получения КПП",
            "type": "string"
          },
          "date_end": {
            "description": "Дата завершения КПП",
            "type": "string"
          }
        }
      ]
    },
    "ogrn": {
      "description": "ОГРН",
      "type": "string"
    },
    "okpo": {
      "description": "ОКПО",
      "type": "string"
    },
    "company_short_name": {
      "description": "Краткое название",
      "type": "string"
    },
    "condition_name": {
      "description": "Название состояния контрагента",
      "type": "string"
    },
    "condition_code": {
      "description": "Код состояния контрагента",
      "type": "integer"
    },
    "status_name": {
      "description": "Название статуса контрагента",
      "type": "string"
    },
    "status_code": {
      "description": "Код статуса контрагента",
      "type": "integer"
    },
    "okved": {
      "description": "Номера оквед",
      "type": "string"
    },
    "reg_number_pf": {
      "description": "Регистрационный номер ПФ",
      "type": "string"
    },
    "reg_number_fss": {
      "description": "Регистрационный номер ФСС",
      "type": "string"
    },
    "registration_date": {
      "description": "Дата регистрации",
      "type": "string"
    },
    "liquidation_date": {
      "description": "Дата ликвидации",
      "type": "string"
    },
    "legal_form_text": {
      "description": "Правовая форма",
      "type": "string"
    },
    "entrepreneur": {
      "description": "Признак предпринимателя",
      "type": "bool"
    },
    "entrepreneur_name": {
      "description": "Имя предпринимателя",
      "type": "string"
    },
    "entrepreneur_surname": {
      "description": "Фамилия предпринимателя",
      "type": "string"
    },
    "entrepreneur_patronymic": {
      "description": "Отчество предпринимателя",
      "type": "string"
    },
    "entrepreneur_floor": {
      "description": "Пол предпринимателя",
      "type": "string"
    },
    "entrepreneur_citizenship": {
      "description": "Гражданство предпринимателя",
      "type": "string"
    },
    "entrepreneur_reg_number_pfip": {
      "description": "Регистрационный номер ПФИП предпринимателя",
      "type": "string"
    },
    "counterparty_extension_okfs": {
      "description": "ОКФС",
      "type": "string"
    },
    "counterparty_extension_okato": {
      "description": "ОКАТО",
      "type": "string"
    },
    "counterparty_extension_note": {
      "description": "Примечание",
      "type": "string"
    },
    "address_postal": {
      "description": "Адрес почтовый",
      "type": "string"
    },
    "address_actual": {
      "description": "Адрес фактический",
      "type": "string"
    },
    "address_legal": {
      "description": "Адрес юридический",
      "type": "string"
    },
    "number_organizations_with_same_phone": {
      "description": "Количество организаций с таким же телефоном",
      "type": "integer"
    },
    "number_organizations_with_same_legal_address": {
      "description": "Количество организаций с таким же адресом юридическим",
      "type": "integer"
    },
    "director_surname": {
      "description": "Фамилия директора",
      "type": "string"
    },
    "director_name": {
      "description": "Имя директора",
      "type": "string"
    },
    "director_patronymic": {
      "description": "Отчество директора",
      "type": "string"
    },
    "director_inn": {
      "description": "ИНН директора",
      "type": "string"
    },
    "director_position": {
      "description": "Должность должности директора",
      "type": "string"
    },
    "director_egrul_surname": {
      "description": "Фамилия директора по ЕГРЮЛ",
      "type": "string"
    },
    "director_egrul_name": {
      "description": "Имя директора по ЕГРЮЛ",
      "type": "string"
    },
    "director_egrul_patronymic": {
      "description": "Отчество директора по ЕГРЮЛ",
      "type": "string"
    },
    "director_egrul_position": {
      "description": "Должность директора по ЕГРЮЛ",
      "type": "string"
    },
    "director_egrul_inn": {
      "description": "ИНН директора по ЕГРЮЛ",
      "type": "string"
    },
    "main_okved": {
      "description": "Номер основного ОКВЕД",
      "type": "string"
    },
    "main_okved_name": {
      "description": "Название основного ОКВЕД",
      "type": "string"
    },
    "oktmo": {
      "description": "ОКТМО",
      "type": "string"
    },
    "kladr": {
      "description": "КЛАДР",
      "type": "string"
    },
    "bank_reg_number": {
      "description": "Регистрационный номер банка",
      "type": "string"
    },
    "bank_correspondent_account": {
      "description": "Корреспондентский счет банка",
      "type": "string"
    },
    "bank_bic": {
      "description": "Бик банка",
      "type": "string"
    },
    "bank_bic_rcc": {
      "description": "БИК РКЦ банка",
      "type": "string"
    },
    "bank_type_name": {
      "description": "Тип банка",
      "type": "string"
    },
    "bank_rcc": {
      "description": "Тип банка",
      "type": "string"
    },
    "bank_name": {
      "description": "Название банка",
      "type": "string"
    },
    "bank_rcc_name": {
      "description": "Название расчетно кассового центра банка",
      "type": "string"
    },
    "sb": {
      "description": "Гос. орган",
      "type": "integer"
    },
    "sb_name": {
      "description": "Название госоргона",
      "type": "string"
    },
    "sb_code": {
      "description": "Код госоргона",
      "type": "string"
    },
    "sb_extra_code": {
      "description": "Дополнительный код госоргона",
      "type": "string"
    },
    "sb_type_name": {
      "description": "Название типа госоргона",
      "type": "string"
    },
    "about_company": {
      "description": "О компании",
      "type": "string"
    },
    "activity_kind": {
      "description": "Вид деятельности",
      "type": "string"
    },
    "activity_type_code": {
      "description": "Вид деятельности код",
      "type": "string"
    },
    "egais": {
      "description": "ЕГАИС",
      "type": "string"
    },
    "region": {
      "description": "Регион",
      "type": "string"
    },
    "brand_name": {
      "description": "Название бренда",
      "type": "string"
    },
    "unreliable": {
      "description": "Недостоверность",
      "type": "object",
      "properties": {
        "unreliable_addresses": {
          "description": "Недостоверность адреса",
          "type": "bool"
        },
        "unreliability_manager": {
          "description": "Недостоверность управляющего",
          "type": "bool"
        },
        "unreliability_founder": {
          "description": "Недостоверность учредителя",
          "type": "bool"
        }
      }
    },
    "shareholders_registers": {
      "description": "Набор реестров акционеров",
      "type": "????"
    },
    "reg_number_tszn": {
      "description": "Регистрационный номер центра занятости",
      "type": "string"
    },
    "mercury_guid": {
      "description": "GUID меркурия",
      "type": "string"
    },
    "parsed_address": {
      "description": "Адрес разбитый на части",
      "type": "string"
    },
    "taxation_form_code": {
      "description": "Код формы налогообложения",
      "type": "integer"
    },
    "taxation_form_name": {
      "description": "Название формы налогообложения",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "link": {
      "description": "Сылка на карточку контрагента",
      "type": "string"
    },
    "has_logo": {
      "description": "Имеет ли контрагент логотип",
      "type": "bool"
    },
    "directors": {
      "description": "Список директоров",
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "director_surname": {
              "description": "Фамилия директора",
              "type": "string"
            },
            "director_name": {
              "description": "Имя директора",
              "type": "string"
            },
            "director_patronymic": {
              "description": "Отчество директора",
              "type": "string"
            },
            "director_inn": {
              "description": "ИНН директора",
              "type": "string"
            },
            "director_position": {
              "description": "Должность должности директора",
              "type": "string"
            }
          }
        }
      ]
    },
    "amount_of_employees": {
      "description": "Количество сотрудников",
      "type": "object",
      "properties": {
        "amount_by_nalogru": {
          "description": "Сотрудников по версии nalogru",
          "type": "integer"
        },
        "amount_calculated_by_spp": {
          "description": "Сотрудников по версии sbis",
          "type": "integer"
        },
        "amount_difference": {
          "description": "Разница в сумме",
          "type": "integer"
        },
        "amount_is_grow": {
          "description": "Количество растёт",
          "type": "bool"
        },
        "average_salary_by_nalogru": {
          "description": "Средняя зп по версии nalogru",
          "type": "float"
        },
        "average_salary_by_spp": {
          "description": "Средняя зп по версии sbis",
          "type": "float"
        },
        "average_salary_difference": {
          "description": "Разница средней зп",
          "type": "float"
        },
        "average_salary_is_grow": {
          "description": "Средняя хп растёт",
          "type": "bool"
        },
        "history_amount_by_nalogru": {
          "description": "История количества сотрудников по версии nalogru",
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "count": {
                  "description": "Количество сотрудников",
                  "type": "integer"
                },
                "difference": {
                  "description": "На сколько изменилось",
                  "type": "integer"
                },
                "difference_percent": {
                  "description": "На сколько изменилось в процентах",
                  "type": "string"
                },
                "is_grow": {
                  "description": "Растет",
                  "type": "bool"
                },
                "year": {
                  "description": "Год",
                  "type": "integer"
                }
              }
          }
        ]
      },
        "history_salary_by_fns": {
          "description": "История количества сотрудников по версии fns",
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "count": {
                  "description": "Количество сотрудников",
                  "type": "integer"
                },
                "difference": {
                  "description": "На сколько изменилось",
                  "type": "integer"
                },
                "difference_percent": {
                  "description": "На сколько изменилось в процентах",
                  "type": "string"
                },
                "is_grow": {
                  "description": "Растет",
                  "type": "bool"
                },
                "year": {
                  "description": "Год",
                  "type": "integer"
                }
              }
            }
          }
        ]
      }
      }
    },
    "address_is_mass": {
      "description": "Является ли адрес юридический массовым",
      "type": "bool"
    },
    "director_is_mass": {
      "description": "Является ли директор массовым",
      "type": "bool"
    },
    "spec_reg": {
      "description": "Вхождение в специальные реестры",
      "type": "object",
      "properties": {
        "ttprf_membership": {
          "description": "Член ТТП РФ",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "terrorist_list": {
          "description": "Входит в список террористических организаций",
          "type": "object",
          "properties": {
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "unscrupulous_supplier": {
          "description": "По данным ФАС в реестре недобросовестных поставщиков",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "date_end": {
              "description": "Дата окончания",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "bribe_takers": {
          "description": "По данным Генпрокуратуры РФ привлекалась за незаконное вознаграждение от имени ЮЛ",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "court_name": {
              "description": "Наименование суда",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "entry_decision_name": {
              "description": "номер дела",
              "type": "string"
            },
            "decision_date": {
              "description": "дата дела",
              "type": "string"
            }
          }
        },
        "reliable_partners": {
          "description": "Надёжный партнёр",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "consolidated_taxpayers": {
          "description": "Консолидированная группа налогоплательщиков",
          "type": "object",
          "properties": {
            "membership_type": {
              "description": "Описание",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "business_size": {
          "description": "Когда стал субъектом малого и среднего предпринимательства",
          "type": "str"
        },
        "suspended_account": {
          "description": "Приостановлены операции по счетам",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "total_count": {
              "description": "Общее количество",
              "type": "integer"
            },
            "list": {
              "description": "Список счетов",
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "number": {
                      "description": "Последние числа счёта",
                      "type": "integer"
                    },
                    "date_begin": {
                      "description": "Когда началась блокировка",
                      "type": "string"
                    },
                    "bic": {
                      "description": "Бик банка",
                      "type": "string"
                    },
                    "bank_name": {
                      "description": "Название банка",
                      "type": "string"
                    }
                  }
                }
              ]
            }
          }
        },
        "has_mass_founders": {
          "description": "Массовые учредители среди владельцев",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "total_count": {
              "description": "Общее количество",
              "type": "integer"
            },
            "faces": {
              "description": "Список лиц",
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "name": {
                      "description": "Имя",
                      "type": "string"
                    },
                    "patronymic": {
                      "description": "Отчество",
                      "type": "string"
                    },
                    "surname": {
                      "description": "Фамилия",
                      "type": "string"
                    },
                    "share": {
                      "description": "Доля",
                      "type": "integer"
                    }
                  }
                }
              ]
            }
          }
        },
        "head_negative_involvement": {
          "description": "Руководитель отрицает причастность",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "total_count": {
              "description": "общее количество",
              "type": "integer"
            },
            "list": {
              "description": "Список руководителей",
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "full_name": {
                      "description": "Полное имя руководителя",
                      "type": "string"
                    },
                    "position": {
                      "description": "Позиция руководителя",
                      "type": "string"
                    },
                    "case_number": {
                      "description": "Номер дела",
                      "type": "string"
                    },
                    "reason": {
                      "description": "Причина",
                      "type": "string"
                    }
                  }
                }
              ] 
            }
          }
        },
        "qualified_contractors": {
          "description": "Квалифицированная подрядная организация",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "total_count": {
              "description": "общее количество",
              "type": "integer"
            },
            "list": {
              "description": "Список регионов действия",
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "region": {
                      "description": "Регион",
                      "type": "string"
                    },
                    "begin_price": {
                      "description": "Начальная стоимость",
                      "type": "string"
                    },
                    "procedure_number": {
                      "description": "Номер процедуры регистрации",
                      "type": "string"
                    },
                    "registry_number": {
                      "description": "Номер регистрации",
                      "type": "string"
                    },
                    "type_work": {
                      "description": "Тип работ",
                      "type": "string"
                    },
                    "expiration_date": {
                      "description": "Дата окончания срока",
                      "type": "string"
                    },
                    "start_date": {
                      "description": "Дата начала",
                      "type": "string"
                    },
                    "publish_date": {
                      "description": "Дата публикации",
                      "type": "string"
                    },
                    "decision_date": {
                      "description": "Дата решения",
                      "type": "string"
                    }
                  }
                }
              ] 
            }
          }
        },
        "disqualified_person": {
          "description": "Юридические лица, в состав исполнительных органов которых входят дисквалифицированные лица",
          "type": "object",
          "properties": {
            "date_begin": {
              "description": "Дата начала",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "total_count": {
              "description": "Общее количество",
              "type": "integer"
            },
            "affiliates": {
              "description": "Список дисквалифицированных",
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "full_name": {
                      "description": "Полное имя дисквалифицированного",
                      "type": "string"
                    },
                    "date_begin": {
                      "description": "Когда начало статус",
                      "type": "string"
                    },
                    "date_end": {
                      "description": "Когда конец статуса",
                      "type": "string"
                    },
                    "reason": {
                      "description": "Причина",
                      "type": "string"
                    },
                    "reason_type": {
                      "description": "тип причины",
                      "type": "string"
                    },
                    "contractor": {
                      "description": "информация по контрагенту",
                      "type": "object",
                      "properties": {
                        "company_name": {
                          "description": "название контрагента",
                          "type": "string"
                        },
                        "position": {
                          "description": "позиция в контрагенте",
                          "type": "string"
                        }
                      }
                    },
                    "official": {
                      "description": "информация об органе дисквалификации",
                      "type": "object",
                      "properties": {
                        "full_name": {
                          "description": "полное имя",
                          "type": "string"
                        },
                        "position": {
                          "description": "позиция в органе",
                          "type": "string"
                        },
                        "institutions": {
                          "description": "орган",
                          "type": "string"
                        }
                      }
                    }
                  }
                }
              ]
            }
          }
        },
        "tax_debt": {
          "description": "Имеет взыскиваемую судебными приставами задолженность более 1000 р",
          "type": "object",
          "properties": {
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "not_dend_reporting": {
          "description": "По данным ФНС не сдает отчетность более 1 года",
          "type": "object",
          "properties": {
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```

**Пример ответа**

```json
{
  "inn": "7605016030",
  "kpp": "760401001",
  "multi_kpp": [
    {
      "date_end": null,
      "date_start": "2020-05-22",
      "is_default": null,
      "kpp": "540501001"
    }
  ],
  "ogrn": "1027600787994",
  "okpo": "50946225780001",
  "company_short_name": "КОМПАНИЯ \"ТЕНЗОР\", ООО",
  "company_full_name": "Общество с ограниченной ответственностью \"Компания \"Тензор\"1",
  "company_name": "\"Компания \"Тензор\", ООО",
  "condition_code": 1,
  "condition_name": "Действующее",
  "okved": "62.01,26.20,33.12,43.21,46.51,46.66,46.69.2,47.41,47.41.4,61.10.1,61.10.4,62.02,62.09,63.11,63.11.1,68.20.2,82.30,95.11",
  "reg_number_pf": "086004004145",
  "reg_number_fss": "760501904076001",
  "registration_date": "2002-09-24",
  "liquidation_date": null,
  "legal_form_text": "Общества с ограниченной ответственностью",
  "entrepreneur": false,
  "entrepreneur_name": null,
  "entrepreneur_surname": null,
  "entrepreneur_patronymic": null,
  "entrepreneur_floor": null,
  "entrepreneur_citizenship": null,
  "entrepreneur_reg_number_pfip": null,
  "counterparty_extension_okfs": "16",
  "counterparty_extension_okato": "78401000000",
  "counterparty_extension_note": null,
  "address_postal": null,
  "address_actual": "109456, г. Москва, 1-й Вешняковский проезд, д. 1, кв. 100",
  "address_legal": "150007, г. Ярославль, Московский пр-кт, д. 12",
  "number_organizations_with_same_phone": null,
  "number_organizations_with_same_legal_address": 1,
  "director_surname": "Уваров",
  "director_name": "Сергей",
  "director_patronymic": "Васильевич",
  "director_inn": "760400948823",
  "director_position": "Директор",
  "director_egrul_surname": "Уваров",
  "director_egrul_name": "Сергей",
  "director_egrul_patronymic": "Васильевич",
  "director_egrul_position": "ДИРЕКТОР",
  "director_egrul_inn": "760400948823",
  "main_okved": "62.01",
  "main_okved_name": "Разработка компьютерного программного обеспечения",
  "oktmo": "78701000001",
  "kladr": "760000010000492",
  "bank_reg_number": null,
  "bank_correspondent_account": null,
  "bank_bic": null,
  "bank_bic_rcc": null,
  "bank_type_name": null,
  "sb": null,
  "bank_rcc": null,
  "sb_name": null,
  "bank_rcc_name": null,
  "sb_code": null,
  "sb_extra_code": null,
  "sb_type_name": null,
  "activity_kind": "Программное обеспечение",
  "activity_type_code": "2706000000",
  "bank_name": null,
  "egais": "566666666666",
  "region": "Ярославль",
  "status_code": 4,
  "brand_name": "Розничная точка продаж г.Ярославль",
  "unreliable": {
    "unreliable_addresses": false,
    "unreliability_manager": false,
    "unreliability_founder": false
  },
  "shareholders_registers": null,
  "reg_number_tszn": "123-456-789012",
  "mercury_guid": null,
  "amount_of_employees": {
    "amount_by_nalogru": 4858,
    "amount_calculated_by_spp": null,
    "amount_difference": 331,
    "amount_is_grow": true,
    "average_salary_by_nalogru": 81398.23,
    "average_salary_by_spp": null,
    "average_salary_difference": 5397,
    "average_salary_is_grow": true,
    "history_amount_by_nalogru": [
      {
        "count": 4858,
        "difference": 331,
        "difference_percent": "7%",
        "is_grow": true,
        "year": 2020
      },
      {
        "count": 4527,
        "difference": 0,
        "difference_percent": null,
        "is_grow": true,
        "year": 2019
      }
    ],
    "history_salary_by_fns": [
      {
        "count": 81398.23,
        "difference": 5397.67999999999,
        "difference_percent": "7%",
        "is_grow": true,
        "year": 2020
      },
      {
        "count": 76000.55,
        "difference": null,
        "difference_percent": null,
        "is_grow": true,
        "year": 2019
      }
    ]
  },
  "parsed_address": null,
  "taxation_form_code": 1,
  "taxation_form_name": ["ОСНО"],
  "directors": [
    {
      "director_position": "Директор",
      "director_surname": "Уваров",
      "director_name": "Сергей",
      "director_patronymic": "Васильевич",
      "director_inn": "760400948823"
    }
  ],
  "link": "https://test-online.sbis.ru/contractor/746633c5-3ada-4537-b6d2-105b97aaa680",
  "status_name": "Действующее",
  "about_company": "Компания \"Тензор\" - это крупный холдинг, занимающийся информационными технологиями.\n\n\nМы работаем во всех регионах России:\n\n\n\nФилиальная сеть - в 75 регионах\n\nПартнерская сеть - в 80 регионах, число партнеров более 600 по РФ\n\nЧисло сотрудников - около 3000 человек\n\n\n\"Тензор\" создает, активно продвигает и внедряет целый комплекс IT-решений, которым пользуются более 800 000 крупных предприятий и представителей малого бизнеса.\n\nМы выдаем и обслуживаем 40 000 сертификатов электронных подписей ежемесячно.\n\nМы организуем электронный документооборот с госорганами и компаниями по защищенным каналам связи.\n\nМы разрабатываем программное обеспечение для автоматизации управления предприятием, для бухгалтерского и налогового учета, для работы с отчетностью, для сфер торговли и общественного питания.\n\nМы оснащаем офисы \"под ключ\": поставляем сервера и компьютерную технику.\n\n\nИстория компании\n\n\n\n\n1996\n\n\n\nВремя популярности игрушек тамагочи и приставок денди. Несколько вчерашних студентов решают заняться \nпродажами компьютерной техники\n. В подвале одного из зданий г. Ярославля они открыли первый офис продаж. В ассортименте - самые современные произведения научной мысли - толстые мониторы, гигантские факсы и флоппи-дискеты.\n\n\n1998\n\n\nВ год великого российского кризиса в компанию пришли свежие люди. В то время как рубль падал, их уровень креативности зашкаливал. Они предложили разработать комплекс собственных программных продуктов для компьютеров. Так начался \nСБИС\n.\n\n\n1999\n\n\nЗа 3 года специалисты «Тензора» продали сотни компьютеров и провели десятки гарантийных ремонтов. К моменту выхода на экраны культового фильма «Матрица» компания занялась обслуживанием техники на профессиональном уровне – появился \nсервисный центр «Вирт»\n, который мгновенно начал коллекционировать авторизации.\n\n\n2000\n\n\nК концу девяностых магазин компьютерной техники значительно увеличил не только обороты, но и торговые площади. Миллениум «Тензор» и вовсе отпраздновал пополнением - появилась \nоптовая компания «Синто»\n, созданная специально для того, чтобы снабжать компьютерной техникой крупные организации.\n\n\n2001\n\n\nОдновременно с инаугурационной речью Джорджа Буша компания «Тензор» делает заявление, что знает о технической стороне продаж все. Наряду с компьютерной, компания начинает поставлять клиентам торговую технику. Так возник самостоятельный \nОтдел торгового оборудования\n.\n\n\n2004\n\n\nНа Марс высадился марсоход «Спирит», а программные продукты СБИС++ внедрились почти в каждую крупную организацию Ярославля и начали путешествие по близлежащим городам - открыт первый филиал «Тензора» в Костроме. В связи со столь бурным ростом популярности учетных управленческих систем «Тензор» запускает собственное направление финансового консалтинга - \nаудиторскую фирму «Квеста»\n.\n\n\n2005\n\n\nВ то время как футболисты ЦСКА поднимали над головами кубок УЕФА, слово «Тензор» в графе \"работодатель\" было вписано 500-му сотруднику. Специалисты по персоналу «Тензор» решили, что настал момент предложить услуги по поиску классных кадров клиентам - появилось \nкадровое агентство «Квеста»\n.\n\n\n2007\n\n\nВдохновленная тем, что чемпионами Формулы-1 стала команда Ferrari, компания «Тензор» развивает рекордную скорость: за два года охватывает сетью филиалов всю европейскую часть России, включая крупнейшие города – Санкт-Петербург, Москву и Екатеринбург. Число пользователей СБИС++ по всей стране превышает 150 000. Число сотрудников достигает 1000.\n\n\n2008\n\n\nЛето в Пекине выдалось жарким – на Олимпийских играх было разыграно 302 комплекта наград. Компания «Тензор» решает быть как можно ближе к эпицентру событий и с триумфом осваивает Восточную Сибирь. А осенью, после получения всех необходимых сертификатов, успешно стартует \nудостоверяющий центр «Тензор»\n.\n\n\n2011\n\n\nОпубликованы официальные данные Всероссийской переписи населения. По новейшим данным количество субъектов федерации в России составляет 83. В 67 из них присутствуют филиалы «Тензора». Количество абонентов системы СБИС++ приближается к отметке в миллион.\n\n\n2013\n\n\nВместе с олимпийским огнем по стране победно шествует СБИС: к сдаче отчетности подключены все субъекты РФ. Тензор возглавляет пьедестал почета по количеству клиентов. 3 миллиона электронных документов отправлены с помощью СБИС. 75 офисов продаж и 7 центров разработки – Тензор сейчас.\n\nZalgo.",
  "address_is_mass": false,
  "director_is_mass": false,
  "spec_reg": {
    "ttprf_membership": {
      "date_begin": "2021-09-08",
      "url": "https://orel.tpprf.ru/ru/member_list/?page=3&page_size=50"
    }
  },
  "has_logo": true
}
```