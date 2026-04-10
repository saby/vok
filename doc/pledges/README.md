## Залог/Лизинг

Получить список объектов находящихся в залоге/лизинге

**Ограничения по лицензии** :

В базовой и расширенной версии лицензии: последние 3 записи исключая files_id. В расширенной
 лицензии доступно всё для всех организаций.

**URL** : `/pledges`

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
        "cost": {
          "description": "стоимость",
          "type": "number/null"
        },
        "type": {
          "description": "тип записи",
          "type": "string"
        },
        "status": {
          "description": "статус записи",
          "type": "string"
        },
        "url": {
          "description": "ссылка на источник",
          "type": "string"
        },
        "comment": {
          "description": "комментарии",
          "type": "string"
        },
        "pledgor_name": {
          "description": "название залогодателя",
          "type": "string"
        },
        "pledgee_name": {
          "description": "название залогодержателя",
          "type": "string"
        },
        "lessor_name": {
          "description": "название арендодателя",
          "type": "string"
        },
        "lessee_name": {
          "description": "название арендатора",
          "type": "string"
        },
        "category": {
          "description": "название залогодержателя",
          "type": "array",
          "items": [
            {
              "description": "название категории",
              "type": "string"
            }
          ]
        },
        "files_id": {
          "description": "идентификаторы файлов",
          "type": "array",
          "items": [
            {
              "description": "идентификатор файла",
              "type": "string"
            }
          ]
        },
        "objects": {
          "description": "объекты записи",
          "type": "array",
          "items": [
            {
              "description": "объект записи",
              "type": "object",
              "properties": {
                 "cost": {
                  "description": "стоимость",
                  "type": "number/null"
                },
                 "description": {
                  "description": "описание",
                  "type": "string"
                },
                 "category": {
                  "description": "категория",
                  "type": "string"
                }
              }
            }
          ]
        },
        "agreement": {
          "description": "соглашение",
          "type": "object",
          "properties": {
             "title": {
              "description": "заголовок",
              "type": "string"
            },
             "number": {
              "description": "номер записи",
              "type": "string"
            },
             "publish_date": {
              "description": "дата публикации",
              "type": "string"
            },
             "maturity_date": {
              "description": "дата погашения",
              "type": "string"
            }
          }
        }
      }  
    }
  ]
}
```

**Пример запроса**

```text
https://api.sbis.ru/vok/pledges?inn=7712040126
```

**Пример ответа для базовой и расширенной лицензии**

```json
[
  [
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№658 от 05.08.2025",
        "number": "658",
        "publish_date": "2025-10-02",
        "maturity_date": "2030-10-01"
      },
      "category": [
        "компьютерное оборудование, комплектующие и программное обеспечение"
      ],
      "url": "https://fedresurs.ru/sfactmessage/4F83F35E547646F793C262113CE4681F",
      "comment": "26.12.2025 - подписание Дополнительного соглашения №1 к договору лизинга №658 от 05.08.2025 - в связи со сменой лизингодателя",
      "message_number": "32996092",
      "assets": [
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        }
      ],
      "act_date": "2025-12-29",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        }
      ]
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№505 от 13.10.2023",
        "number": "505",
        "publish_date": "2024-01-18",
        "maturity_date": "2029-02-05"
      },
      "category": [
        "прочее"
      ],
      "url": "https://fedresurs.ru/sfactmessage/D33E6913C24742ABADA1BCC7E4290AB5",
      "comment": "17.01.2024 передача имущества в лизинг по Акту приема-передачи к Договору Лизинга №505 от 13.10.2023",
      "message_number": "18317388",
      "assets": [
        {
          "type": "прочее",
          "description": "Комплект серверного оборудования",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Коммутаторы ",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Типовые аппаратные серверы",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Типовые аппаратные серверы",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Системы хранения данных",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Системы хранения данных",
          "number": null,
          "type_key": 99
        }
      ],
      "act_date": "2024-01-18",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Системы хранения данных",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Системы хранения данных",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Типовые аппаратные серверы",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Типовые аппаратные серверы",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Коммутаторы ",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Прочее",
          "number": null
        }
      ]
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№221221-YA от 31.12.2021",
        "number": "221221-YA",
        "publish_date": "2022-01-12",
        "maturity_date": "2027-05-16"
      },
      "category": [
        "компьютерное оборудование, комплектующие и программное обеспечение"
      ],
      "url": "https://fedresurs.ru/sfactmessage/9F8EB1885BE4404E9C8F1FDB1F9C8793",
      "comment": null,
      "message_number": "10624724",
      "assets": [
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Программно-аппаратный комплекс Цифровой Платформы Управления Экипажами в составе: серверы, системы хранения данных, комплекты ПО.",
          "number": null,
          "type_key": 104005
        }
      ],
      "act_date": "2022-01-12",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Программно-аппаратный комплекс Цифровой Платформы Управления Экипажами в составе: серверы, системы хранения данных, комплекты ПО.",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": null
        }
      ]
    }
  ]
]
```

**Пример ответа для максимальной лицензии**
```json
[
  [
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№658 от 05.08.2025",
        "number": "658",
        "publish_date": "2025-10-02",
        "maturity_date": "2030-10-01"
      },
      "category": [
        "компьютерное оборудование, комплектующие и программное обеспечение"
      ],
      "url": "https://fedresurs.ru/sfactmessage/4F83F35E547646F793C262113CE4681F",
      "comment": "26.12.2025 - подписание Дополнительного соглашения №1 к договору лизинга №658 от 05.08.2025 - в связи со сменой лизингодателя",
      "message_number": "32996092",
      "assets": [
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        },
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Комплект серверного оборудования",
          "number": "Серверное оборудование",
          "type_key": 104005
        }
      ],
      "act_date": "2025-12-29",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": "Серверное оборудование"
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№505 от 13.10.2023",
        "number": "505",
        "publish_date": "2024-01-18",
        "maturity_date": "2029-02-05"
      },
      "category": [
        "прочее"
      ],
      "url": "https://fedresurs.ru/sfactmessage/D33E6913C24742ABADA1BCC7E4290AB5",
      "comment": "17.01.2024 передача имущества в лизинг по Акту приема-передачи к Договору Лизинга №505 от 13.10.2023",
      "message_number": "18317388",
      "assets": [
        {
          "type": "прочее",
          "description": "Комплект серверного оборудования",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Коммутаторы ",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Типовые аппаратные серверы",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Типовые аппаратные серверы",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Системы хранения данных",
          "number": null,
          "type_key": 99
        },
        {
          "type": "прочее",
          "description": "Системы хранения данных",
          "number": null,
          "type_key": 99
        }
      ],
      "act_date": "2024-01-18",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Системы хранения данных",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Системы хранения данных",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Типовые аппаратные серверы",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Типовые аппаратные серверы",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Коммутаторы ",
          "cost": 0,
          "category": "Прочее",
          "number": null
        },
        {
          "description": "Комплект серверного оборудования",
          "cost": 0,
          "category": "Прочее",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№221221-YA от 31.12.2021",
        "number": "221221-YA",
        "publish_date": "2022-01-12",
        "maturity_date": "2027-05-16"
      },
      "category": [
        "компьютерное оборудование, комплектующие и программное обеспечение"
      ],
      "url": "https://fedresurs.ru/sfactmessage/9F8EB1885BE4404E9C8F1FDB1F9C8793",
      "comment": null,
      "message_number": "10624724",
      "assets": [
        {
          "type": "компьютерное оборудование, комплектующие и программное обеспечение",
          "description": "Программно-аппаратный комплекс Цифровой Платформы Управления Экипажами в составе: серверы, системы хранения данных, комплекты ПО.",
          "number": null,
          "type_key": 104005
        }
      ],
      "act_date": "2022-01-12",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Программно-аппаратный комплекс Цифровой Платформы Управления Экипажами в составе: серверы, системы хранения данных, комплекты ПО.",
          "cost": 0,
          "category": "Компьютерное оборудование, комплектующие и программное обеспечение",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/04-19 от 30.12.2019",
        "number": "ДЛ 247/04-19",
        "publish_date": "2019-12-30",
        "maturity_date": "2031-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/B38EAA206FD94DAF9591537215D2A4BC",
      "comment": null,
      "message_number": "04639855",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2019-12-30",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/05-19 от 30.12.2019",
        "number": "ДЛ 247/05-19",
        "publish_date": "2019-12-30",
        "maturity_date": "2031-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/21FC7FB73C3148DD9F23378ECD4BD353",
      "comment": null,
      "message_number": "04639877",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2019-12-30",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/06-19 от 30.12.2019",
        "number": "ДЛ 247/06-19",
        "publish_date": "2019-12-30",
        "maturity_date": "2031-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/BDE8BA7DA00140E68390BB477CB82250",
      "comment": null,
      "message_number": "04639894",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2019-12-30",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/07-19 от 30.12.2019",
        "number": "ДЛ 247/07-19",
        "publish_date": "2019-12-30",
        "maturity_date": "2031-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/61792E657DB7420A9223395A3FEFAA85",
      "comment": null,
      "message_number": "04639903",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2019-12-30",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/08-19 от 30.12.2019",
        "number": "ДЛ 247/08-19",
        "publish_date": "2019-12-30",
        "maturity_date": "2031-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/9DDA6EB4F7434E7EBC7BE7A57FB3811B",
      "comment": null,
      "message_number": "04639916",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2019-12-30",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet100 модель RRJ-95B - 1 ед.",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Действующий",
      "agreement": {
        "title": "№ДЛ 247/02-17 от 26.07.2017",
        "number": "ДЛ 247/02-17",
        "publish_date": "2017-07-28",
        "maturity_date": "2030-07-20"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/A223249990F9B55A0FA431D94B167879",
      "comment": null,
      "message_number": "02509158",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Воздушное судно Sukhoi Superjet 100 модель RRJ-95B (20 единиц)",
          "number": "",
          "type_key": 1
        }
      ],
      "act_date": "2017-07-28",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "ВЭБ-Лизинг, АО",
      "objects": [
        {
          "description": "Воздушное судно Sukhoi Superjet 100 модель RRJ-95B (20 единиц)",
          "cost": 0,
          "category": "Материальные активы",
          "number": ""
        }
      ],
      "files_id": []
    },
    {
      "cost": null,
      "type": "В лизинге",
      "status": "Недействующий",
      "agreement": {
        "title": "№ДЛ 247/09-20 от 30.12.2020",
        "number": "ДЛ 247/09-20",
        "publish_date": "2021-01-11",
        "maturity_date": "2023-12-31"
      },
      "category": [
        "материальные активы"
      ],
      "url": "https://fedresurs.ru/sfactmessage/D90C36D2B0C14946B1161CC29DB01473",
      "comment": null,
      "message_number": "05865752",
      "assets": [
        {
          "type": "материальные активы",
          "description": "Приборы и устройства авиационные (Первоначальный склад авиационных приборов и устройств для самолетов «СухойСуперджет 100») - 10 комплектов",
          "number": null,
          "type_key": 1
        }
      ],
      "act_date": "2021-01-11",
      "lessor_name": "Аэрофлот, ПАО",
      "lessee_name": "Сведения о лизингодателе скрыты в соответствии с требованиями постановления Правительства РФ от 12.01.2018 г. №5",
      "objects": [
        {
          "description": "Приборы и устройства авиационные (Первоначальный склад авиационных приборов и устройств для самолетов «СухойСуперджет 100») - 10 комплектов",
          "cost": 0,
          "category": "Материальные активы",
          "number": null
        }
      ],
      "files_id": []
    }
  ]
]
```


***

Получить файл

**Ограничения по лицензии** :

Только для расширенной лицензии

**URL** : `/pledges/file`

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
https://api.sbis.ru/vok/pledges/file?inn=7712040126&file_id=100500
```
