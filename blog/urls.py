from django.urls import path,include
from . import views

urlpatterns = [
    path('addBlog/', views.addBlog, name="addBlog"),
    path('viewBlog/', views.viewBlog, name="viewBlog"),
    path('searchBlog/', views.searchBlog, name="searchBlog"),
]