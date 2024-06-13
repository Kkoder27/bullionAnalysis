#BULLION ANALYSIS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, re
import pandas as pd

from SKUref import SKULocations
from SKUcost import SKUcost
from pandasWork import costAssembly


def seleniumAction(searchURL, loc1, loc2, loc3, loc4):
    seleniumOutput = [] #ALPHA
    driver = webdriver.Chrome()
    while True:
        try: driver.get(searchURL)
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
        break
    time.sleep(3)
    locList = [loc1, loc2, loc3, loc4]
    for value in locList:
        cost = 'Out of Stock'
        try: cost = driver.find_element(By.XPATH, value).text
        except NoSuchElementException:
            pass
        seleniumOutput.append(cost)
    driver.close()
    return seleniumOutput

def scrape():
    for item in SKULocations:
            for company in SKULocations[item]:
                if company == 'JMBullion':
                    continue
                else:
                #if company == 'StJP':
                    searchURL = SKULocations[item][company]['URL']
                    searchQuantity1 = SKULocations[item][company]['Quantity']['1-9']
                    searchQuantity2 = SKULocations[item][company]['Quantity']['10-19']
                    searchQuantity3 = SKULocations[item][company]['Quantity']['20-49']
                    searchQuantity4 = SKULocations[item][company]['Quantity']['50+']
                    seleniumOutput = seleniumAction(searchURL, searchQuantity1, searchQuantity2, searchQuantity3, searchQuantity4)
                    SKUcost[item][company]['Cost']['1-9'] = seleniumOutput[0]
                    SKUcost[item][company]['Cost']['10-19'] = seleniumOutput[1]
                    SKUcost[item][company]['Cost']['20-49'] = seleniumOutput[2]
                    SKUcost[item][company]['Cost']['50+'] = seleniumOutput[3]