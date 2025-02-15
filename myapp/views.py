from django.shortcuts import render, redirect
from django.http import JsonResponse
from io import BytesIO
import base64
import src.my_script.Executable as Executable
import src.my_script.JobObject as JobObject
import src.my_script.Filter as Filter
from .forms import AttributeSelectionForm
from .forms import FilterSelectionForm
from .forms import GraphSelectionForm


##This session.get has some issues because the filters do not reset after the plotting. Which is a PAIN.
##I think it should be possible to set the filters to be empty again after passing it to the exe
def plot(request):
    plots = []

    attributes = request.GET.getlist('attributes')


    filters = {
        'jobtitle': request.session.get('jobtitle', []),
        'sector': request.session.get('sector', []),
        'company': request.session.get('company', []),
        'language': request.session.get('language', []),
        'location': request.session.get('location', []),
    }

    for attribute in attributes:
        
        #Set up the data set & apply filters
        jobs = JobObject.createlist()

        
        for key, value in filters.items(): 
            if value != '' and value !=[]:
                jobs = Filter.contains(jobs, {key : value})
        

        print("Graphtype i nthe views fiel", request.GET.get(f'graphtype_{attribute}'))
        plt = Executable.run(attribute, request.GET.get(f'graphtype_{attribute}'), jobs)
        
        # Convert plot to PNG image in memory
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()


        plot_data = base64.b64encode(buffer.read()).decode('utf-8')
        plots.append(plot_data)

    # Encode the PNG image to base64
    return plots


def home(request):

    if 'submit_filters' in request.GET:
        print("Pressed Apply Filters")
        
        # Store filters in the session
        request.session['jobtitle'] = request.GET.get('jobtitle', [])
        request.session['sector'] = request.GET.getlist('sector', [])
        request.session['company'] = request.GET.get('company', [])  
        request.session['language'] = request.GET.getlist('language', [])  
        request.session['location'] = request.GET.getlist('location', [])  

    filter = FilterSelectionForm(request.GET or None)
    form = AttributeSelectionForm(request.GET or None)
    graph = GraphSelectionForm(request.GET or None)

    plots = []

    if form.is_valid():
        plots = plot(request)        
        request.session['plots'] = plots
        return redirect('home')
   
    if 'plots' in request.session:
        plots = request.session.pop('plots')
    
    context = {
        'welcome_message': 'Welcome to AI Job Help HSLU!',  # Update message here
        'form' : form,
        'filter' : filter,
        'plots' : plots,
        'graph' : graph,
        # Add more dynamic data as needed
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Only return JSON-serializable data
        return JsonResponse({'plots': plots})
    
    return render(request, 'myapp/home.html', context)