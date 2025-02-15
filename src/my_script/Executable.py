
#Exists momentarily because of Django 
def main_function():
    pass

import src.my_script.Visualization as Visualization
import src.my_script.Classification as Classification




#Passed attributes are: Filters, Keywords, and the list
def run(input, graphtype, jobs):

    print("Input in the exe file", input)

    normalized_values = []
    
    for job in jobs:
        normalized_values.append(Classification.normalize(getattr(job, input.lower())))


    #### Rework this Classification part please


    #Classify the now normalized values
    #The returned list must be equal in length or there is something wrong
    if(input != "Techskills" and input != "Softskills"):
        classified_list = Classification.classify_single(normalized_values, input)
    else:
        classified_list = Classification.classify_multiple(normalized_values, input)



    if len(classified_list) != len(normalized_values):
        print("length classified list: ", len(classified_list), " Length normalized values: ", len(normalized_values))

    #Visually Display the Data
    return(Visualization.plotinput(classified_list, graphtype, input))

#weirdly little results (What is the issue?):
#run("Company")



#Doesnt exist yet:
##run("URL")


#Bad Reading by GPT:
#run("Ai_Tech")
#run("Salary")
#run("Publish_Date")


