import requests
url = "https://ru.wikipedia.org/w/api.php"
headers =  {"user-agent":"nano catano"}
def c(par):
    a = requests.get(url,params={"format":"json",**par},headers=headers)
    return a.json()
def t(qs):
    s = c()