import json

# Additional Notes for this File:
# Maybe it would be good to do the normalizaiton before creating the JobObjects.




#Define the JobObject with the required attributes
class JobObject:
    def __init__(self, id, jobtitle, company, sector, publish_date, language, workload, 
                 contract_type, role, benefits, location, ai_tech, salary, techskills, softskills, degree, website):

        self.id = id
        self.jobtitle = jobtitle
        self.company = company
        self.location = location
        self.sector = sector
        self.language = language
        self.workload = workload
        self.contract_type = contract_type
        self.role = role
        self.benefits = benefits
        self.publish_date = publish_date
        self.ai_tech = ai_tech
        self.salary = salary
        self.techskills = techskills
        self.softskills = softskills
        self.degree = degree
        self.website = website





#Takes a json file and transforms it to a JobObject list.
def createlist():

    jobs = []
    job_objects = []

    #Acess .json file
    with open(r'src/my_script/Data/responses/combined.json', 'r', encoding='utf-8') as file:
        try:
            data = file.read()

            json_array = json.loads(data)
        
        #Take each .json string and convert it to a dictionary. Then append it to the jobs list
            for json_str in json_array:
                job_dict = json.loads(json_str)
                jobs.append(job_dict)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from json_object: {json_str}")
            print(e)


#Acess each dictionary in the jobs list and set the fields to the according value
    for job in jobs:
        id = job.get("MY ID")
        jobtitle = job.get("Jobtitle")
        company = job.get("Company")
        sector = job.get("Sector")
        publish_date = job.get("Publish Date")
        language = job.get("Language")
        location = job.get("Location")
        ai_tech = job.get("AI-technology")
        salary = job.get("Salary")
        techskills = job.get("Techskills")
        softskills = job.get("Softskills")
        degree = job.get("Degree")    
        workload = job.get("Workload")
        contract_type = job.get("Contract Type")
        role = job.get("Role")
        benefits = job.get("Benefits")
        website = job.get("Website")

#create new JobObject with the fields of the .json object in the loop
        job_object = JobObject(id, jobtitle, company, sector, publish_date, language, workload, 
                     contract_type, role, benefits, location, ai_tech, salary, techskills, softskills, degree, website)

#Append the current JobObject to the list of JobObjects
        job_objects.append(job_object)


#return the JobObject list
    return job_objects