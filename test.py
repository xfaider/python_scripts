import requests
from bs4 import BeautifulSoup

def get_html(site):
    r = requests.get(site)
    return r.text

def get_page_data(html):                         #sources
    soup = BeautifulSoup(html, 'lxml')           #(format_in, parser)

    line = soup.find('table', id='theProxyList').find_all('tr')     #resolve table

    for tr in line:
        td = tr.find_all('td')
        if td == []:
            continue
        ip = td[1].text
        port = td[2].text
        country = td[3].text
        anonym = td[4].text
        types = td[5].text
        time = td[6].text

        data = {'ip': ip,
                'Port': port,
                'Country': country,
                'Anonymize': anonym,
                'Type': types,
                'Time': time}
        print(data['ip'] + ':'+ data['Port'])
        
def main():
    url = 'http://foxtools.ru/Proxy'
    get_page_data(get_html(url))

if __name__ == '__main__':
        main()
	


    ##########################
    