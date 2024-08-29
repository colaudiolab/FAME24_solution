import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import time
from tqdm import tqdm 
proxies = {
   'http': 'http://127.0.0.1:7891',
   'https': 'http://127.0.0.1:7891',
}
# current_url = "https://en.wikipedia.org/wiki/Category:21st-century_Indian_male_actors"
# current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_male_actors&pagefrom=Bawa%2C+Samridh%0ASamridh+Bawa#mw-pages'
# current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_male_actors&pagefrom=Dev%2C+Rajan+P%0ARajan+P.+Dev#mw-pages'
# current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_male_actors&pagefrom=Jamal%2C+Assim%0AAssim+Jamal#mw-pages'
# current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_male_actors&pagefrom=Pandian%2C+Arun%0AArun+Pandian#mw-pages'
# current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_male_actors&pagefrom=Ram%2C+Sampath%0ASampath+Ram#mw-pages'
# current_url = 'https://en.wikipedia.org/wiki/Category:21st-century_Indian_actresses'
# current_url = 'https://en.wikipedia.org/wiki/Category:21st-century_Indian_women_artists'
# current_url = 'https://en.wikipedia.org/wiki/Category:21st-century_Indian_women_politicians'
# current_url = 'https://en.wikipedia.org/wiki/Category:21st-century_Indian_women_scientists'
# current_url = 'https://en.wikipedia.org/wiki/Category:21st-century_Indian_women_writers'
current_url = 'https://en.wikipedia.org/w/index.php?title=Category:21st-century_Indian_actresses&pagefrom=Singh%2C+Sadhana%0ASadhana+Singh#mw-pages'
for _ in range(100):
    
    print('current_url:', current_url)
    response = requests.get(current_url, proxies=proxies)

    
    soup = BeautifulSoup(response.text, 'html.parser')
   
    mw_pages_div = soup.find('div', id='mw-pages')
  
    li_tags = mw_pages_div.find_all('li')
  
    for li in tqdm(li_tags):
        a = li.find('a')
        if a:
         
            relative_url = a['href']

        
            full_url = 'https://en.wikipedia.org' + relative_url

          
            response = requests.get(full_url, proxies=proxies)
            soup_sub = BeautifulSoup(response.text, 'html.parser')

            
            infobox_image_td = soup_sub.find('td', {'colspan': '2', 'class': 'infobox-image'})

            if infobox_image_td:
               
                img = infobox_image_td.find('img')

                if img:
                    
                    img_url = 'https:' + img['src']

                    
                    img_name = os.path.basename(img_url)
                   
                    time.sleep(0.5)
                    urllib.request.urlretrieve(img_url, 'indian_actresses_women/'+a.text+'.png')
 
    # <a href="/w/index.php?title=Category:21st-century_Indian_male_actors&amp;pagefrom=Bawa%2C+Samridh%0ASamridh+Bawa#mw-pages" title="Category:21st-century Indian male actors">next page</a>
    next_page_a = soup.find('a', text='next page')
    # print('next_page_a:', next_page_a)
    if not next_page_a:
        break
    # else:
    current_url = 'https://en.wikipedia.org' + next_page_a['href']


    