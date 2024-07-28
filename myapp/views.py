from django.shortcuts import render
import json
from django.http import JsonResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import src

from src.my_script.Executable import main_function
from src. my_script.Visualization import generate_graphs

def plot_view(request):
    # Generate a sample plot (replace with your actual plot generation logic)
    plt.figure(figsize=(8, 6))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.title('Sample Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    # Convert plot to PNG image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the PNG image to base64
    graphic = base64.b64encode(buffer.read()).decode('utf-8')

    return graphic


def home(request):

    selected_option = request.GET.get('option', 'Title')  # Default to 'Title' if option is not specified
    options = ['Title', 'Sector', 'Location', 'Other Option']
    graphic = plot_view(request)
    
    context = {
        'welcome_message': 'Welcome to AI Job Help HSLU!',  # Update message here
        'image_path': 'myapp/images/LOGO.jpg',
        'selected_option' : selected_option,
        'options' : options,
        'graphic' : graphic
        # Add more dynamic data as needed
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(context)
    
    return render(request, 'myapp/home.html', context)


def view_that_uses_json(request):
    # Assuming data.json is in your static directory
    json_file_path = 'json/data.json'  # Adjust the path as per your setup
    
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    context = {
        'json_data': data,
    }
    
    return render(request, 'template.html', context)



def index(request):
    # Example usage of existing code
    result = main_function()
    graph_url = generate_graphs(result)
    return render(request, 'index.html', {'graph_url': graph_url})