from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Article


# Create your views here.

class UserView(View):
    def get(self, request):
        ariticle = Article.objects.get(id=1)

        return HttpResponse(ariticle.name)
