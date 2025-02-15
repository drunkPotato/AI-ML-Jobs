import re
import src.my_script.Classification as Classification


#IMPORTANT:
#At the moment this won't work since the attributes are not yet formatted to being lists

#It seems this function returns an empty list since it runs smoothly without any filter


#This is the logic of this program:
#Filter are being passed as a key : value pair (e.g. "Jobtitle" : "Data Scientist")
#We need to pass the key to know wich attribute we have to access in our JobObjects.
#Then we apply logic and return a new list of JobObjects that match the criteria




#This function checks all jobs if they contain a specific value in one of their attributes (key : value -- "Jobtitle" : "Data Scientist")
def contains(jobs, filter):
    
    #There shouldn't have been data as a filter because I didn't type it in. I don't know why it has
    for item in filter.items():
        print(item)

    print(len(jobs))
    #define returned list
    filteredList = []

    #access the filter
    key = list(filter.keys())[0] 
    values = filter[key]



    ##The problem lies here
    
    # Iterate over each job in the passed jobs list
    for job in jobs:
        
        #We access the attribute of the job. --> For now this can be either a string or a list. I should change it to be lists only.
        attr_value= getattr(job, key.lower(), "")

        #Basically we have to do the same thing twice now for the different types of attributes

        #If the attribute is a list (normal usecase in the future)
        if (isinstance(attr_value, list)):
            print("Are we even here??")

            #We iterate over the all the filters there are
            for value in values:

                #Now we want to check if the value of the attribute is in the specific list that corresponds to the classification
                #We access the category 'key' 
                categorymapping = Classification.getcategory(key)
                print("categorymapping:" ,categorymapping)
                print("category specific element: ", categorymapping[value])
                
                #Now we access the correct element of our category 'key' (e.g. secotr )
                for object in categorymapping[value]:
                    for attr_val in attr_value:
                        #Now we check if it can be counted as "in the category"
                        if attr_val in object:
                            if(job not in filteredList):
                                filteredList.append(job)

        elif (isinstance(attr_value, str)):
            print("We're dealing with a string")

            #We're iterating over the filters
            for value in values:

                categorymapping = Classification.getcategory(key)

                #This doesn't work for the filters that are typed in by the user because they are not in the mapping of course
                #So they have to be handled seperately
                for object in categorymapping[value]:
                    if attr_value.lower() in object:
                        if(job not in filteredList):
                            filteredList.append(job)


    for filteredjob in filteredList:
        print(getattr(filteredjob, key.lower(), ""))

    print(len(filteredList))
    return filteredList