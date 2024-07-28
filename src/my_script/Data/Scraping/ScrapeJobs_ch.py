from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup


def visitPage(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        print("Webpage found", soup.title.text)

        return soup
    else:
        print("Webpage not found", response.status_code) 
    

def write_to_file(text):

    text = ' '.join(line.strip() for line in text.strip().split('\n') if line.strip())

    with open('example.txt', 'a', encoding= 'utf-8', errors= 'ingore') as file:
        while text:
            file.write(text[:150] + "\n")
            text = text[150:]
        file.write("\n\n")
      

#This function uses the passed href link to open the jobdescription on a seperate page
#Then the text is returned if there is one
def openFlowtext(link, classname):

    response = requests.get(link)


    soup = BeautifulSoup(response.content, "html.parser")

    helper = soup.find('main', class_= classname)

    flowtext = helper.find('div', class_= "pos_relative")
    
    if(flowtext):
        return flowtext.get_text()
    else:
        return 'No text available'
    

#Go to each page and scrape all the joblistings on it
for a in range(4, 5):
    soup = visitPage('https://www.jobs.ch/de/stellenangebote/?page=' + str(a) + '&source=home&term=artificial%20intelligence')


#For each page we visit we must first navigate to the HTML object we need
    
    #This has changed find the right class
    htmlobject1 = soup.find('div', class_= 'grow_1')

    
    htmlobject2 = htmlobject1.find_all('div', class_=['Div-sc-1cpunnt-0 Flex-sc-mjmi48-0 LnCSG', 'Div-sc-1cpunnt-0 Flex-sc-mjmi48-0 jcRJav'])
    for job in htmlobject2:
        #htmlobject2 = job.find('div', class_='Div-sc-1cpunnt-0 kiHQbx')
        if(htmlobject2):           
           link = "https://www.jobs.ch" + job.parent.get('href')
           print(job.parent.get('href'))
           write_to_file(openFlowtext(link, 'grid-area_jobAd w_100%')) #add the name of the div here

