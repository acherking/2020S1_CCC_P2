from django.http import HttpResponse
from django.shortcuts import render
from . import testcouchdb
from . import ProcessingData
#This function is used to return index page
def hello(request):
    context = {}
    context['hello'] = 'CCC A2 Web'
    return render(request, 'index.html', context)

#This function contains the data that should displayed
def display(request):
    ctx={}
    ctx['rlt'] = [100,100,100,100,100,100,100]
    #if request.POST:
        #ctx['rlt'] = ProcessingData.processingdata()
        #ctx['rlt'] = testcouchdb.readcouchdb()
    #return render(request, 'display.html', ctx)
    return render(request, 'test.html', ctx)

def introduction(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = 'This is introduction page'

    return render(request, 'introduction.html', ctx)