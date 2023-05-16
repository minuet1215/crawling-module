import requests
import urllib3
import os
from json import JSONEncoder, JSONDecoder


import dotenv
from bs4 import BeautifulSoup


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

urllib3.disable_warnings()


def main():
    # preprocessing url
    url = os.environ['URL']
    webpage = requests.get(url, verify=False)

    # scraping
    bs = BeautifulSoup(webpage.content, "html.parser")
    datas = bs.find_all()

    # output
    print(bs.prettify())
    # print(datas)


if __name__ == '__main__':
    main()
