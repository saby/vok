## Реквизиты контрагента

Получить реквизиты головного контрагента.

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
      "description": "Номера оквэд",
      "type": "string"
    },
    "is_government_agency": {
      "description": "Является бюджетным ужреждением",
      "type": "bool"
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
    "legal_form": {
      "description": "Код правовой формы",
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
      "description": "Номер основного ОКВЭД",
      "type": "string"
    },
    "main_okved_name": {
      "description": "Название основного ОКВЭД",
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
    "bank_swbic": {
      "description": "Свифт банка",
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
    "authorized_capital": {
      "description": "Уставной капитал",
      "type": "float"
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
      "description": "Ссылка на карточку контрагента",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            },
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            }
          }
        },
        "black_list": {
          "description": "Организация в черном списке ЦБ РФ. Признаки нелегальной деятельности на финансовом рынке",
          "type": "object",
          "properties": {
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            },
            "signs": {
              "description": "признаки нелегальной деятельности",
              "type": "string"
            },
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "foreign_agent": {
          "description": "Иностранный агент",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_uk": {
          "description": "Присутствует в санкционных списках Великобритании",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_usa": {
          "description": "Присутствует в санкционных списках США",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_lv": {
          "description": "Присутствует в санкционных списках Латвии",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_un": {
          "description": "Присутствует в санкционных списках Организации Объединенных Наций",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_ua": {
          "description": "Присутствует в санкционных списках Украины",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_ch": {
          "description": "Присутствует в санкционных списках Швейцарии",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_eu": {
          "description": "Присутствует в санкционных списках Европейского союза",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_ca": {
          "description": "Присутствует в санкционных списках Канады",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_jp": {
          "description": "Присутствует в санкционных списках Японии",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_au": {
          "description": "Присутствует в санкционных списках Австралии",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_nz": {
          "description": "Присутствует в санкционных списках Новой Зеландии",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
            "url": {
              "description": "ссылка на источник",
              "type": "string"
            }
          }
        },
        "in_sanction_pl": {
          "description": "Присутствует в санкционных списках Польши",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
                    "base": {
                      "description": "Основание",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
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
            "actuality_date": {
              "description": "Дата сверки с источником",
              "type": "string"
            },
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


**Пример запроса**

```text
https://api.sbis.ru/vok/req?inn=7712040126
```

**Пример ответа для базовой лицензии:**

```json
{
  "inn": "7712040126",
  "kpp": "770401001",
  "multi_kpp": [
    {
      "kpp": "770435001",
      "date_end": null,
      "date_start": "2023-03-21",
      "is_default": null
    },
    {
      "kpp": "770401001",
      "date_end": null,
      "date_start": "2023-03-21",
      "is_default": null
    }
  ],
  "ogrn": "1027700092661",
  "okpo": "29063984",
  "company_short_name": "ОАО \"АЭРОФЛОТ\"",
  "company_full_name": "ОТКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО \"АЭРОФЛОТ-РОССИЙСКИЕ АВИАЛИНИИ\"",
  "company_name": "Аэрофлот, ПАО",
  "condition_code": 1,
  "okved": "51.10.1,18.12,33.16,41.20,46.14,51.21.1,51.21.3,52.29,55.10,56.10.1,58.19,62.01,62.02,62.09,64.99,68.32.2,70.22,73.20,79.11,85.22,85.42.9,86.21",
  "reg_number_pf": "087107060532",
  "reg_number_fss": "770200001477211",
  "registration_date": "1994-06-21",
  "liquidation_date": null,
  "legal_form_text": "Публичные акционерные общества",
  "entrepreneur": false,
  "entrepreneur_name": null,
  "entrepreneur_surname": null,
  "entrepreneur_patronymic": null,
  "entrepreneur_floor": null,
  "entrepreneur_citizenship": null,
  "entrepreneur_reg_number_pfip": null,
  "counterparty_extension_okfs": "48",
  "counterparty_extension_okato": "45286552000",
  "counterparty_extension_note": null,
  "address_postal": null,
  "address_actual": "119002, г. Москва, ул. Арбат, д. 10",
  "address_legal": "119019, г. Москва, вн.тер.г. муниципальный округ Арбат, ул. Арбат, д. 1",
  "legal_form": "12247",
  "number_organizations_with_same_phone": null,
  "number_organizations_with_same_legal_address": 3,
  "director_surname": "Александровский",
  "director_name": "Сергей",
  "director_patronymic": "Владимирович",
  "director_inn": "770177090572",
  "director_position": "Генеральный директор",
  "director_egrul_surname": "Александровский",
  "director_egrul_name": "Сергей",
  "director_egrul_patronymic": "Владимирович",
  "director_egrul_position": "ГЕНЕРАЛЬНЫЙ ДИРЕКТОР",
  "director_egrul_inn": "770177090572",
  "main_okved": "51.10.1",
  "main_okved_name": "Перевозка воздушным пассажирским транспортом, подчиняющимся расписанию",
  "oktmo": "45374000",
  "kladr": "770000000000758",
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
  "activity_kind": "Перевозки пассажирские",
  "activity_type_code": "3502000000",
  "bank_name": null,
  "egais": null,
  "region": "Москва",
  "status_code": null,
  "brand_name": "Аэрофлот для занятого пространства",
  "unreliable": {
    "unreliable_addresses": false,
    "unreliability_manager": false,
    "unreliability_founder": false
  },
  "shareholders_registers": null,
  "reg_number_tszn": null,
  "mercury_guid": null,
  "parsed_address": "{\"House\": \"Д. 1\", \"Region\": \"Г.МОСКВА\", \"Street\": \"УЛ АРБАТ\", \"PostalCode\": \"119019\", \"InnerCityTerr\": \"ВН.ТЕР.Г. МУНИЦИПАЛЬНЫЙ ОКРУГ АРБАТ\"}",
  "directors": [
    {
      "director_position": "ГЕНЕРАЛЬНЫЙ ДИРЕКТОР",
      "director_surname": "Александровский",
      "director_name": "Сергей",
      "director_patronymic": "Владимирович",
      "director_inn": "770177090572"
    }
  ],
  "bank_swbic": null,
  "link": "https://test-online.sbis.ru/contractor/7595b955-0960-4ec0-ab8c-42d9b90129eb",
  "status_name": null,
  "condition_name": "Действующий",
  "spec_reg": {
    "suspended_account": {
      "PDF": 44550001,
      "LastQuery": "2024-04-18"
    },
    "in_sanction_ua": {
      "date_begin": "2023-10-13",
      "date_end": "9999-12-31",
      "actuality_date": "2024-03-22",
      "url": "https://sanctions.nazk.gov.ua/ru/sanction-company/"
    }
  },
  "has_logo": true,
  "authorized_capital": 3975771215,
  "is_government_agency": false,
  "about_company": "Аэрофлот является бесспорным лидером гражданской авиации России, фактическим национальным перевозчиком.\n\nГенеральный директор авиакомпании с 10 апреля 2009 года - Виталий Савельев.\n\nАэрофлот, основанный 17 марта 1923 года, является одной из старейших авиакомпаний мира и одним из наиболее узнаваемых российских брендов.\n\nАэрофлот в 1989 году первым из российских авиакомпаний вступил в Международную ассоциацию воздушного транспорта (IATA).\n\nАэрофлот базируется в г. Москве в аэропорту «Шереметьево». \n\nВ расписании полетов «Зима 2014/2015» - собственные регулярные пассажирские рейсы в 121 пунктов 52 стран мира  (по России 41 пункт).\n\nВ России авиакомпания имеет 4 филиала: в Санкт-Петербурге,  Калининграде,  Перми и Владивостоке.\n\nПриоритетное значение придает развитию внутреннего рынка, присутствию в Сибири и на Дальнем Востоке.\n\nВ течение первых девяти месяцев 2014 года авиакомпания перевезла 17,83 млн. пассажиров – на 13,4% больше по сравнению с аналогичным периодом прошлого года, а совокупный пассажиропоток Группы компаний «Аэрофлот» составил 26,53 млн человек (+10,5%). Пассажирооборот ОАО «Аэрофлот» за девять месяцев 2014 года составил 50,73 млрд. пкм (прирост на 11,8%). Процент занятости пассажирских кресел – 79,5 %.\n\nАэрофлот постоянно увеличивает и совершенствует свой парк воздушных судов, а также построил современный аэропортовый терминал в Шереметьево. Терминал D,   вступивший в строй в конце 2009 года, предназначен для обслуживания рейсов Аэрофлота и партнёров по альянсу SkyTeam.\n\nАэрофлот располагает крупнейшим в Восточной Европе Центром управления полётами.\n\nОткрыл собственную Авиационную школу с запланированным объемом выпуска 160 пилотов (80 экипажей) в год. Подготовка кадров предусмотрена по 120 авиационным специальностям.\n\nСоздал высокотехнологичный Ситуационный центр, который в случае сбойной или кризисной  ситуации позволяет эффективно руководить производственными процессами.",
  "address_is_mass": false,
  "director_is_mass": false
}
```

**Пример ответа для расширенной лицензии:**

```json
{
  "inn": "7712040126",
  "kpp": "770401001",
  "multi_kpp": [
    {
      "kpp": "770435001",
      "date_end": null,
      "date_start": "2023-03-21",
      "is_default": null
    },
    {
      "kpp": "770401001",
      "date_end": null,
      "date_start": "2023-03-21",
      "is_default": null
    }
  ],
  "ogrn": "1027700092661",
  "okpo": "29063984",
  "company_short_name": "ОАО \"АЭРОФЛОТ\"",
  "company_full_name": "ОТКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО \"АЭРОФЛОТ-РОССИЙСКИЕ АВИАЛИНИИ\"",
  "company_name": "Аэрофлот, ПАО",
  "condition_code": 1,
  "okved": "51.10.1,18.12,33.16,41.20,46.14,51.21.1,51.21.3,52.29,55.10,56.10.1,58.19,62.01,62.02,62.09,64.99,68.32.2,70.22,73.20,79.11,85.22,85.42.9,86.21",
  "reg_number_pf": "087107060532",
  "reg_number_fss": "770200001477211",
  "registration_date": "1994-06-21",
  "liquidation_date": null,
  "legal_form_text": "Публичные акционерные общества",
  "entrepreneur": false,
  "entrepreneur_name": null,
  "entrepreneur_surname": null,
  "entrepreneur_patronymic": null,
  "entrepreneur_floor": null,
  "entrepreneur_citizenship": null,
  "entrepreneur_reg_number_pfip": null,
  "counterparty_extension_okfs": "48",
  "counterparty_extension_okato": "45286552000",
  "counterparty_extension_note": null,
  "address_postal": null,
  "address_actual": "119002, г. Москва, ул. Арбат, д. 10",
  "address_legal": "119019, г. Москва, вн.тер.г. муниципальный округ Арбат, ул. Арбат, д. 1",
  "legal_form": "12247",
  "number_organizations_with_same_phone": null,
  "number_organizations_with_same_legal_address": 3,
  "director_surname": "Александровский",
  "director_name": "Сергей",
  "director_patronymic": "Владимирович",
  "director_inn": "770177090572",
  "director_position": "Генеральный директор",
  "director_egrul_surname": "Александровский",
  "director_egrul_name": "Сергей",
  "director_egrul_patronymic": "Владимирович",
  "director_egrul_position": "ГЕНЕРАЛЬНЫЙ ДИРЕКТОР",
  "director_egrul_inn": "770177090572",
  "main_okved": "51.10.1",
  "main_okved_name": "Перевозка воздушным пассажирским транспортом, подчиняющимся расписанию",
  "oktmo": "45374000",
  "kladr": "770000000000758",
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
  "activity_kind": "Перевозки пассажирские",
  "activity_type_code": "3502000000",
  "bank_name": null,
  "egais": null,
  "region": "Москва",
  "status_code": null,
  "brand_name": "Аэрофлот для занятого пространства",
  "unreliable": {
    "unreliable_addresses": false,
    "unreliability_manager": false,
    "unreliability_founder": false
  },
  "shareholders_registers": null,
  "reg_number_tszn": null,
  "mercury_guid": null,
  "amount_of_employees": {
    "amount_by_nalogru": null,
    "amount_calculated_by_spp": 19301,
    "amount_difference": null,
    "amount_is_grow": true,
    "average_salary_by_nalogru": 133282.78,
    "average_salary_by_spp": 133282.78,
    "average_salary_difference": -51901,
    "average_salary_is_grow": false,
    "history_amount": [
      {
        "count": 19301,
        "difference": 0,
        "difference_percent": null,
        "is_grow": true,
        "source_id": 212,
        "spp": true,
        "year": 2021
      },
      {
        "count": 16192,
        "difference": 0,
        "difference_percent": null,
        "is_grow": true,
        "source_id": 212,
        "spp": true,
        "year": 2020
      },
      {
        "count": 16192,
        "difference": 0,
        "difference_percent": null,
        "is_grow": true,
        "source_id": 212,
        "spp": true,
        "year": 2018
      }
    ],
    "history_salary_by_fns": [
      {
        "count": 133282.78,
        "difference": -51901.56,
        "difference_percent": "28%",
        "is_grow": false,
        "year": 2021
      },
      {
        "count": 185184.34,
        "difference": -47262.11,
        "difference_percent": "20%",
        "is_grow": false,
        "year": 2020
      },
      {
        "count": 232446.45,
        "year": 2018
      }
    ],
    "hide_salary": true
  },
  "parsed_address": "{\"House\": \"Д. 1\", \"Region\": \"Г.МОСКВА\", \"Street\": \"УЛ АРБАТ\", \"PostalCode\": \"119019\", \"InnerCityTerr\": \"ВН.ТЕР.Г. МУНИЦИПАЛЬНЫЙ ОКРУГ АРБАТ\"}",
  "taxation_form_code": 1,
  "directors": [
    {
      "director_position": "ГЕНЕРАЛЬНЫЙ ДИРЕКТОР",
      "director_surname": "Александровский",
      "director_name": "Сергей",
      "director_patronymic": "Владимирович",
      "director_inn": "770177090572"
    }
  ],
  "bank_swbic": null,
  "link": "https://test-online.sbis.ru/contractor/7595b955-0960-4ec0-ab8c-42d9b90129eb",
  "status_name": null,
  "condition_name": "Действующий",
  "spec_reg": {
    "suspended_account": {
      "PDF": 44550001,
      "LastQuery": "2024-04-18"
    },
    "in_sanction_ua": {
      "date_begin": "2023-10-13",
      "date_end": "9999-12-31",
      "actuality_date": "2024-03-22",
      "url": "https://sanctions.nazk.gov.ua/ru/sanction-company/"
    }
  },
  "has_logo": true,
  "authorized_capital": 3975771215,
  "is_government_agency": false,
  "about_company": "Аэрофлот является бесспорным лидером гражданской авиации России, фактическим национальным перевозчиком.\n\nГенеральный директор авиакомпании с 10 апреля 2009 года - Виталий Савельев.\n\nАэрофлот, основанный 17 марта 1923 года, является одной из старейших авиакомпаний мира и одним из наиболее узнаваемых российских брендов.\n\nАэрофлот в 1989 году первым из российских авиакомпаний вступил в Международную ассоциацию воздушного транспорта (IATA).\n\nАэрофлот базируется в г. Москве в аэропорту «Шереметьево». \n\nВ расписании полетов «Зима 2014/2015» - собственные регулярные пассажирские рейсы в 121 пунктов 52 стран мира  (по России 41 пункт).\n\nВ России авиакомпания имеет 4 филиала: в Санкт-Петербурге,  Калининграде,  Перми и Владивостоке.\n\nПриоритетное значение придает развитию внутреннего рынка, присутствию в Сибири и на Дальнем Востоке.\n\nВ течение первых девяти месяцев 2014 года авиакомпания перевезла 17,83 млн. пассажиров – на 13,4% больше по сравнению с аналогичным периодом прошлого года, а совокупный пассажиропоток Группы компаний «Аэрофлот» составил 26,53 млн человек (+10,5%). Пассажирооборот ОАО «Аэрофлот» за девять месяцев 2014 года составил 50,73 млрд. пкм (прирост на 11,8%). Процент занятости пассажирских кресел – 79,5 %.\n\nАэрофлот постоянно увеличивает и совершенствует свой парк воздушных судов, а также построил современный аэропортовый терминал в Шереметьево. Терминал D,   вступивший в строй в конце 2009 года, предназначен для обслуживания рейсов Аэрофлота и партнёров по альянсу SkyTeam.\n\nАэрофлот располагает крупнейшим в Восточной Европе Центром управления полётами.\n\nОткрыл собственную Авиационную школу с запланированным объемом выпуска 160 пилотов (80 экипажей) в год. Подготовка кадров предусмотрена по 120 авиационным специальностям.\n\nСоздал высокотехнологичный Ситуационный центр, который в случае сбойной или кризисной  ситуации позволяет эффективно руководить производственными процессами.",
  "address_is_mass": false,
  "director_is_mass": false,
  "taxation_form_name": [
    "ОСНО"
  ]
}
```
