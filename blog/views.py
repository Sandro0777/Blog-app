import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import blogSerializer
from blog.models import BlogModel
from django.db.models import Q

# Create your views here.
def  view