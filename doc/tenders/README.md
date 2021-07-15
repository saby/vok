## Общее о торгах:

Общая статистика по торгам контрагента

**URL** : `/tenders-info/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.

 
**Метод** : `GET`

**Формат ответа:**
```
    'customer': количество заказчиков аукциона,
    'participant': количество аукционов где ЮЛ участвовало,
```

## Торги:

Список торгов в которых участвовало ЮЛ

**URL** : `/tenders/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количетсов запрашиваемых записей
- `page (int)` - номер страницы
Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```
        'company_name' (str): нзвание ЮЛ организовавщая торг,
        'lot_name' (str): имя лота,
        'tp_type_name'  (str): имя группы торга,
        'winner_name'  (str): название победивщей ЮЛ,
        'region'  (str): регион торга,
        'tp_brief'  (str): название процедуры,
        'proc_type'  (str): тип процедуры,
        'industry' (list(str)): сферы деятельности торга,
        'amount' (float): цена торга,
        'endofferdate'  (str): дата окончания торга,
        'publishdate'  (str): дата публикации торга,
```

## Заказ торгов:

Список организованных ЮЛ торгов 

**URL** : `/customers/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количетсов запрашиваемых записей
- `page (int)` - номер страницы
Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```
            'company_name' (str): название ЮЛ заказчика,
            'region' (str): регион заказчика,
            'contact_name' (str): название руководителя заказчика
            'dir_name' (str): ФИО руководителя,
            'area' (str): сфера торга,
            'count_try' (int): общее количество участников,
            'count_win' (int): выйгранных заявок,
            'contract_count' (int): контрактов,
            'price_win' (float): сумма побед
            'win_percent' (int): процент побед,
            'contract_price' (float): цена контракта,
```

## Конкуренты:

Пересечение с конкурентами по торгам у ЮЛ

**URL** : `/rivals/`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента.
- `limit (int)` - количетсов запрашиваемых записей
- `page (int)` - номер страницы
Пример работы limit и page: номер страницы указывает интервал который нужно получить, кратный ограничению. Если limit=10, а page=0 будут получены записи с 0-ой по 9 (всего 10 штук).

Правая граница интервала ограничена 1000-ой записью.
 
**Метод** : `GET`

**Формат ответа:**

```
    'company_name' (str): название конкурента ЮЛ
    'count_try' (int): сколько было пересечений,
    'count_win' (int): сколько победил в пересекающихся торгах,
    'price_win' (int): сумма при победе,
    'region' (str): регион проведения пересекающегося торга,
    'count_all' (int): общее количество участников,
    'price_win_all' (int): общая сумма побед,
    'dir_name' (str): ФИО или название руководителя,
    'area' (str): сфера деятельности,
```