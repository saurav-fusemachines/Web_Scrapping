import requests
from bs4 import BeautifulSoup
import json

def extract(page):
    job = "Data Engineer"
    location = "United States"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    url = f'https://www.simplyhired.com/search?q={job}&l={location}'
    r = requests.get(url, headers=headers)
    # print(r.json())
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def transform(soup):
    arr = []
    ul = soup.find_all('ul', id='job-list')
    jobs = ul[0].find_all('li')
    # print(len(jobs))

    for item in jobs:
        title = item.find('a', class_='chakra-button').text.strip()
        company = item.find('span', class_='css-lvyu5j').text.strip()
        location = item.find('span', class_='css-1t92pv').text.strip()
        salary = item.find('div', class_='css-1b6seq1').text.strip()
        qualification = item.find('span',class_='css-4ltz5z')
        job_anchor = item.a.get('href')
        summary = item.find('p', class_='chakra-text css-jhqp7z').text.strip()
        print(item.a.text)


        # job = {'title': title, 'company': company, 'location': location, 'salary': salary, 'summary': summary}
        job = {'title':title,'company':company,'location':location,'salary':salary,'qualification':qualification,'summary':summary,'job_anchor':job_anchor}
        arr.append(job)
        

    return arr

if __name__ == "__main__":
    for i in range(1):
        c = extract(i)
        t = transform(c)
        t = json.dumps(t,indent=2)
        print(t)





# import requests

# from bs4 import BeautifulSoup

# url = "https://wwww.simplyhired.com"
# response = requests.get(url)

# content = response.content

# soup = BeautifulSoup(content,'html.parser')
# soup.prettify()
# # print(soup)

# job_list = soup.find_all("ul",id='job-list')



# print(job_list)





















