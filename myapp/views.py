from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
import json
import os
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            
            # Set the faculty and teacher_grade fields from the form
            #new_user.faculty = user_form.cleaned_data['faculty']
            #new_user.teacher_grade = user_form.cleaned_data['teacher_grade']
            
            # Save the user object
            new_user.save()
            
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})





def teacher_dashboard(request):
    # Get the absolute path to the JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), 'classrooms.json')

    # Read and parse the JSON file
    with open(json_file_path, 'r') as json_file:
        classrooms = json.load(json_file)

    return render(request, 'teacher_dashboard.html', {'classrooms': classrooms})