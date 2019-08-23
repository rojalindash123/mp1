from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts= [
    {
        'author':'Rojalin',
        'title':'Python',
        'content':'Django',
        'date_posted':'22 aug 2019'
    },
    {
        'author':'Monalin',
        'title':'java',
        'content':'gui',
        'date_posted':'22 aug 2019'
    }
]
def home1(request):
    {
       'posts' : posts
    }
    return render(request,'new1/home.html')


def about(request):
    return render(request,'new1/about.html',{'title':'about'})