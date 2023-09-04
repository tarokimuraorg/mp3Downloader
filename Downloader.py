import os
import re
import urllib.request
from bs4 import BeautifulSoup

def mp3_downloader(url : str):
        
    mp3_urls = []

    os.makedirs('downloads', exist_ok=True)

    with urllib.request.urlopen(url) as res:

        soup = BeautifulSoup(res.read(), 'html.parser')

        for elm in soup.find_all('a'):

            url = elm.get('href')
            search_obj = re.search('http[s]?://[a-zA-Z0-9\-\./]+?\.mp3$',url)
        
            if search_obj:

                mp3_url = search_obj.group()
                mp3_urls.append(mp3_url)
                print('urlを取得 : {}'.format(mp3_url))

    for mp3_url in mp3_urls:

        mp3_title = re.search('[a-zA-Z0-9\-]+?\.mp3$', mp3_url).group()
        mp3_path = 'downloads/{}'.format(mp3_title)
        urllib.request.urlretrieve(mp3_url, mp3_path)
        print('mp3を取得 : {}'.format(mp3_title))

    print('ダウンロードを完了しました。')
