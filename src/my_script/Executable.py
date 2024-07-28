
#Exists momentarily because of Django 
def main_function():
    pass

import src.my_script.Visualization as Visualization
import src.my_script.Classification as Classification
import src.my_script.JobObject as JobObject
import src.my_script.Filter as Filter
 


#Think about what the inputs are
#They should be: Filters, Keywords, 
def run(input):


    #create a Job Object list
    #In the future this list should be passed instead of coded into the JobObject class
    jobs = JobObject.createlist()

    #Should only return a list of JobObjects with the value Finance in the Sector attribute
    #jobs = Filter.filtergetinput(jobs, "Sector", "Finance")

    normalized_values = []
    
    for job in jobs:
        normalized_values.append(Classification.normalize(getattr(job, input.lower())))

    #normalized_values = Filter.filtergetinput(normalized_values, "Sector", "Finance")
    #jobs = Filter.filterleaveinput(jobs, "Language", "Deutsch")

    print("length jobs after filed", len(jobs))


    #Classify the now normalized values
    #The returned list must be equal in length or there is something wrong
    if(input != "Techskills" and input != "Softskills"):
        classified_list = Classification.classify_single(normalized_values, input)
    else:
        classified_list = Classification.classify_multiple(normalized_values, input)



    if len(classified_list) != len(normalized_values):
        print("length classified list: ", len(classified_list), " Length normalized values: ", len(normalized_values))
        #print(len(classified_list), ",", len(normalized_values))

    #Visually Display the Data
    return(Visualization.plotinput(classified_list))

#run("Title")
#run("Company")
#run("Location")
run("Sector")
#run("Language")
#run("Pensum")
##run("Contract Type")
#run("Role")
#run("Benefits")
##run("Publish_Date")
##run("Ai_Tech")
##run("Salary")
#run("Techskills")
#run("Softskills")
#run("Degree")
#run("Website")