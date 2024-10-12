from django.shortcuts import render

# Create your views here.
def render_author(request):
    return render(request, template_name='author_app/view_author.html')

def render_all_authors(request):
    return render(request, template_name='author_app/all_authors.html')

