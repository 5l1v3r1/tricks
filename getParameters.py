import requests
from bs4 import BeautifulSoup

def getParameters(url):
    r = requests.get(url)
    cookies = r.cookies
    html = BeautifulSoup(r.text,"lxml")
    total = list()
    for form in html.find_all("form"):
        formlist = dict()
        for inputs in form.find_all("input"):
            if inputs.has_attr('name'):
                if inputs.has_attr('value'):
                    formlist[inputs['name']] = inputs['value']
                else:
                    formlist[inputs['name']] = None
        total.append(formlist)
        return total,cookies

paramters,cookies = getParameters('https://site.com.br')
