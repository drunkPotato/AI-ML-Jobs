from django import forms

class AttributeSelectionForm(forms.Form):
    attributes = forms.MultipleChoiceField(
        choices=[
            ("Jobtitle", "Jobtitle"),
            ("Sector", "Sector"),
            ("Company", "Company"),
            ("Publish_Date", "Publish Date"),
            ("Language", "Language"),
            ("Location", "Location"),
            ("AI_Tech", "AI Tech"),
            ("Salary", "Salary"),
            ("Techskills", "Techskills"),
            ("Softskills", "Softskills"),
            ("Degree", "Degree"),
            ("Workload", "Workload"),
            ("Contract_Type", "Contract Type"),
            ("Role", "Role"),
            ("Benefits", "Benefits")
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Select Attributes to Plot",
        required=False
    )

class GraphSelectionForm(forms.Form):
    graphtype = forms.ChoiceField(
        choices= [
            ("Bar", "Bar Chart"),
            ("Pie", "Pie Chart"),
            ("Other", "And so on")
        ]
    )

class FilterSelectionForm(forms.Form):

    jobtitle = forms.CharField(label="Job Title", required=False)

    sector = forms.MultipleChoiceField(
        choices=[
            ("Manufacturing", "Manufacturing"),
            ("Retail", "Retail"),
            ("Health Care", "Health Care"),
            ("Finance", "Finance"),
            ("ICT", "ICT"),
            ("Utilities", "Utilities"),
            ("Real Estate", "Real Estate"),
            ("Public Sector", "Public Sector"),
            ("Other", "Other")
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Select the Sector to Filter for",
        required=False
    )

    company = forms.CharField(label="Company", required=False)

    language = forms.MultipleChoiceField(
        choices= [
            ("en", "English"),
            ("ger", "German"),
            ("fr", "French")
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Select the Language to Filter for",
        required=False
    )

    location = forms.MultipleChoiceField(
        choices= [
            ("Central Switzerland", "Central Switzerland"),
            ("Switzerland", "Switzerland"),
            ("Germany", "Germany"),
            ("Europe", "Europe"),
            ("US", "US"),
            ("Global", "Global"),
        ],
        widget=forms.CheckboxSelectMultiple,
        label="Select the Locations to Filter for",
        required=False
    )
    
class InputForm(forms.Form):
    input_field = forms.CharField(label='Input', max_length=100)