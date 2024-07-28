import re
import src.my_script.Classification as Classification
#Input Dictionary with JobObject objects

#Define different filter functions for the different criteria
#Return List of JobObject objects fulfilling the requirements

#The things that are passed are: 
#The list itself
#The input (the attribute we're interested in like: Company or Language)
#The keyword we're looking for(e.g. French)

def filtergetinput(lst, attribute, keyword):

    outputlist = []
    
    #keywords = []
    #category = [Classification.getcategory_mapping(attribute, keyword)]

    for job in lst:
        atr = getattr(job, attribute.lower(), None)

        print(atr)

        if atr is not None:

            #if isinstance(atr, str):
            #    atr_items = [item.strip().lower() for item in atr.split(',')]
            #elif isinstance(atr, list):
            #    atr_items = atr
            #else:
            #    pass

            if keyword in atr:
                outputlist.append(job)
    
    return outputlist



def filterleaveinput(list, input, keyword):

    outputlist = []

    for job in list:
        attr_value = getattr(job, input.lower(), None)

        if attr_value == None:
            continue
    
        print("keyword: ", keyword, "item: ", attr_value)
        if not any(keyword in item for item in attr_value):
            outputlist.append(job)
            
    return outputlist