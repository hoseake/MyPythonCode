import requests
from bs4 import BeautifulSoup
import re
import json

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
homePage = response.content.decode()

soup = BeautifulSoup(homePage,'lxml')
script = soup.find(id='getListByCountryTypeService2true')
text = script.text
json_str = re.findall(r'\[.+\]',text)[0]

lastDay_CoronaVirus = json.loads(json_str)
print(lastDay_CoronaVirus)

with open('lastDay_CoronaVirus.json','w',encoding='utf-8') as fp:
    json.dump(lastDay_CoronaVirus,fp,ensure_ascii=False)