from django.urls import path
from .views import *

urlpatterns=[
    path('all_posts/', view_all_posts),
    path('view_post/', view_post)
]
