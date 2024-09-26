import time, datetime, ezgmail
from SKUcost import SKUcost
from main import *

def costTestResult (testgroup):
    for item in SKUcost:
        if item == testgroup:
            print(item)
            for company in SKUcost[item]:
                print(company)
                print(SKUcost[item][company])
        else: 
            for company in SKUcost[item]:
                if company == testgroup:
                    print(item)
                    print(SKUcost[item][company])

def chunkTest(number): #test mailchunk n times
    for value in range(number):
        now = datetime.datetime.now()
        print('TEST ' + str(value))
        print('Tested at ' + now.strftime('%H'))
        mailChunk()
        time.sleep(3600)

def singleMailTest(number):
    for value in range(number):
        testNo = 'test ' + str(value)
        ezgmail.send('brunswickkm7@gmail.com', testNo, 'this is test number ' + str(value))
        time.sleep(900)

def companyScrapeTest(testgroup):
    for item in SKULocations:
            for company in SKULocations[item]:
                if company == testgroup:
                    seleniumAction(item,company)
    costTestResult(testgroup)