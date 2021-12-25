import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url1 = 'https://comptrain.co/wod/'
page = requests.get(url1, verify=False, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
daily_wod = soup.find_all('div', class_='wod-wrap mt-5')

print(daily_wod)
with open("wod.html", 'w') as f:
    f.write(str(daily_wod))


headers = {
    'authority': 'www.crossfitinvictus.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.crossfitinvictus.com/wod/december-23-2021-performance/?sub=1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_gcl_au=1.1.1976870024.1640188604; _ga=GA1.2.446025632.1640188604; _gid=GA1.2.1175021425.1640188604; _fbp=fb.1.1640188604182.2017956543; _vwo_uuid_v2=DB66FC5A04B8B1E50B12768B70A7C0857|d413bd4109e1c36020fc7524a11ed403; _tcfpup=1640188605133; ti_ukp=697bd156.5773.b844.2315.8aeac3fcc1e1; _tcafterScoket=1; WOD-performance=2; WOD-fitness=2; cookie_pop_visited=true; PHPSESSID=4a9375b1163ba64dffcc5e28fc344811; amember_nr=55a8666f6b0f53ff44534ec7d98a13e6; wordpress_logged_in_7e30870647d4eae1cba4a254cebc1ba5=pricemgp24%7C1645409485%7Crb4r55XixFiCmpZAp1UnVKVEnM7618XubcXAMX64VL3%7Cb0544eaf189373685ffd603bdeb8d85b81b83d5f75c93c5f78428c3db1b018b8; amember_ru=pricemgp24; amember_rp=5c95af3284524bab877a8eb46699ad506599e7c9; _tiupvc=["6666cd76f96956469e7be39d750cc7d9","7533a6b283dd388b9cbf1b1643223935","43d926ee587fa80fb5aba8a33747df08","01611a57630fe341bb31023c780ed90a","e3ac7ea0ca1171cdb0e71f0b8796afb4","aa7ff6af01a958adfd7dd94dea51dbfb","ec3be2a636374e378040b1d1e6c6649d","f7aa5e7d8164aa09aacfe1de7eb14da6","b168aadbce4ddbd120563403f1865128","3286476cd6fb87bb0b2c58bfe578c37c"]; WOD-isSubscribe=true; WOD-latest-url=; _tcSessInfo={"timestamp":1640227691254,"pageView":2}; _tcSecSess={"sess":"feba23344b04e37858b7c51dad5","device_type":"desktop","ip":"75.140.197.72","tcvfp":"6be823e1-3754-205c-3813-ca15a9adaf60","locale":"en_US","country":"US","city":"Sanford","region":"NC","timestamp":1640227733288}; _tisfrv=uu:bb0082e4b77664545aadde00eb7abe33|v:40|sts:1640188605140|cst:1640227733291',
}
url2 = 'https://www.crossfitinvictus.com/wod/december-23-2021-performance/'
page2 = requests.get('https://www.crossfitinvictus.com/wod/december-23-2021-performance/', headers=headers)
soup2 = BeautifulSoup(page2.content, 'html.parser')
daily_wod2 = soup2.find_all('div', class_='entry-content')
print(daily_wod2)
with open("wod2.html", 'w') as f:
     f.write(str(daily_wod2))
