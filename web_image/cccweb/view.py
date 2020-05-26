import json

from django.http import HttpResponse
from django.shortcuts import render
from . import webdb

#This function is used to return index page
def hello(request):

    return render(request, 'index.html')

#This function contains the data that should displayed
def display(request):
    ctx={}
    ctx['rlt']=['test']

    #get database data
    afterCovidMelbourneMood = webdb.readAfterCovidMelbournemood()
    beforeCovidMelbourneMood = webdb.readBeforeCovidAustriliamood()
    afterCovidAustriliaTweetNumber = webdb.readAfterCovidAustriliaTweetNumber()
    beforeCovidAustriliaTweetNumber = webdb.readBeforeCovidAustriliaTweetNumber()
    afterCovidMelbourneTweetNumber = webdb.readAfterCovidMelbourneTweetNumber()
    beforeCovidMelbourneTweetNumber = webdb.readBeforeCovidMelbourneTweetNumber()
    comparingAustriliaHappiness = webdb.getComparingAustriliaHappiness()
    comparingAustriliaTweetNumber = webdb.getComparingAustriliaTweetNumber()
    pastAustriliaHashTag = webdb.getPastAustriliaHashTag()
    nowAustriliaHashTag = webdb.getNowAustriliaHashTag()
    aurinMelbourne = webdb.readAurinMelbourne()
    ctx['austriliamap'] = 'This is introduction page'
    ctx['melbournemap'] = 'This is introduction page'
    #if request.POST:
        #ctx['rlt'] = ProcessingData.processingdata()
        #ctx['rlt'] = testcouchdb.readcouchdb()
    #return render(request, 'display.html', ctx)
    return render(request, 'display.html', {
        'comparingAustriliaHappiness': json.dumps(comparingAustriliaHappiness),
        'comparingAustriliaTweetNumber': json.dumps(comparingAustriliaTweetNumber),
        'pastAustriliaHashTag': json.dumps(pastAustriliaHashTag),
        'nowAustriliaHashTag': json.dumps(nowAustriliaHashTag),
        'afterCovidMelbourneMood':json.dumps(afterCovidMelbourneMood),
        'aurinMelbourne': json.dumps(aurinMelbourne),
                                            'beforeCovidMelbourneMood': json.dumps(beforeCovidMelbourneMood),
                                            'afterCovidAustriliaTweetNumber':json.dumps(afterCovidAustriliaTweetNumber),
                                            'beforeCovidAustriliaTweetNumber': json.dumps(beforeCovidAustriliaTweetNumber),
                                            'afterCovidMelbourneTweetNumber':json.dumps(afterCovidMelbourneTweetNumber),
                                            'beforeCovidMelbourneTweetNumber':json.dumps(beforeCovidMelbourneTweetNumber)})

