#Input should be a dictionary of JobObject objects
#Task of the function is to show the data as graphs
#Add identical data points together

#For that matter what is the final data
#Return Nothing
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def truncate_label(label, max_length=20):
    """Truncate label if it's too long."""
    if len(label) > max_length:
        return label[:max_length] + "..."
    return label

def plotinput(mylist, graphtype, input):
        
    mycounter = Counter()
    # Go through the passed list
    for job in mylist:
        if isinstance(job, list):
            for item in job:
                if item != "Not Specified":  # Skip "Not Specified"
                    mycounter[item] += 1
        else:
            if job != "Not Specified":  # Skip "Not Specified"
                mycounter[job] += 1
             
    # Step 2: Sort the items by frequency in descending order
    sorted_items = sorted(mycounter.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Determine the count of the most frequent item
    if len(sorted_items) == 0:
        raise ValueError("No data to plot.")
    max_count = sorted_items[0][1]
    
    # Step 4: Filter items based on the 1/20 rule and limit the number of elements to 13
    filtered_items = [item for item in sorted_items if item[1] >= max_count / 20]
    top_items = filtered_items[:13]  # Display at most 13 elements

    # Prepare labels and values for the filtered items
    labels = [truncate_label(item[0]) for item in top_items]
    values = [item[1] for item in top_items]
    number_of_all_jobs = sum(mycounter.values())

    total_count = sum(values)

    positions = range(len(labels))

    if graphtype == "bar":
        plt.figure(figsize=(12, 8))
        plt.bar(positions, values, align='center')
        plt.xticks(positions, labels, rotation=90, fontsize=16)
        plt.xlabel('Categories', fontsize=16)
        plt.ylabel('Count', fontsize=16)
        plt.title(input, fontsize=20)
        plt.tight_layout()
        plt.text(0.95, 0.95, f"Shows {total_count} out of {number_of_all_jobs} items.", 
                 ha='right', va='top', transform=plt.gca().transAxes, fontsize=12)
        # Optionally, add the values on top of each bar
        for i, value in enumerate(values):
            plt.text(i, value, str(value), ha='center', va='bottom', fontsize=14)

    elif graphtype == "pie":
        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, autopct=lambda pct: f'{pct:.1f}%\n({int(pct * total_count / 100)})'
                , startangle=140, labeldistance=1.1, pctdistance=0.85, textprops={'fontsize': 14})
        plt.title(input, fontsize=18)
        plt.tight_layout()
        plt.text(1, 1, f"Shows {total_count} out of {number_of_all_jobs} items.", 
                ha='right', va='top', transform=plt.gca().transAxes, fontsize=8)


    elif graphtype == "line":
        plt.figure(figsize=(12, 8))
        plt.plot(labels, values, marker='o')
        plt.xticks(rotation=90, fontsize=12)
        plt.xlabel('Categories', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title(input, fontsize=16)
        plt.tight_layout()
        plt.text(0.95, 0.95, f"Shows {total_count} out of {number_of_all_jobs} items.", 
                 ha='right', va='top', transform=plt.gca().transAxes, fontsize=12)

    elif graphtype == "scatter":
        plt.figure(figsize=(12, 8))
        plt.scatter(labels, values, color='blue', s=100)
        plt.xticks(rotation=90, fontsize=12)
        plt.xlabel('Categories', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title(input, fontsize=16)
        plt.tight_layout()
        plt.text(0.95, 0.95, f"Shows {total_count} out of {number_of_all_jobs} items.", 
                 ha='right', va='top', transform=plt.gca().transAxes, fontsize=12)

    elif graphtype == "area":
        plt.figure(figsize=(12, 8))
        plt.fill_between(range(len(labels)), values, color="skyblue", alpha=0.4)
        plt.plot(range(len(labels)), values, marker='o', color="Slateblue", alpha=0.6)
        plt.xticks(range(len(labels)), labels, rotation=90, fontsize=12)
        plt.xlabel('Categories', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title(input, fontsize=16)
        plt.tight_layout()
        plt.text(0.95, 0.95, f"Shows {total_count} out of {number_of_all_jobs} items.", 
                 ha='right', va='top', transform=plt.gca().transAxes, fontsize=12)
    else:
        raise ValueError(f"Graph type '{graphtype}' is not supported. Use 'bar', 'pie', or 'line'.")
    
    # Show the plot
    return plt