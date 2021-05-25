import requests
from bs4 import BeautifulSoup
import csv
import ast
import re
import os
import phone_no
#-------------------------------GETTING URL AND TRY TO GET REQUEST ON SERVER SIDE-----------------------------------------
def prasingurl(fkid):
    url = 'https://slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion.ly'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.text
    if title == "Darknet TOR / I2P Proxy and Gateway":
        print("Tata bye bye khatam good bye finish")
        pass
    else:
#         fkid=input("Enter Your Phone or Email: ")
        headers={"content-type":"text"}
        print(headers)
        res = requests.get('https://slf2rrahypck3bwckpdohsnhpeqrb3nhvwznjmarmweofwnptowe4mad.onion.ly/api/search/'+fkid)
        data = (res.text)
        data = ast.literal_eval(str(data))
    return data
#-------------------------------AFTER GETTING DATA OF WEBSITE, DATA PRASING AND SAVE IN CSV FILE--------------------------
def createdata(phone, name):
    phone = str(phone)
    data = prasingurl(phone)
    try:
        linked_mobiles = data['db_data']['linked_mobiles'][0]
    except:
        linked_mobiles = data['search_str']
    try:
        linked_emails = data['db_data']['linked_emails'][0]
    except:
        linked_emails = ""
    try:
        total_num_orders = data['db_data']['total_num_orders']
    except:
        total_num_orders = ""
    try:
        total_price_spent = data['db_data']['total_price_spent']
    except:
        total_price_spent = ""


    with open('dominos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, linked_mobiles,linked_emails.encode('utf-8'),total_num_orders,total_price_spent])
    return

#-------------------------------PASSING PHONE NO AND TRYING TO GET DATA FROM WEBSITE--------------------------------------


#-------------------------------BUT FOR THAT WE NEED TO CREATE DATASET OF PHONENO-----------------------------------------
''' IF YOU ARE TRYING TO GET DATA OF YOUR EVERY PHONE USER THEN EXPORT CSV FILE OF YOUR PHONE NO
    AND THEN AFTER WITH HELP OF PYTHON LIB WE EXRACT NAME AND PHONE NO

    OKK SO LETS DO THAT FIRST, AND PASS THAT PHONE NO AS THE INPUT OF THE FUNCTION
'''
#-------------------------------GRABBING PHONE NO FROM .VSF FILE----------------------------------------------------------

filename = 'Contacts-2021-05-25.vcf'
phoneno = phone_no.datagrabbing(filename)
print(phoneno) #for checking you phone no are correctly imported or not


#-------------------------------EXTRACTING PHONE NO PROVIDE AT THE DOMINOS SITE AS INPUT-----------------------------------------
resultlist = 0
for i in range(len(phoneno)):
    phone = phoneno[i][1]
    name = phoneno[i][0]
    itter = 0
    while True:
        try:
            print(f"{itter} times trying {phone}")
            createdata(phone,name)
        except (SyntaxError, TypeError, ValueError):
            print("Site not reloading")
            itter += 1
        except (ConnectionError, OSError):
            print('Server is down')
            itter += 1
        else:
            break
        finally:
            resultlist += 1
            print(f'after {itter} time trying, finally result get')

print(resultlist)
