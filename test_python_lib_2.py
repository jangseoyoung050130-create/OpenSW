import os, re, requests
from bs4 import BeautifulSoup

os.makedirs("Crawling",exist_ok=True)
news = 'https://news.daum.net/'

res = requests.get(news)
res.encoding = 'utf-8'


soup = BeautifulSoup(res.text, 'lxml')

for i in soup.find_all('div',{'class':'cont_thumb'}):
    print(i.text)


from datetime import datetime
today = datetime.now().strftime("%Y%m%d")
file_path = os.path.join("Crawling", today + ".text")

with open(file_path, "w", encoding="utf-8") as f:
    for i in soup.find_all('div',{"class":"cont_thumb"}):
        link = i.find_parent('a').get('href')

        title_tag = i.find('strong',class_ = 'tit_txt')
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)

        sub_res = requests.get(link)
        sub_res.encoding = 'utf-8'
        sub_soup = BeautifulSoup(sub_res.text,'lxml')

        content = sub_soup.find('div',{"class":"article_view"})
        if content:
            article_text = content.get_text("\n",strip=True)
        else:
            article_text = '본문 없음'
        
        f.write(title + '\n')
        f.write(link + '\n')
        f.write(article_text + '\n')
        f.write( '-----\n')

print(f"저장완료: {file_path}")