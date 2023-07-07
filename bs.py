import requests
from bs4 import BeautifulSoup

# Set the URL and headers
url = 'https://www.simplyhired.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Set the search query and filters
query = 'data scientist'
location = 'New York, NY'
radius = '50'
page = 1

# Loop through the pages and scrape the job listings
while page <= 2:
    params = {'q': query, 'l': location, 'radius': radius, 'pn': page}
    response = requests.get(url + '/job-search', headers=headers, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the job listings and extract the job titles
    job_listings = soup.find_all('div', class_='SerpJob-jobCard card')
    jobs = [job.find('a', class_='SerpJob-link').text.strip() for job in job_listings]

    # Print the list of jobs
    print(f"Page {page} Jobs:\n")
    for job in jobs:
        print(job)
    print("\n")

    # Move to the next page
    page += 1
