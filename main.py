import requests
import urllib3
import dotenv
import os

from bs4 import BeautifulSoup

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

urllib3.disable_warnings()


def main():
    url = os.environ['URL']
    webpage = requests.get(url, verify=False)
    bs = BeautifulSoup(webpage.content, "html.parser")

    datas = bs.find_all('td')
    result = []

    for data in datas:
        result.append(data)
    
    print(result)


if __name__ == '__main__':
    main()
