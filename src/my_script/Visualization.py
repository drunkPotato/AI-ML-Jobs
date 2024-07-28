
#Exists because of Django momentarily
def generate_graphs():
    pass

#Define class

#Input should be a dictionary of JobObject objects
#Task of the function is to show the data as graphs
#Add identical data points together

#For that matter what is the final data
#Return Nothing

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter




#Displays the single attribute of the list
def DisplayOne(list, attribute):
    pass


#Displays all the attributes of the list
def Display(list):
    pass


def plotinput(mylist):

    mycounter = Counter()
    
    #Go through the passed list
    for job in mylist:
        if isinstance(job, list):
            for item in job:
                mycounter[item] += 1
        else:
            mycounter[job] += 1
            

    # Step 2: Sort the items by frequency in descending order
    sorted_items = sorted(mycounter.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Select the top 15 elements
    top_15_items = sorted_items[:15]

    # Prepare labels and values for the top 15 items
    labels = [item[0] for item in top_15_items]
    values = [item[1] for item in top_15_items]

        # Create the bar chart
    positions = range(len(labels))
    plt.figure(figsize=(15, 8))
    plt.bar(positions, values, align='center')
    plt.xticks(positions, labels, rotation=90)

# Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Values by Categories')

# Add xticks with rotated labels for better readability
    plt.xticks(positions, labels, rotation=90)
# Adjust layout to fit labels
    plt.tight_layout()
# Show the plot
    plt.show()
    return(plt)

    #for element in notdisplayed:
        #print(element)
        
    print(len(notdisplayed))