## Контактные данные контрагента:

Получить контактные данные.  
Без лицензии на АПИ контрагентов контакты не будут возвращены.  
При наличии лицензии иписок возвращаемых источников зависит от тарифа.

Для расширенного:  
    Все источники

Для базового:  
    

**URL** : `/contacts-official`

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
    "phone_numbers": {
      "description": "Телефонные номера",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "sites": {
      "description": "Сайты",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "emails": {
      "description": "Адреса электронной почты",
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    }
  }
}
```

**Пример ответа**

```json
{
   "phone_numbers": [
      "74952584601",
      "74957757822",
      "78002007799",
      "74957772424", 
      "74957755454",
      "74957397739", 
      "73027831515"
   ],
   "sites": [
      "vtb.ru",
      "wecare.vtb.ru",
      "vtbstrana.ru", 
      "vtbrussia.ru", 
      "vtbglobalperspectives.com",
      "vtbcareer.com", 
      "vtb24.ru",
      "vitrina.vtb.ru",
      "start.vtb.ru",
      "startup.vtb.ru",
      "school.vtb.ru", 
      "qr.vtb.ru",
      "private.vtb.ru",
      "osago.vtb.ru",
      "onlinebroker.ru", 
      "olb.ru", 
      "lk.vtb.ru",
      "lkbo.vtb.ru",
      "ligabisnesa.vtb.ru",
      "kdelu.vtb.ru", 
      "ipoteka-online.vtb.ru",
      "gallery360.vtb.ru", 
      "digital.vtb.ru",
      "delo.vtb.ru", 
      "cifra.vtb.ru", 
      "cbvtb24back.vtb24.ru", 
      "business.vtb.ru",
      "broker.vtb.ru", 
      "brand.vtb.ru", 
      "auth.lk.vtb.ru",
      "ankety.vtb.ru", 
      "anketa.vtb.ru", 
      "acquiring.vtb.ru",
      "accr.vtb.ru"
   ], 
   "emails": [
      "zhuravlevas2@nwr.vtb.ru",
      "zakupki@msk.vtb.ru",
      "chellukinaes@chel.vtb24.ru",
      "zakupki@vtb.ru",
      "zakupki@kha.vtb.ru", 
      "yrssey1@yrs.vtb.ru", 
      "yatskoed@vtb-sz.ru", 
      "yatskoed@nwr.vtb.ru",
      "voronkinaam@vtb.ru", 
      "vorobevaee@vtb-sz.ru", 
      "volovik.k@vtb.ru",
      "vk.cvetkov@tensor.ru",
      "valentin.kravchenko@msk.vtb.ru",
      "urban@vtb.ru", 
      "ulykov@ul.vtb.ru",
      "tve37647@tve.vtb.ru",
      "turkhanar@kazan.vtb24.ru",
      "tsvetkovatu@vtb.ru",
      "tsvetkovatu@nwr.vtb.ru",
      "tischenkons@ektb.vtb24.ru",
      "sta47308@sta.vtb.ru", 
      "spemav@spe.vtb.ru", 
      "shvetsov@eka.vtb.ru", 
      "shvetsea@irkutsk.vtb24.ru", 
      "sergeevdv@msk.vtb.ru", 
      "semenkodv@szrc.vtb.ru",
      "say@vtb.ru", 
      "samorukovana@altai.vtb24.ru",
      "rodionov@vtb.ru",
      "ppetrova@vtb.ru", 
      "poponina@msk.vtb.ru",
      "o.vechkasov@pen.vtb.ru",
      "ovchinnikovaea@corp.vtb.ru",
      "okozlova@msk.vtb.ru", 
      "novikovmg@msk.vtb.ru", 
      "nechaevani@vrn.vtb.ru", 
      "mvgutsa@vtb.ru", 
      "menshikova@msk.vtb.ru",
      "mashkova.mi@nsk.vtb24.ru",
      "malitsina@vtb.ru", 
      "lchernova@vtb.ru", 
      "kulinichrp@msk.vtb.ru", 
      "kulikovae@vtb.ru", 
      "kra@vtb.ru", 
      "kra30868@kravtb.vtb.ru",
      "kkomleva@vtb.ru",
      "khizuntp@tmn.vtb24.ru",
      "kha45217@ppk.vtb.ru",
      "kdrnrk@kdr.vtb.ru", 
      "job@vtbdc.ru",
      "j55@msk.vtb.ru",
      "hr@kemerovo.vtb24.ru",
      "gorokhova@msk.vtb.ru", 
      "furmanml@nsk.vtb.ru",
      "ermakov-in@kha.vtb.ru", 
      "egorova_sa@vtb.ru",
      "ebelikova@msk.vtb.ru",
      "drozdovag@vtb-sz.ru",
      "doshicin@msk.vtb.ru", 
      "dennis.urban@msk.vtb.ru",
      "davletgildeeva@kaz.vtb.ru",
      "dariya.pimenova@msk.vtb.ru",
      "chikvv2@chita.vtb.ru", 
      "cherkasovapv@msk.vtb.ru",
      "brovun@vtb.ru",
      "bogdanovavia@spb.vtb24.ru",
      "belkvm@bel.vtb.ru",
      "belkea@bel.vtb.ru",
      "baushevara@vtb.ru",
      "aleshin.ruslan@bryansk.vtb.ru",
      "aasorokin@vtb.ru"
   ]
}
```