import requests
from random import choice
from os.path import exists

user_agents = []


def with_proxy():
    if exists('mail.txt') and exists('proxy.txt'):
        with open('mail.txt', 'r', encoding='utf-8') as mail_file, open('proxy.txt', 'r', encoding='utf-8') as proxy_file:
            mail_lines = mail_file.readlines()
            proxy_lines = proxy_file.readlines()
            for mail, proxy in zip(mail_lines, proxy_lines):
                try:
                    session = requests.Session()
                    user_agent = {
                        'user-agent': choice(user_agents)
                    }
                    proxy_split = proxy.strip().split(':')
                    user_proxy = proxy_split[2]
                    psw_proxy = proxy_split[3]
                    proxy_ip = proxy_split[0]
                    proxy_port = proxy_split[1]
                    mail_strip = mail.strip()
                    proxy = {
                        'https': f'http://{user_proxy}:{psw_proxy}@{proxy_ip}:{proxy_port}/'
                    }
                    session.headers.update(user_agent)
                    session.proxies.update(proxy)
                    session.headers['accept'] = 'application/json'
                    session.headers['accept-encoding'] = 'gzip, deflate, br'
                    session.headers['pragma'] = 'no-cache'
                    session.headers['referer'] = 'https://kuwallet.com/'
                    session.headers['origin'] = 'https://kuwallet.com'
                    session.headers['cache-control'] = 'no-cache'

                    data = {
                        'email': mail_strip
                    }
                    r = session.post('https://wallet-baiscs.kucoin-wallet.cc/basics/v1/promotion/add/email', json=data).json()
                    if r.get('code', False) == 200:
                        print(f"[+] Успешно зарегистрирован {mail_strip}")
                    else:
                        print(r.get('msg', False))
                except Exception as ex:
                    print(ex)
    else:
        print("Создайте файл с почтами - mail.txt или с прокси - proxy.txt")
        input("Нажмите enter для выхода")


def without_proxy():
    if exists('mail.txt'):
        with open('mail.txt', 'r', encoding='utf-8') as mail_file:
            mail_lines = mail_file.readlines()
            for mail in mail_lines:
                try:
                    session = requests.Session()
                    user_agent = {
                        'user-agent': choice(user_agents)
                    }
                    mail_strip = mail.strip()
                    session.headers.update(user_agent)
                    session.headers['accept'] = 'application/json'
                    session.headers['accept-encoding'] = 'gzip, deflate, br'
                    session.headers['pragma'] = 'no-cache'
                    session.headers['referer'] = 'https://kuwallet.com/'
                    session.headers['origin'] = 'https://kuwallet.com'
                    session.headers['cache-control'] = 'no-cache'

                    data = {
                        'email': mail_strip
                    }
                    r = session.post('https://wallet-baiscs.kucoin-wallet.cc/basics/v1/promotion/add/email', json=data).json()
                    if r.get('code', False) == 200:
                        print(f"[+] Успешно зарегистрирован {mail_strip}")
                    else:
                        print(r.get('msg', False))
                except Exception as ex:
                    print(ex)
    else:
        print("Создайте файл с почтами - mail.txt")
        input("Нажмите enter для выхода")


if exists('user_agents.txt'):
    with open('user_agents.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            user_agents.append(line.strip())
    is_proxy = input("Используем прокси?? >> y/n  ")
    if is_proxy.lower() == "y":
        with_proxy()
    else:
        without_proxy()
    print("Я завершил работу!")
else:
    print("Создайте файл с юзер-агентами")
    input("Нажмите enter для выхода")

