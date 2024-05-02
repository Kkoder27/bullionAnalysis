from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#reference dictionary
SKULocations = {
    'OzAuEagRan' : {
          'StJP' : {
              'URL' : 'https://www.stjosephpartners.com/item/1-oz-american-gold-eagle/1EAGLE',
              'Quantity': {
                  '1-9' : '/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[2]',
                  '10-19' : '/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div[2]/div/div/table/tbody/tr[3]/td[2]',
                  '20-49' : '/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div[2]/div/div/table/tbody/tr[4]/td[2]',
                  '50+' : '/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div[2]/div/div/table/tbody/tr[5]/td[2]'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzAuEagCur' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzAuMapleCur' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzAuPhilCur' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzAuBarCoice' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzArEagCur' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzArMapleCur' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'OzArBuffalo' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        },
    'TenOzArBar' : {
          'StJP' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'APMEX' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'JMBullion': {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
          },
          'SDBullion' : {
              'URL' : 'get',
              'Quantity': {
                  '1-9' : 'pass',
                  '10-19' : 'pass',
                  '20-49' : 'pass',
                  '50+' : 'pass'
                  }
            }
        }
}

def configTest():
    print(SKULocations['OzAuEagRan']['StJP']['URL'])
    print(SKULocations['OzAuEagRan']['StJP']['Quantity']['1-9'])

def seleniumAction(searchURL, loc1, loc2, loc3, loc4):
    testParams = [] #ALPHA
    driver = webdriver.Chrome()
    driver.get(searchURL)
    time.sleep(5)
    locList = [loc1, loc2, loc3, loc4]
    for value in locList:
        cost = driver.find_element(By.XPATH, value).text
        testParams.append(cost)
    print(testParams) #ALPHA
    driver.close()

def scrape():
    for item in SKULocations:
        if item == 'OzAuEagRan':
            for company in SKULocations[item]:
                if company == 'StJP':
                    searchURL = SKULocations[item][company]['URL']
                    searchQuantity1 = SKULocations[item][company]['Quantity']['1-9']
                    searchQuantity2 = SKULocations[item][company]['Quantity']['10-19']
                    searchQuantity3 = SKULocations[item][company]['Quantity']['20-49']
                    searchQuantity4 = SKULocations[item][company]['Quantity']['50+']
                    seleniumAction(searchURL, searchQuantity1, searchQuantity2, searchQuantity3, searchQuantity4)

def scrapeTest(n):
    m = 1
    while n > 0:
        time.sleep(5)
        print('test ' + str(m))
        scrape()
        print('-' * 10)
        n -= 1
        m += 1
        time.sleep(5)