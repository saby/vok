## Реквизиты контрагента:

Получить реквизиты по контрагенту.

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
      "description": "Название статуса контрагента",
      "type": "string"
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
    "counterparty_extension_website": {
      "description": "Сайты",
      "type": "string"
    },
    "counterparty_extension_email": {
      "description": "email-ы",
      "type": "string"
    },
    "counterparty_extension_okato": {
      "description": "ОКАТО",
      "type": "string"
    },
    "counterparty_extension_telephone": {
      "description": "Телефоны",
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
    "reliability": {
      "description": "Надежность",
      "type": "float"
    },
    "cost": {
      "description": "Стоимость",
      "type": "float"
    },
    "revenue": {
      "description": "Выручка",
      "type": "integer"
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
    "creditworthiness": {
      "description": "Кредитоспособность",
      "type": "integer"
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
    }
    "total_index_positive": {
      "description": "Градусник позитивное значение",
      "type": "integer"
    },
    "total_index_negative": {
      "description": "Градусник негативное значение",
      "type": "integer"
    },
    "total_index_has_critical": {
      "description": "Наличие критических значений",
      "type": "bool"
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
    "taxation_form": {
      "description": "Форма налогообложения",
      "type": "string"
    },
    "link": {
      "description": "Сылка на карточку контрагента",
      "type": "string"
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
  "inn": "1655203331",
  "kpp": "165501001",
  "multi_kpp": null,
  "ogrn": "1101690064343",
  "okpo": "68736333",
  "company_short_name": "ООО \"АЧИР\"",
  "company_full_name": "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"АЧИР\"",
  "company_name": "Ачир, ООО",
  "condition_name": "Действующее",
  "okved": "41.2,43.12,43.2,43.3,43.99,45.2,47.52",
  "reg_number_pf": "013502025859",
  "reg_number_fss": "160167230916011",
  "registration_date": "2010-11-18",
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
  "counterparty_extension_website": null,
  "counterparty_extension_email": null,
  "counterparty_extension_okato": "92401367000",
  "counterparty_extension_telephone": null,
  "counterparty_extension_note": null,
  "address_postal": null,
  "address_actual": null,
  "address_legal": "420021, г. Казань, ул. Парижской Коммуны, д. 18",
  "number_organizations_with_same_phone": null,
  "number_organizations_with_same_legal_address": 0,
  "director_surname": "Каримов",
  "director_name": "Ильдар",
  "director_patronymic": "Раисович",
  "director_inn": "163802215790",
  "director_position": "Генеральный директор",
  "director_egrul_surname": "Каримов",
  "director_egrul_name": "Ильдар",
  "director_egrul_patronymic": "Раисович",
  "director_egrul_position": "Генеральный директор",
  "director_egrul_inn": "163802215790",
  "main_okved": "41.2",
  "main_okved_name": "Строительство жилых и нежилых зданий",
  "oktmo": "92701000001",
  "kladr": "160000010001024",
  "reliability": 81,
  "cost": 1341000,
  "revenue": 18027000,
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
  "custom_data": {},
  "activity_kind": "Строительство, ремонт и реконструкция зданий и сооружений",
  "activity_type_code": "623000000",
  "bank_name": null,
  "creditworthiness": 4423000,
  "egais": null,
  "region": "Казань",
  "brand_name": null,
  "unreliable": {
    "unreliable_addresses": false,
    "unreliability_manager": false,
    "unreliability_founder": false
  },
  "total_index_positive": 62,
  "total_index_negative": -7.9,
  "total_index_has_critical": false,
  "shareholders_registers": null,
  "reg_number_tszn": null,
  "mercury_guid": null,
  "amount_of_employees": {
    "amount_by_nalogru": 6,
    "amount_calculated_by_spp": 0,
    "amount_difference": 0,
    "amount_is_grow": true,
    "average_salary_by_nalogru": null,
    "average_salary_by_spp": null,
    "average_salary_difference": null,
    "average_salary_is_grow": null,
    "history_amount_by_nalogru": [
      {
        "count": 6,
        "difference": 0,
        "difference_percent": null,
        "is_grow": true,
        "year": 2020
      },
      {
        "count": 6,
        "difference": null,
        "difference_percent": null,
        "is_grow": true,
        "year": 2019
      }
    ],
    "history_salary_by_fns": []
  },
  "parsed_address": null,
  "taxation_form": 1,
  "directors": [
    {
      "director_position": "Генеральный директор",
      "director_surname": "Каримов",
      "director_name": "Ильдар",
      "director_patronymic": "Раисович",
      "director_inn": "163802215790"
    }
  ],
  "link": "https://test-online.sbis.ru/contractor-spp/v1/5169066",
  "address_is_mass": false,
  "director_is_mass": false,
  "spec_reg": {
    "qualified_contractors": {
      "date_begin": "2017-07-03",
      "url": "https://zakupki.gov.ru/epz/rkpo/search/results.html",
      "list": [
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        },
        {
          "decision_date": "2017-07-03",
          "publish_date": "2018-04-26",
          "start_date": "2017-07-03",
          "expiration_date": "2020-07-03",
          "type_work": "Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов",
          "registry_number": "00165520333120180000",
          "procedure_number": "PO17030100001",
          "begin_price": "60000000.00",
          "region": "Татарстан Респ"
        }
      ],
      "total_count": 46
    },
    "business_size": "2016-08-01"
  }
}
```