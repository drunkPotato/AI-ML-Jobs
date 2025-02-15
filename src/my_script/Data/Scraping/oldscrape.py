import requests
from bs4 import BeautifulSoup
import openai
import json
from dotenv import load_dotenv, find_dotenv
import os
from openai import OpenAI
from datetime import date

#Note there was a weird error that tripped up the code
#Note we're not filtering for relevance which I have to change
#Not an Issue I dont know how to fix yet is the changing html code of the website
#Note I should seperate the GPT analysis from the other part of the code and see which side causes erros

#Logic:
#Go to the jobs.ch page
#Find all the links (href) to the individual job pages
#Go to each page & scrape the info
#Analyse the text for additional information
#Add the analysis into the json object so the format is correct
#Write it to the .txt file

#Set up with UI PATH (Get one then complete the process with GPT and go to the next one)
#Convert the finished python scripts to .exe files



#Setting up OpenAI Key
dotenv_path = r"C:/Users/hidbe/VSCodeProjects/JobAssistance/.env"
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


#Visits a webpage and returns the soup. If the webpage inst found it returns the status code
def visitPage(url):
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        print("Webpage found", soup.title.text)
        return soup
    else:
        print("Webpage not found", response.status_code) 
    

#Finds the URL for each of the listings and returns them as a list
def findURL(soup):

    linklist = []
    htmlobject1 = soup.find('div', class_= 'd_flex flex-d_column h_100% w_100%')
    htmlobject2 = htmlobject1.find_all("article")
    for job in htmlobject2:
        if(htmlobject2):           
           link = "https://www.jobs.ch" + job.find("a" , {"data-cy": "job-link"}).get('href')
        linklist.append(link)
        print(link)
    return linklist

#This function navigates the html code to find the objects we need to access the data
def accessData(soup, URL):

    #This series of .find goes through the various objects since we cant directly acess them.
    htmlObject1 = soup.find('div', class_ = 'h_100% w_100%')
    htmlObject2 = htmlObject1.find('main', class_ = 'grid-area_jobAd w_100%')
    logo1 = htmlObject2.find("div" , {"data-cy": "vacancy-logo"})
    if(logo1):
        logo2 = logo1.find('img')
    else:
        logo2 = None
    htmlObject3 = htmlObject2.find("div" , {"data-cy": "vacancy-info"})
    if htmlObject3 is None:
        placeholder = htmlObject2.find('div', class_ = 'pos_relative')
        htmlObject3 = placeholder.find('div', class_ ='grid-area_info mt_s24 sm:mt_s40') 

    htmlObject4 = htmlObject3.find('ul', class_ = ['li-t_none pl_s0 mb_s0 mt_s0 d_grid gap_s16 grid-tc_[auto] sm:grid-tc_[1fr_1fr] md:grid-tc_[1fr] pb_s24', 
                                   'li-t_none pl_s0 mb_s0 mt_s0 d_grid gap_s16 grid-tc_[auto] sm:grid-tc_[repeat(2,_1fr)] md:grid-tc_[repeat(3,_1fr)] grid-tr_[repeat(4,_auto)_minmax(72px,1fr)] sm:grid-tr_[repeat(2,_auto)_minmax(72px,1fr)] md:grid-tr_[auto_minmax(72px,1fr)]'])
    htmlObject5 = htmlObject4.find_all('li')  
    htmlObject6 = htmlObject2.find('span', class_ = 'bjhRRP nVRGN gsjAMe jHMARW notranslate')

    #At this time we have accessed all the right objects and can now start to extract and format the text
    text = "{\n"
    text += "\"URL\" : " + URL + "\"\n"
    text += "\"Titel\" : " + "\"" + soup.title.text.split(' - ')[0] + "\"\n"

    #Rarely they add the company as an image so we cannot extract its text
    if htmlObject6 is not None:
        text += "\"Firma\" : " + "\"" + htmlObject6.get_text() + "\"\n"
    if (logo2):
        text += "\"Logo\" : " + "\"" + logo2.get('src').replace("48x0", "500x0") + "\"\n"

    #htmlObject5 contains multiple fields like Publish Date & Contract Type
    for obj in htmlObject5:
        #With some logic we format them correctly
        key, value = obj.get_text().replace("\n", "").split(":")
        text +=  f'"{key.strip()}" : "{value.strip()}"' + "\n"


    #GPT Analysis
    system_message_content = ( 
            """
        Extract the following fields from this job description:
        - Benefits
        - Requirements
        - Responsibilities

        Return the result as a JSON object with this format:
        {
          \"Benefits\": \"...\",
          \"Requirements\": \"...\",
          \"Responsibilities\": \"...\",
        }
        """
    )    
    content = htmlObject2.get_text().replace("\n", "")
    client = OpenAI(organization='org-Mwew5KzJPrkUVmfjavXwSslP')
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    #response_format={"type": "json_object"},  
    messages=[
        {"role": "system", "content": system_message_content},
        {"role": "user","content": content}
    ],
    temperature=0.7,
    max_tokens=1024,
    top_p=1
    )
    completion = json.loads(response.choices[0].message.content)

    text += f"\"Benefits\" : \"{completion['Benefits']}\"\n"
    text += f"\"Requirements\" : \" {completion['Requirements']}\"\n"
    text += f"\"Responsibilities\" : \" {completion['Responsibilities']}\"\n"

    #htmlobject 2 contains the entire text 
    text += "\"Text\" : " + "\"" +htmlObject2.get_text().replace("\n", "") + "\"\n}"

    #If the lowest object of the hierarchy is present the above are as well
    if(htmlObject5):
        return text
    else:
        return 'No text available'



### This is the Executed code ###

#I should change this into a single function and make the exe call that function with the given parameters

#Make it so that this is a function and callable with different arguments (machine learning, artificial intelligence)
#To decide what we are scraping change the link below so that the 'term' is what you are looking for ↓ (here ai) & the range to be how many pages there are
for a in range(1, 26):

    #We visit a page & get it's <html> code. This is referenced as "soup" in the code.
    soup = visitPage('https://www.jobs.ch/de/stellenangebote/?page=' + str(a) + '&source=home&term=%22machine%20learning%22')

    #In this soup (<html>) we then find the URL ('href') for each of the jobs we want to scrape. 
    #In this for loop we now go over each job individually 
    for link in findURL(soup):

        #We iterate over the individual jobs & extract the soup
        soup = visitPage(link)


        #We get all the data we want & format it directly
        data = accessData(soup, link)


        #We then write the entry for the individual job into the file and add three newlines to seperate it from the next
        with open(f"{date.today()}_Jobs_CH.txt", 'a', encoding='utf-8', errors='ignore') as file:
            file.write(data)
            file.write("\n\n\n")