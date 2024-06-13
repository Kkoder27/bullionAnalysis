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
            time.sleep(5)
            continue
        break
    time.sleep(5)
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
    for item in SKULocations:
            for company in SKULocations[item]:
                if company == 'JMBullion':
                    continue
                else:
                #if company == 'StJP':
                    seleniumAction(item, company)
                    return