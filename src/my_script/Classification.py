#returns values in the form of strings


def getcategory_mapping(category, element):   

    title_categories = {

    }

    company_categories = {
        "ETH Zürich" : ["eth", "ETH"],
        "Universität Bern" : ["university of bern", "universität bern"],
        "Universität St. Gallen" : ["university st. gallen", "university of st. gallen", "universität st. gallen", "universität st gallen"]
    }

    sector_categories = {
        "Energy" :["energy", "energie"],
        "Manufacturing": ["manufacturing", "produktion", "movement systems"],
        "Retail": ["retail", "einzelhandel"],
        "Health Care": ["health care", "gesundheitswesen", "medical", "pharma", "biotech", "medtech", "pathology"],
        "Finance": ["finance", "finanzen", "insurance", "financial"],
        "ICT": ["ict", "ikt", "computer science", "technology", "intelligent solutions", "people flow"],
        "Utilities": ["utilities", "versorgungsunternehmen"],
        "Real Estate": ["real estate", "immobilien", "building"],
        "Public": ["public", "öffentlicher dienst", "education", "research"],
        "Other" : []
    }

    publishdate_categories = {
        "January" : ["januar", "january"],
        "February": ["februar", "february"],
        "March": ["märz", "march"],
        "April": ["april"],
        "May": ["mai", "may"],
        "June": ["juni", "june"],
        "July": ["juli", "july"],
        "August": ["august"],
        "September": ["september"],
        "October": ["oktober", "october"],
        "November": ["november"],
        "December": ["dezember", "december"]
    }

    language_categories = {
        "German": ["deutsch", "german"],
        "English": ["englisch", "english"],
        "French" : ["french", "französisch"],
        "Italian" : ["italian", "italienisch"]
    }

    pensum_categories = {

    }

    contract_type_categories = {

    }

    role_categories = {

    }

    benefits_categories = {

    }

    location_categories = {
        "Zerntralschweiz" : ["luzern", "lucerne", "uri", "schwyz", "obwalden", "nidwalden", "zug",
                             "baar", "dierikon", "thermoplanplatz", "weggis", "eichacher", ],

        "Schweiz" : ["switzerland", "solothurn", "basel-stadt", "basel-landschaft", "schaffhausen", "appenzell ausserrhoden", "appenzell a.rh.",
            "appenzell innerrhoden", "appenzell i.rh.", "sankt gallen", "st. gallen", "graubünden", "aargau", "thurgau",  "tessin", 
            "waadt", "wallis", "neuenburg", "genf", "jura", "zürich", "bern", "freiburg", "ticino", "vaud", "valais", "neuchâtel", "geneva", "genève"
            "chur", "zollikofen", "baden", "wetzikon", "grabs", "winterthur", "rancate", "neuhausen", "mägenwil", "mönchaltdorf", "disentis", "eschlikon",
            "olten", "les acacias", "liestal", "sion", "niederönz", "ljubliana", "petit-lancy", "wolfhausen", "gland", "zimmerwald", "sursee", "uster",
            "Adliswil", "yverdon-les-bains", "yverdon", "domat/ems", "spreitenbach", "liebefeld", "reinbach", "arlesheim"]
    }


