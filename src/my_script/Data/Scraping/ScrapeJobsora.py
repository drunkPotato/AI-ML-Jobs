#On hold due to captcha
'''
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def visitPage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        print("Webpage found", soup.title.text)

        return soup
    else:
        print("Webpage not found", response.status_code)
    

def write_to_file(text):
    text = ' '.join(line.strip() for line in text.strip().split('\n') if line.strip())

    with open('jobsora.txt', 'a', encoding= 'utf-8', errors= 'ingore') as file:
        while text:
            file.write(text[:150] + "\n")
            text = text[150:]
        file.write("\n\n")
      

#This function uses the passed href link to open the jobdescription on a seperate page
#Then the text is returned if there is one
def openFlowtext(link, classname):

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(link)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    print(soup)
    #helper = soup.find('div', class_="")
    
    driver.quit()

    flowtext = ""

    if(flowtext):
        return flowtext.get_text()
    else:
        return 'No text available'
    
    

#Go to each page and scrape all the joblistings on it
for a in range(1, 300):
    soup = visitPage('https://de.jobsora.com/jobs?query=K%C3%BCnstliche+Intelligenz')
    htmlobject1= soup.find('main', class_='grid-common__col-9')
    htmlobject2= htmlobject1.find_all('article', class_='js-listing-item')
    for job in htmlobject2:
        link = job.get('data-href')
        write_to_file(openFlowtext(link, 'w-page w-page--unlimited'))
'''