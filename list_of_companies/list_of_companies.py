import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def get_table(address, index):
    url = "{}{}".format(address, index)

'''
    headers = {'authority': 'www.dnb.com',
    'method': 'GET',
    'path': '/business-directory/company-information.information.ca.ontario.html?page={}'.format(index),
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': 'bm_sz=660CD5E8601A356436C42EDC37841842~YAAQbA/QF9mJLe6EAQAAYKof/RKhuEGyXFGdz+VqjZFsZZE2abc2C1JavTnJe1YFaoc18EjMy/00BP8vxRk51lSIMych8kJA6BHqSID4LaWbKgj9C1AlopKc2Jn/xLJXV4/BMc0f7GCkZYyhDsvVuCma+Hx/2B6rezI4zEgBhHFtCWHbnjzBiKh1pfmxSxCPLq1NuNgHgHm7yxiF0yAhBf/gk3VffU3z9AwAU/pJ6vBid1Ou+sJcr4xTkA35hzfdZgL4ECC8az9m2cLsz98FBgyYrRr1N6nPOaM4do01xrc=~4339009~3360049; ak_bmsc=FBBCE85BC9CCFA59509A3173F40C0BAD~000000000000000000000000000000~YAAQbA/QF/KJLe6EAQAAcqsf/RIPYXAQ+C2dmgwz40ljMsSi8qe8PHGPdT38cYk+ogaohPcQTCVDx64eWP8Y8xvpVU7/G1lHsxwAaQktczNoB+fES0yH72wO/P7IkLAN2rEgMAVeC7Y7HVJy7WapsFTrUsjYwHf/AVjY+QNF83uKj71ol08ANa3aOJnGUNbnHL07m4Uadj+6eqpMmJaNHmM8bF3qnHf3SzWZd/W7kSj08sEADH383QPMP8obODvVrDC7mpol5YaT0QbRnGKM7un7dIe/2zJXct3tMG9V6U7g2bWWjJ61faa18929th4kqfvHYzQSA0AAUPEnc8lyMZxEOUWDJERK06MR5NU0Wc8KT6/fETOPkVl20rC0u5becM6rFAwLCAcFzdF2vNoILTxZR9sAX8a2nyolJ7PtB8MVF6jRsT7TksFKcevI7dX3vsVu6vDJFyNB; bm_mi=E8A59F2229447FBEFA610FE41B9B9618~YAAQbA/QF/OJLe6EAQAAcqsf/RKB3hQzXmBr1KJiOATWYqGF4tZZ0vG3AJIy5hUd4mfQ/FQdJNxK+W2IZZnNv7dp8XKz9ihMeDiwq9G/aJ5YKDaXuGlQutEMubpzEKc2D4aHW3en0qWyo6+OskXB60l9hgm1pm6Tu/zgaAu0cHmhfbicsl2m4mTr6eR+3l+RpIZOAJei8fVlp8WjaSXLIkkhW3HFLTpHObW/JUOOFOEM/gAVrsgddFAiA6XtFQCdfxfWSTDMbVqWIAgwYv41BNm4DRg2ijyRGVyXpBarjrIipO50nFNkvJQbvil/4XxrOg52DJru5ZeTojpOAut375MK2Qfj8Poou2vDFOnyJVWJisvNTxwtQYSHmGe611vHbFx4SwVkDPuIkv4D~1; bm_sv=D98C4475AB95E819C3DD43718D1955EC~YAAQbA/QF/SJLe6EAQAAcqsf/RJ77nIqLDcu5rDSJOWpwvo1xGrOeaF1VCa6Ao87uk0v46UL04adhKqA3luXcfglu06Zej1Up0z4en3LH+aD79JDnaqSkLUbr9Jq8yIF9mTsJiXbc0SONZhlR3gbEtj/GnMDqHphlk5lrVDElB+tC+KIdq0kLTi/OSl665dxlYsyG21ADn4I7h0xpLrOMLaUq90e2Y8MrpkUD3NWZkots+yizYqTmrdgmLng~1; _gcl_au=1.1.1365759335.1670694023; AMCVS_8E4767C25245B0B80A490D4C%40AdobeOrg=1; language_preference=en-us; site_preference=en-us; __exponea_etc__=1ddcc1c2-bca3-431e-8f71-9b3c0db43a9c; __exponea_time2__=-0.1385657787322998; s_nr30=1670694024250-New; _gid=GA1.2.205123087.1670694024; _uetsid=ba17394078b111ed8425a31cd743dd84; _uetvid=ba17666078b111eda2a3e3e6618f2da8; __ncuid=0034e8a7-7c21-4d7d-b89c-1a235a63ef6b; ln_or=d; _biz_sid=31083b; AMCV_8E4767C25245B0B80A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C19337%7CMCMID%7C88369281062172287614220430237042445630%7CMCAAMLH-1671298823%7C7%7CMCAAMB-1671298823%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1670701223s%7CNONE%7CMCSYNCSOP%7C411-19344%7CvVersion%7C5.2.0; _mkto_trk=id:080-UQJ-704&token:_mch-dnb.com-1670694025564-31094; _hjSessionUser_1097690=eyJpZCI6ImUwNmIxMzA5LWMyOTctNTczYS1hODg5LTgzMGViZDZlODliMSIsImNyZWF0ZWQiOjE2NzA2OTQwMjU2MzUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_1097690=eyJpZCI6IjZlMjY2NzU3LWNjODktNDczZS1hZjA2LTI2NzIyYmNhZTRhZSIsImNyZWF0ZWQiOjE2NzA2OTQwMjU2OTgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _biz_uid=17170188bbe04c39b1c202295db692bc; _biz_nA=3; _biz_flagsA=%7B%22Version%22%3A1%2C%22Ecid%22%3A%22-1650037607%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; tbw_bw_uid=bito.AABndU7G-dkAACNLL92ZAA; tbw_bw_sd=1670694026; _biz_pendingA=%5B%5D; _sp_ses.2291=*; __qca=P0-1138802520-1670694024807; s_cc=true; _st_bid=bb3439e0-78b1-11ed-9d16-e7dfd0bd539e; QSI_HistorySession=https%3A%2F%2Fwww.dnb.com%2Fbusiness-directory%2Fcompany-information.information.ca.ontario.html%3Fpage%3D1~1670694026509; s_sq=dnb-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253DCompany%252520Information%2526link%253DAccept%252520Cookies%2526region%253Donetrust-button-group%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DCompany%252520Information%2526pidt%253D1%2526oid%253DAccept%252520Cookies%2526oidt%253D3%2526ot%253DSUBMIT; _ga=GA1.2.967737606.1670694024; OptanonAlertBoxClosed=2022-12-10T17:40:35.792Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Dec+10+2022+12%3A40%3A35+GMT-0500+(Eastern+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=b1ed569c-c220-4d4b-ab70-073e9dc0675c&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; drift_campaign_refresh=846cab69-c343-4e6a-abb0-8f592a5094f1; drift_aid=c8b86c4b-0e8a-443f-8c6b-8195d50bc7c9; driftt_aid=c8b86c4b-0e8a-443f-8c6b-8195d50bc7c9; _ga_K0F9RX4KM4=GS1.1.1670694024.1.1.1670695295.0.0.0; _st_l=38.600|8662583217,8559076632,,+18559076632,0,1670696246|7927328084.2648800943.80902618931.1931427245; _st=bb3439e0-78b1-11ed-9d16-e7dfd0bd539e.bb36d1f0-78b1-11ed-9d16-e7dfd0bd539e....0....1670696246.1670704826.600.10800.30.0....1....1.10,11..dnb^com.UA-18184345-1.967737606^1670694024.38.; _abck=DFD0A9CD4324FFD82DB6FDA44C9E1DD5~-1~YAAQbA/QFwFdMO6EAQAAxXw4/QmUVqp5RA1LUyZnXGuEEGlo6mICQ2LC9orlMSxP9HCiyCSMPLhxv/De+cSwAxRKIgp8Vhn9sGeD81nf4m5jCgNMUtoF+nSMPHba4JZFCUfDML6AQIM9X1JO/8kqKoOMjNaxQYTq6GmWn1O/ZoMl7O8ZXklJVcL6cvqbm6CGp9D+7M5xwWplZq7SAaFwZ5FOIg+4MapQRUSDfHzYNx0gkER0ZsXL1GgKnP8SzKAKqYrl+JNyfzeLzG9XtdYEOD0wp96ywo/Vtfsqc45QyPEQsbDl4XK8EJ39WYtLh4qp7k637kqccPrJo1RhnZB+HO2wmAtxatmeF/iMnoCRxS5NF74cdw2+kjBNYAu1Fah9Y7C8zsjCQ5/miTOZFuszYook9nM=~0~-1~-1; _sp_id.2291=1104bd50-d1fc-468b-ad6d-457603e8bf6f.1670694026.1.1670695656.1670694026.5f181ac5-e71e-4242-91d3-0d0e181c7877',
    'referer': 'https://www.dnb.com/business-directory/company-information.information.ca.ontario.html?page=1',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

'''
    headers = {'Origin': 'https://js.driftt.com',
            'Referer': 'https://fonts.googleapis.com/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
           }

    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    print (soup)



address = "https://www.dnb.com/business-directory/company-information.information.ca.ontario.html?page="
for i in range (1, 51):
    df = get_table(address, i)