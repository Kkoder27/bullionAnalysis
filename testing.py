import time
from main import testParams, scrape
from SKUcost import SKUcost
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

def costTest (testgroup):
    for item in SKUcost:
        for company in SKUcost[item]:
            if company == testgroup:
                print(item)
                print(SKUcost[item][company])