## Отчёты и подписанная выписка :

Получить бизнес справку.

**Ограничения по лицензии** :

Только в расширенной лицензии.

**URL** : `/pdf/business-report`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
PDF
```

***
Получить отчёт о должной осмотрительности.

**Ограничения по лицензии** :

Доступно в базовой лицензии.

**URL** : `/pdf/due-diligence-report`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
PDF
```

***
Получить финансовую отчётность организации

**Ограничения по лицензии** :

Доступно в базовой лицензии.

**URL** : `/pdf/financial-report`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
PDF
```

***
Получить подписаннаю выписку ЕГРЮЛ

**Ограничения по лицензии** :

Только в расширенной лицензии.

**URL** : `/pdf/signed-excerpt`

**Обязательные параметры** :
- `inn(str) or ogrn(str)` - ИНН или ОГРН контрагента

**Необязательные параметры** :
- `kpp(str)` - КПП контрагента

**Метод** : `GET`

**Формат ответа**

```json
PDF
```