#Urgently ask Donnacha to provide this
    aitechnology_categories = {

    }

    salary_categories = {
        "~40'000" : [],
        "40'000 - 60'000" : [],
        "60'000 - 80'000" : [],
        "80'000 - 10'0000" : [],
        "100'000 +" : []
    }

    techskills_categories = {
        "Python" : ["python"],
        "SQL" : ["sql", "postgresql"],
        "C" : ["c#", "c++"],
        "Java" : ["java", "javascript"],
        "Office" : ["office", "excel", "power point", "powerpoint"],
        "Data Science" : ["data science"],
        "Data analysis" : ["data analysis", "daten analyse"],
        "Azure" : ["azure"],
        "Machine Learning" : ["machine learning"],
        "AWS" : ["aws"],
        "Docker" : ["docker"],
        "Power BI" : ["power bi", "powerbi"],
        "SAP" : ["sap"],
        "Kubernetes" : ["kubernetes"],
        "HTML" : ["html"],
        "Sark" : ["spark"],
        "DevOps" : ["devops"],
        "Tableau" : ["tableau"],
        "Statistics" : ["statistics", "statistik"],
        "Software Development" : ["software development"],
        "Pytorch" : ["pytorch"],
        "Linux" : ["linux"],
        "Git" : ["git", "github"],
        "Scala" : ["scala"],
        "Software Engineering" : ["software engineering"],
        "tensorflow" : ["tensorflow"],
        "Data Modeling" : ["data modeling", "data modelling"],
        #"CI / CD" : ["ci"]
        ".Net" : [".net"],
        "Databricks" : ["databricks"],
        "Cloud Computing" : ["cloud computing"],
        "Big Data" : ["big data"],
        "Matlab" : ["matlab"],
        "Kafka" : ["kafka"],
        "Snowflake" : ["snowflake"],
        "Terraform" : ["terraform"],
        "Data bases" : ["data base", "data bases", "datenbanken"],
        "Openshift" : ["openshift"],
        "Automation" : ["automation"],
        "Jenkins" : ["jenkins"]
    }

    softskills_categories = {
        "Problem solving" : ["problem-solving", "problem solving"],
        "Communication" : ["communication", "kommunikation"],
        "Team player" : ["team", "teamwork", "teamworking", "teamfähig"],
        "Analytical skills" : ["analytical"],
        "Flexibility" : ["flexiility", "Flexibilität"],
        "Leadership" : ["leadership"],
        "Collaboration" : ["collaboration"],
        "Organizational Skills" : ["organization", "organizational skills"],
        "Curiosity" : ["curious", "curiosity"],
        "Creativity" : ["creativity", "creative"],
        "Initiative" : ["initiative", "proactive", "initiativ"],
        "Independence" : ["independent", "independence", "unabhängig", "unabhängigkeit", "autonomy", "selbstständig"],
        "Reliability" : ["reliable", "reliability", "verlässlichkeit", "zuverlässig", "verantwortungsbewusst"],
        "Customer oriented" : ["customer", "kundenorientierung", "kundenorientiert"],
        "Presentation skills" : ["presentation"],
        "Detail oriented" : ["detail"],
        "Project Management" : ["project management"],
        "Motivated" :  ["self-motivated", "motivated"]
    }

    degree_categories = {
        "EFZ" : ["EFZ", "basic education", "commerical education"],
        "Fachhochschule" : ["Hochschule", "FH"],
        "Bachelor" : ["bachelor", "bsc"],
        "Master" : ["master", "msc"],
        "PhD" : ["phd", "doctoral"]
    }

    website_categories = {

    }

    mapping = {
        "title" : title_categories,
        "company": company_categories,
        "sector": sector_categories,
        "publish date": publishdate_categories,
        "language": language_categories,
        "pensum" : pensum_categories,
        "contract_type" : contract_type_categories,
        "role" : role_categories,
        "benefits" : benefits_categories,
        "location": location_categories,
        "ai-technology" : aitechnology_categories,
        "salary": salary_categories,
        "techskills" : techskills_categories,
        "softskills" : softskills_categories,
        "degree" : degree_categories,
        "website" : website_categories,
    }

    if element is None:
        return mapping.get(category.lower())
        return mapping.get(category.lower(), {}).get(element, [])

def normalize(value):

    if isinstance(value, str):
        return [v.strip() for v in value.split(",") if v.strip()]
    
    elif isinstance(value, list):
        return [str(v) for v in value]
    
    elif isinstance(value, dict):
        return [f"{k} : {v}" for k, v in value.items()]
    
    else:
        return ["unsupported type"]

#values is being passed as a list. the content of which are lists with 1 or more items
def classify_single(values, input):

    categories = getcategory_mapping(input.lower(), None)

    classified_list = []

#We go over all the objects in the passed list.
    for object in values:
#For each object we need to reset our entire flags
        best_match = None
        max_score = -1
        matched = False


#We go through all the items in said objects
        for item in object:
#If we matched a previous item in this object we step out
            if matched:
                break

            #print(item)
            item = item.lower()

            for category, keywords in categories.items():
                for keyword in keywords:
                
                    keyword = keyword.lower()

                    if keyword in item and matched == False: #if the keyword is in the values
                        classified_list.append(category)
                        matched = True

        if best_match is not None and max_score >= 90 and matched == False:
            classified_list.append(best_match)
            matched = True

        if matched == False:
            classified_list.append(object)
            matched = True


    return classified_list


def getcategory(category):
    return getcategory_mapping(category, None)

#In this function attributes that should / can yield multiple criteria 
#E.g. Techskills should include a variety of results for each job object.

#The logic is: Iterating over each job object gives us a list of items we have to iterate over again.
#Then the keywords are checked against the items. If any keyword is in the item it can then be categorised.
#If no matching keyword is found the item itself is appended to the list instead. 


def classify_multiple(values, input):

#We only care about the keywords in the matching category and thus only take the one fitting the input
#Also setting up the returned list

    categories = getcategory(input.lower())
    classified_list = []

#First we have to loop over all the objects here shown as values
#After that we have to iterate over all the items that are in each object (this can be multiple or only one)
    
    
    for object in values:
        for item in object:


#Now we must match each keyword in the appropriate category against each item.

            for category, keywords in categories.items():
                if any(keyword.lower() in item.lower() for keyword in keywords):                    
                    classified_list.append(category)
                    break
            else:
                classified_list.append(item)

#Add the category to the returned list if a match is found.
#Add the item to the returned list if no match is found.

#Potential bias:

#Appending each item has the potential to be bad if duplicates or very similar items are counted towards the same category multiple times.
#I should be able to accomadate but its not the most important now. 
    return classified_list
