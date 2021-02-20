import requests
from bs4 import BeautifulSoup

def get_(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    li = soup.findAll("li", class_=None)
    return [l.text for l in li]


urls = [
        'https://citation.wiki/citations-amour',
        'https://citation.wiki/citations-phrase-insta',
        'https://citation.wiki/',
        'https://citation.wiki/citations-courtes/',
        'https://citation.wiki/citations-amitie/',
        'https://citation.wiki/phrases-citations-philosophiques/',
        'https://citation.wiki/citations-tristes/',
        'https://citation.wiki/citations-positives/',
        'https://citation.wiki/citations-vie/',
        'https://citation.wiki/citations-bonheur/'
        ]

with open('./db.txt','w') as f:
    for url in urls:
        lst = get_(url)
        for i,string in enumerate(lst):
            lst[i] = string.replace('\n',' ').replace('\r','')
            try:
                lst[i] = string.split(' : ')[1]
            except:
                continue
        for string in lst:
            f.write(string+'\n')
    f.close()