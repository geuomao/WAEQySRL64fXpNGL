# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re
import socks
import socket
from stem import Signal
from stem.control import Controller


def get_domain(weburls):
    domain = weburls.replace('www.', "")
    domain = domain.split(".")
    domain = domain[0]
    return domain


def check_domain_sku_status(domain):
    x = requests.get("https://signup.microsoft.com/signup?sku=Education")
    soup = BeautifulSoup(x.text, 'html.parser')
    match = soup.find('input', id='WizardState')
    while match is None:
        controller.signal(Signal.NEWNYM)
        time.sleep(10)
        x = requests.get("https://signup.microsoft.com/signup?sku=Education")
        soup = BeautifulSoup(x.text, 'html.parser')
        match = soup.find('input', id='WizardState')
        WizardState = match["value"]
    else:
        WizardState = match["value"]
    data = {
        "StepsData.Email": "fadaw@" + domain,
        "MessageId": "GenericError",
        "BackgroundImageUrl":"",
        "SkuId": "Education",
        "Origin": "",
        "IsAdminSignup": False,
        "CurrentWedcsTag": "/Signup/CollectEmail",
        "WizardState": WizardState,
        "WizardFullViewRendered": True,
        "ShowCookiesDisclosureBanner": False,
        "X-Requested-With": "XMLHttpRequest"
    }
    x = requests.post("https://signup.microsoft.com/signup/indexinternal?sku=Education", json=data)
    if 'id="sku_314c4481-f395-4525-be8b-2ec4bb1e9d91"' in x.text:
        print("The domain: " + domain + ". Can use for A1.")
        with open("domain_A1.txt", "a") as write:
            write.write(domain + "\n")
    elif 'id="sku_e82ae690-a2d5-4d76-8d30-7c6e01e6022e"' in x.text:
        print("The domain: " + domain + ". Can use for A1P.")
        with open("domain_A1P.txt", "a") as write:
            write.write(domain + "\n")
    else:
        print("The domain: " + domain + ". Can't do anything")


def get_domain_can_register(domain):
    url = "https://who.is/whois/" + domain
    x = requests.get(url)
    if "No match for" in x.text or "NOT FOUND" in x.text:
        return True
    else:
        return False


def get_google_search_result():
    global count, pages
    sub_domain = ['.com', '.net', '.org']
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    x = requests.get("https://www.google.com/search?q=site:.edu&start=" + str(pages * 10), headers=header)
    bs = BeautifulSoup(x.text, 'html.parser')
    cites = bs.find_all("cite")
    while len(cites) == 0:
        time.sleep(100)
        x = requests.get("https://www.google.com/search?q=site:.edu&start=" + str(pages * 10), headers=header)
        bs = BeautifulSoup(x.text, 'html.parser')
        cites = bs.find_all("cite")
    domains = get_domain(cites)
    for domain in domains:
        for i in range(3):
            _domain = domain + sub_domain[i]
            print(_domain)
            if get_domain_can_register(_domain):
                check_domain_sku_status(_domain)
    print("Current Done: " + str(pages + 1))
    count += 1
    pages += 1


def google_map_get():
    global count
    print("Current Page: " + str(count))
    sub_domain = ['.com', '.net', '.org']
    while True:
        url = ''
        # 上面修改成 Google Map的搜索结果网址就ojbk了
        x = requests.get(url)
        json_string = x.text.replace('/*""*/', "")
        json_string = json_string.replace('\\', "")
        matchs = re.findall(r'(https?)://(.*?)/', json_string)
        for match in matchs:
            if "google" not in match[1]:
                print(match[1])
                domain = get_domain(match[1])
                for i in range(3):
                    _domain = domain + sub_domain[i]
                    print(_domain)
                    if get_domain_can_register(_domain):
                        check_domain_sku_status(_domain)
        print("Done Page: " + str(count))
        count += 1


def run():
    google_map_get()


count = 0

controller = Controller.from_port(port=9151)
controller.authenticate()
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

run()
