#BULLION ANALYSIS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, re

from SKUref import SKULocations
from SKUcost import SKUcost


def seleniumAction(searchURL, loc1, loc2, loc3, loc4):
    global testParams 
    testParams = [] #ALPHA
    driver = webdriver.Chrome()
    driver.get(searchURL)
    time.sleep(5)
    locList = [loc1, loc2, loc3, loc4]
    for value in locList:
        cost = driver.find_element(By.XPATH, value).text
        testParams.append(cost)
    driver.close()

def scrape():
    for item in SKULocations:
            for company in SKULocations[item]:
                    searchURL = SKULocations[item][company]['URL']
                    searchQuantity1 = SKULocations[item][company]['Quantity']['1-9']
                    searchQuantity2 = SKULocations[item][company]['Quantity']['10-19']
                    searchQuantity3 = SKULocations[item][company]['Quantity']['20-49']
                    searchQuantity4 = SKULocations[item][company]['Quantity']['50+']
                    seleniumAction(searchURL, searchQuantity1, searchQuantity2, searchQuantity3, searchQuantity4)
                    SKUcost[item][company]['Cost']['1-9'] = testParams[0]
                    SKUcost[item][company]['Cost']['10-19'] = testParams[1]
                    SKUcost[item][company]['Cost']['20-49'] = testParams[2]
                    SKUcost[item][company]['Cost']['50+'] = testParams[3]

def scrapeTest(quantityTest):
    testNums = 1
    passing = 0
    failing = 0
    while quantityTest > 0:
        time.sleep(1)
        print('test ' + str(testNums))
        scrape()
        quantityTest -= 1
        testNums += 1
        passTest = True
        print(testParams)
        for test in testParams:
            if len(test) == 0:
                passTest = False
        if passTest == 1:
            passing += 1
            print('test passed')
        else: 
            failing += 1
            print('test failed')
        print('-' * 10)
        time.sleep(1)
    print('Passing Tests =' + str(passing))
    print('Failing Tests =' + str(failing))