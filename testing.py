import time, datetime, ezgmail
from SKUcost import SKUcost
from main import *

'DEPRICATED'
# def scrapeTest(quantityTest):
#     testNums = 1
#     passing = 0
#     failing = 0
#     while quantityTest > 0:
#         time.sleep(1)
#         print('test ' + str(testNums))
#         scrape()
#         quantityTest -= 1
#         testNums += 1
#         passTest = True
#         print(testParams)
#         for test in testParams:
#             if len(test) == 0:
#                 passTest = False
#         if passTest == 1:
#             passing += 1
#             print('test passed')
#         else: 
#             failing += 1
#             print('test failed')
#         print('-' * 10)
#         time.sleep(1)
#     print('Passing Tests =' + str(passing))
#     print('Failing Tests =' + str(failing))

# def costTest (testgroup):
#     for item in SKUcost:
#         for company in SKUcost[item]:
#             if company == testgroup:
#                 print(item)
#                 print(SKUcost[item][company])
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