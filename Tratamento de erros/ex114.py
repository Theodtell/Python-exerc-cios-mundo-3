import requests

def verificando_site(url='https://pudim.com.br'):
    try:
        site = requests.get(url, timeout=5)

        if site.status_code == 200:
            print('Consegui acessar o site pudim.com.br')
    except requests.exceptions.RequestException as e:
        print('Infelizmente não consegui acessar o site pudim.com.br')
verificando_site('https://pudim.com.br')
