from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

def test():
    print(SKULocations['OzAuEagRan']['StJP']['URL'])
    print(SKULocations['OzAuEagRan']['StJP']['Quantity']['1-9'])

def scrape():
    for item in SKULocations:
        for company in item:
            for key in company:
                if SKULocations[item][company][key] == 'URL': print('selenium access URL')
                if SKULocations[item][company][key] == 'Quantity': print('Have selenium access the data')