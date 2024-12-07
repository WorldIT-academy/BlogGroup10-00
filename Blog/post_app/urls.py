from django.urls import path
from .views import *

urlpatterns=[
    path('all_posts/', view_all_posts, name = "all_posts"),
    path('view_post/<int:pk>', view_post, name = 'view_post')
]
