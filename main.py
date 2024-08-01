#BULLION ANALYSIS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, datetime, threading
import pandas as pd
from SKUref import SKULocations
from SKUcost import SKUcost
from pandasWork import costAssembly
from mail import mailMain, mailList


def seleniumAction(item, company):
    searchParam = SKULocations[item][company]
    seleniumOutput = SKUcost[item][company]['Cost']
    driver = webdriver.Chrome()
    searchURL = searchParam['URL']
    locList = searchParam['Quantity']
    while True:
        try: driver.get(searchURL)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
        break
    time.sleep(3)
    count = 0
    for value in locList.values():
        cost = 'Out of Stock'
        try: cost = driver.find_element(By.XPATH, value).text
        except NoSuchElementException as e:
            print(e)
            pass
        seleniumOutput[list(locList.keys())[count]] = cost
        count += 1
    driver.close()

def scrape():
    #Construct Threading parameters
    threadMax = len(SKULocations['OzAuEagRan'])
    threadArray = []
    threadCount = 0
    startThreads = 0
    while len(threadArray) < threadMax:
        threadArray.append('thread_' + str(threadCount))
        threadCount += 1
    #Scrape Main
    for item in SKULocations:
            for company in SKULocations[item]:

                if company == 'JMBullion':
                    continue
                #startup for threads
                if startThreads < threadMax:
                        threadArray[startThreads] = threading.Thread(target=seleniumAction, args=(item, company))
                        threadArray[startThreads].start()
                        startThreads += 1
                #threading main
                threadFound = False
                while not threadFound and not startThreads < threadMax:
                    for indexValue in range(len(threadArray)):
                        if threadFound: break
                        if not threadArray[indexValue].is_alive():
                            threadArray[indexValue] = threading.Thread(target=seleniumAction, args=(item, company))
                            threadArray[indexValue].start()
                            threadFound = True
                            break
    for indexValue in range(len(threadArray)):
         threadArray[indexValue].join()

def initialize():
    while True:
        now = datetime.datetime.now()
        if int(now.strftime('%H')) == 3:
            scrape()
            sendFile = costAssembly()
            for address in mailList:
                mailMain(address, sendFile)
            time.sleep(3600)
        else: time.sleep(900)