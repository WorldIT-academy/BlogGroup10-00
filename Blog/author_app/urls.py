# from django.contrib import admin
from django.urls import path
from .views import render_author,render_all_authors

urlpatterns = [
    path('all_authors/', render_all_authors),
    path('view_author/', render_author)
]