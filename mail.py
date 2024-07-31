import ezgmail, datetime

mailList = [
    'brunswickKM7@gmail.com'
]

def mailMain(address, file): #serves to mail out the bullionanalysis to mailing list
    now = datetime.datetime.now()
    timeStamp = now.strftime('%d/%m/%y')
    subject = 'Bullion Price Scrape ' + timeStamp
    body = 'Attached you will find relevant price scrapings from the morning of ' + timeStamp
    #'''\n Improvement for this system is constantly ongoing; please submit any ideas for improvement, comments, criticism, or otherwise to this email with a subjectline preceded by "!'''
    ezgmail.send(address, subject, body, file)

def mailCheck(): #checks mail for commands sent
    pass 