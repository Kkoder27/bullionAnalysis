import pandas as pd
from SKUcost import SKUcost
import datetime
from SKUKey import SKUkey

def costAssembly():
    itemList = []
    now = datetime.datetime.now()
    timeStamp =  now.strftime('%y') + now.strftime('%m') + now.strftime('%d') + now.strftime('%H') + now.strftime('%M') + now.strftime('%S')
    fileName = 'BullionScrape' + timeStamp + '.xlsx'
    writefile = 'w'
    for key in SKUcost:
        itemList.append(key)
    for item in itemList:
        sheetName = SKUkey[item]
        activeDF = pd.DataFrame()
        activeDF['Quantity'] = ['1-9', '10-19', '20-49', '50+']
        for company in SKUcost[item]:
            if company == 'JMBullion':
                continue
            activeDF[company] = SKUcost[item][company]['Cost'].values()
        with pd.ExcelWriter(fileName, mode=writefile, engine='openpyxl') as writer:
            activeDF.to_excel(writer, sheet_name=sheetName, index=False)
            writefile = 'a'
    return fileName