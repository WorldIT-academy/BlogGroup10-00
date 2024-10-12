from django.shortcuts import render
 

def view_home(request):
    return render(request, template_name= "core_app/home.html")

