import re
import os
from chardet import detect

#-------------------------------------------DATA IMPORTING--------------------------------------------------------------
#provide your own file path
# filename = './Downloads/Contacts-2021-05-25.vcf'

def datagrabbing(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    data = rawdata.decode('utf-8')
    data1 = data.split('END:VCARD')

    #-------------------------------------------DATA STORED SUCESSFULL------------------------------------------------------

    #-------------------------------------------ENCODING CONVERT------------------------------------------------------------

    '''
        COZ NOW A DAYS PEOPLE ARE USE EMOJI BEHIND THEIR FAVOURITE PERSON NAME
        SO WE NEED TO CONVERT ASCII TO UTF8 AND THN AFTER ISO-8859-7 WHICH CAN EXTRACT NAME
        NOT A EMOJI...... COZ EMOJI MAKE A TROUBLE IN SAVING CSV FILE SO I REMOVE THAT HERE.
    '''
    phone_book = []

    for i in range(len(data1)):
        data2 = data1[i]
        # print(i)
        try:
            fname = re.findall('FN.*', data2)
            ffname = fname[0].strip('FN:')
            if ffname.startswith(';'):
                charset = ffname.strip(';CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:')
                b = quopri.decodestring(str(charset))
                final_name = b.decode('ISO-8859-7')
            else:
                final_name = (fname[0].strip('FN:')).strip('\r')
        except Exception as e:
            # print('fname is empty', e)
            pass
        try:
            no = re.findall('TEL;CELL:.*', data2)
            if len(no) == 0:
                no = re.findall('TEL;CELL;PREF.*', data2)
                final_no = no[0].strip('TEL;CELL;PREF:')
            else:
                final_no = (no[0].strip('TEL;CELL:')).strip('\r')
        except:
            # print("no ki ma ka bharosha")
            pass

        phone_book.append((final_name, final_no))


    final_phone_book=[]
    for i in range(len(phone_book)):
        if len(phone_book[i][1]) >= 12:
            no = str(phone_book[i][1])
            no = no[3:]
        else:
            no = phone_book[i][1]
        if phone_book[i][0][0].isdigit():
            name = phone_book[i][0]
            name = name[2:7]
        else:
            name = phone_book[i][0]
        final_phone_book.append((name, no))
    return final_phone_book