def displayMelbourne(request):
    ctx={}
    ctx['rlt']=['test']

    #get database data
    afterCovidMelbourneMood = webdb.readAfterCovidMelbournemood()
    beforeCovidMelbourneMood = webdb.readBeforeCovidAustriliamood()
    afterCovidAustriliaTweetNumber = webdb.readAfterCovidAustriliaTweetNumber()
    beforeCovidAustriliaTweetNumber = webdb.readBeforeCovidAustriliaTweetNumber()
    afterCovidMelbourneTweetNumber = webdb.readAfterCovidMelbourneTweetNumber()
    beforeCovidMelbourneTweetNumber = webdb.readBeforeCovidMelbourneTweetNumber()
    comparingAustriliaHappiness = webdb.getComparingAustriliaHappiness()
    comparingAustriliaTweetNumber = webdb.getComparingAustriliaTweetNumber()
    pastAustriliaHashTag = webdb.getPastAustriliaHashTag()
    nowAustriliaHashTag = webdb.getNowAustriliaHashTag()
    aurinMelbourne = webdb.readAurinMelbourne()
    ctx['austriliamap'] = 'This is introduction page'
    ctx['melbournemap'] = 'This is introduction page'
    #if request.POST:
        #ctx['rlt'] = ProcessingData.processingdata()
        #ctx['rlt'] = testcouchdb.readcouchdb()
    #return render(request, 'display.html', ctx)
    return render(request, 'display_melbourne.html', {
        'comparingAustriliaHappiness': json.dumps(comparingAustriliaHappiness),
        'comparingAustriliaTweetNumber': json.dumps(comparingAustriliaTweetNumber),
        'pastAustriliaHashTag': json.dumps(pastAustriliaHashTag),
        'nowAustriliaHashTag': json.dumps(nowAustriliaHashTag),
        'afterCovidMelbourneMood':json.dumps(afterCovidMelbourneMood),
        'aurinMelbourne': json.dumps(aurinMelbourne),
                                            'beforeCovidMelbourneMood': json.dumps(beforeCovidMelbourneMood),
                                            'afterCovidAustriliaTweetNumber':json.dumps(afterCovidAustriliaTweetNumber),
                                            'beforeCovidAustriliaTweetNumber': json.dumps(beforeCovidAustriliaTweetNumber),
                                            'afterCovidMelbourneTweetNumber':json.dumps(afterCovidMelbourneTweetNumber),
                                            'beforeCovidMelbourneTweetNumber':json.dumps(beforeCovidMelbourneTweetNumber)})
def introduction(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = 'This is introduction page'

    return render(request, 'introduction.html', ctx)

def detail(request):
    ctx={}
    return render(request, 'detail.html',ctx)

def displayCompare(request):
    ctx={}
    ctx['rlt']=['test']

    #get database data
    afterCovidMelbourneMood = webdb.readAfterCovidMelbournemood()
    beforeCovidMelbourneMood = webdb.readBeforeCovidAustriliamood()
    afterCovidAustriliaTweetNumber = webdb.readAfterCovidAustriliaTweetNumber()
    beforeCovidAustriliaTweetNumber = webdb.readBeforeCovidAustriliaTweetNumber()
    afterCovidMelbourneTweetNumber = webdb.readAfterCovidMelbourneTweetNumber()
    beforeCovidMelbourneTweetNumber = webdb.readBeforeCovidMelbourneTweetNumber()
    comparingAustriliaHappiness = webdb.getComparingAustriliaHappiness()
    comparingAustriliaTweetNumber = webdb.getComparingAustriliaTweetNumber()
    pastAustriliaHashTag = webdb.getPastAustriliaHashTag()
    nowAustriliaHashTag = webdb.getNowAustriliaHashTag()
    aurinMelbourne = webdb.readAurinMelbourne()
    ctx['austriliamap'] = 'This is introduction page'
    ctx['melbournemap'] = 'This is introduction page'
    #if request.POST:
        #ctx['rlt'] = ProcessingData.processingdata()
        #ctx['rlt'] = testcouchdb.readcouchdb()
    #return render(request, 'display.html', ctx)
    return render(request, 'display_compare.html', {
        'comparingAustriliaHappiness': json.dumps(comparingAustriliaHappiness),
        'comparingAustriliaTweetNumber': json.dumps(comparingAustriliaTweetNumber),
        'pastAustriliaHashTag': json.dumps(pastAustriliaHashTag),
        'nowAustriliaHashTag': json.dumps(nowAustriliaHashTag),
        'afterCovidMelbourneMood':json.dumps(afterCovidMelbourneMood),
        'aurinMelbourne': json.dumps(aurinMelbourne),
                                            'beforeCovidMelbourneMood': json.dumps(beforeCovidMelbourneMood),
                                            'afterCovidAustriliaTweetNumber':json.dumps(afterCovidAustriliaTweetNumber),
                                            'beforeCovidAustriliaTweetNumber': json.dumps(beforeCovidAustriliaTweetNumber),
                                            'afterCovidMelbourneTweetNumber':json.dumps(afterCovidMelbourneTweetNumber),
                                            'beforeCovidMelbourneTweetNumber':json.dumps(beforeCovidMelbourneTweetNumber)})