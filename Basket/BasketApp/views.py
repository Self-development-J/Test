from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from django.http import HttpResponse
# from boardapp.models import Boards

# Create your views here.

def index(request):
    return HttpResponse("안녕 씨발련아. 너 진짜 좆같이 생겼구나?")