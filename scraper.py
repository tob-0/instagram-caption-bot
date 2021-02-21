import requests
from bs4 import BeautifulSoup


def citation_wiki_scraping():
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

    with open('.assets/src/db_citation.wiki.txt','w') as f:
        for url in urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            li = soup.findAll("li", class_=None)
            lst = [l.text for l in li]
            for i,string in enumerate(lst):
                lst[i] = string.replace('\n',' ').replace('\r','')
                try:
                    lst[i] = string.split(' : ')[1]
                except:
                    continue
            for string in lst:
                f.write(string+'\n')
        f.close()

def citationsdefilles_com_scraper():
    urls =[

    ]
def comment_economiser_fr_scraper():
    """scraper for https://www.comment-economiser.fr/85-citations-inspirantes-qui-vont-changer-votre-vie.html
    """

def les_defis_des_filles_zen_com_scraper():
    """https://les-defis-des-filles-zen.com/top-150-citation-motivation-devenir-inarretable
    """

    with open('./assets/src/db_defis-des-filles-zen.com.txt','w') as f:
        page = requests.get("https://les-defis-des-filles-zen.com/top-150-citation-motivation-devenir-inarretable")
        soup = BeautifulSoup(page.text,'html.parser')
        para = soup.findAll('p', class_=None,attrs={"style":"text-align: justify;"})
        lst = [p.text for p in para]
        for string in lst:
            if len(string)>0 and string[0] == "–":
                tmp = string.split('– « ')[1].split(' » – ')[0]
                f.write(tmp+'\n')
        f.close()
