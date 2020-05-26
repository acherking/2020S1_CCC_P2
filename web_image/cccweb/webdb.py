from couchdb import *
import couchdb
import json

from django.shortcuts import render

from . import dataProcessing


afterCovidMelbournemood = dataProcessing.readAfterCovidMelbournemood()
#print(afterCovidMelbournemood)

beforeCovidMelbournemood = dataProcessing.readBeforeCovidMelbournemood()
#print(beforeCovidMelbournemood)

afterCovidMelbourneTweetNumber = dataProcessing.readAfterCovidMelbourneTweetNumber()
beforeCovidMelbourneTweetNumber = dataProcessing.readBeforeCovidMelbourneTweetNumber()
#print(afterCovidMelbourneTweetNumber,beforeCovidMelbourneTweetNumber)


afterCovidAustriliaTweetNumber = dataProcessing.readAfterCovidAustriliaTweetNumber()
#print(afterCovidAustriliaTweetNumber)

beforeCovidAustriliaTweetNumber = dataProcessing.readBeforeCovidAustriliaTweetNumber()
#print(beforeCovidAustriliaTweetNumber)

afterCovidAustriliaMood = dataProcessing.readAfterCovidAustriliaMood()
#print(afterCovidAustriliaMood)

beforeCovidAustriliaMood = dataProcessing.readBeforeCovidAustriliaMood()
#print(beforeCovidAustriliaMood)


comparingAustriliaHappiness=dataProcessing.getComparingAustriliaHappiness(beforeCovidAustriliaMood, afterCovidAustriliaMood)
comparingAustriliaTweetNumber = dataProcessing.getComparingAustriliaTweetNumber(beforeCovidAustriliaMood, afterCovidAustriliaMood)

nowAustriliaHashTag=dataProcessing.getNowAustriliaHashTag()
#print(nowAustriliaHashTag)
pastAustriliaHashTag=dataProcessing.getPastAustriliaHashTag()
#print(pastAustriliaHashTag)
aurinMelbourne=dataProcessing.readAurinMelbourne()
#print(aurinMelbourne)
def readAfterCovidMelbournemood():

    return afterCovidMelbournemood

def readBeforeCovidMelbournemood():

    return beforeCovidMelbournemood

def readAfterCovidAustriliaMood():

    return afterCovidAustriliaMood

def readBeforeCovidAustriliamood():
   return beforeCovidAustriliaMood


def readAfterCovidAustriliaTweetNumber():
    return afterCovidAustriliaTweetNumber

def readBeforeCovidAustriliaTweetNumber():
    return beforeCovidAustriliaTweetNumber

def readAfterCovidMelbourneTweetNumber():
    return afterCovidMelbourneTweetNumber

def readBeforeCovidMelbourneTweetNumber():
    return beforeCovidMelbourneTweetNumber

def getComparingAustriliaHappiness():
    return comparingAustriliaHappiness

def getComparingAustriliaTweetNumber():
    return comparingAustriliaTweetNumber

def getNowAustriliaHashTag():
    return nowAustriliaHashTag

def getPastAustriliaHashTag():
    return pastAustriliaHashTag

def readAurinMelbourne():
    return aurinMelbourne