# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium import webdriver
import pandas as pd
# from pathlib import Path
# from openpyxl import load_workbook
# from openpyxl import Workbook
# from datetime import datetime, timedelta
# import numpy as np
import os
import os.path
from os import path
# from os import listdir
# from os.path import isfile, join
# import re
# import natsort 
import requests



# path='D:/Code/Delexi/playphrase-oxford-5000/'
list_subfolders_with_paths=[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]

# list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]

check_vocab_name=[]
apiHeaders = [{ 'Authorization' : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE2MTEwNjQzNjE4MjgsInVwZGF0ZWRBdCI6MTYzNjY2OTkzNzU4OSwiaWQiOiI2MDA2ZTQyOWNjYTFhNjdkMmJmZmRlMWEiLCJpbWdzIjoiZXlKaGJHY2lPaUpJVXpJMU5pSjkuT0Mwek55MHhNQS4xTE03c3JDZDNnWTR6Mm9ZS3N0eTF0aXJsbzNWM3c1RktpdGs5SnJFUExvLTI2LTEwLTIwMjEtOC0zNy0xMC04MjUucHJvZmlsZWltYWdlIiwiaW1nc0V4dGVudGlvbiI6IiIsIm5hbWUiOiJNb2hzZW4iLCJsZWFybkVuZ2xpc2giOiJFZHVjYXRpb24iLCJlZHVjYXRpb24iOiJNU0MiLCJnZW5kZXIiOiJtYWxlIiwidHlwZSI6MiwicGhvbmVOdW1iZXIiOjkxMjc5NjkxMzAsImRlbGV0ZWQiOmZhbHNlLCJhY3RpdmUiOmZhbHNlLCJ2ZXJpZmljYXRpb25Db2RlIjo3MjgyLCJ2ZXJpZmljYXRpb25FeHBpcmVEYXRlIjp7Il9pc0FNb21lbnRPYmplY3QiOnRydWUsIl9pIjoiMjAyMS0wNy0xNlQwNzowODo0OS44MDdaIiwiX2lzVVRDIjpmYWxzZSwiX3BmIjp7ImVtcHR5IjpmYWxzZSwidW51c2VkVG9rZW5zIjpbXSwidW51c2VkSW5wdXQiOltdLCJvdmVyZmxvdyI6LTIsImNoYXJzTGVmdE92ZXIiOjAsIm51bGxJbnB1dCI6ZmFsc2UsImludmFsaWRFcmEiOm51bGwsImludmFsaWRNb250aCI6bnVsbCwiaW52YWxpZEZvcm1hdCI6ZmFsc2UsInVzZXJJbnZhbGlkYXRlZCI6ZmFsc2UsImlzbyI6ZmFsc2UsInBhcnNlZERhdGVQYXJ0cyI6W10sImVyYSI6bnVsbCwibWVyaWRpZW0iOm51bGwsInJmYzI4MjIiOmZhbHNlLCJ3ZWVrZGF5TWlzbWF0Y2giOmZhbHNlfSwiX2xvY2FsZSI6eyJfY2FsZW5kYXIiOnsic2FtZURheSI6IltUb2RheSBhdF0gTFQiLCJuZXh0RGF5IjoiW1RvbW9ycm93IGF0XSBMVCIsIm5leHRXZWVrIjoiZGRkZCBbYXRdIExUIiwibGFzdERheSI6IltZZXN0ZXJkYXkgYXRdIExUIiwibGFzdFdlZWsiOiJbTGFzdF0gZGRkZCBbYXRdIExUIiwic2FtZUVsc2UiOiJMIn0sIl9sb25nRGF0ZUZvcm1hdCI6eyJMVFMiOiJoOm1tOnNzIEEiLCJMVCI6Img6bW0gQSIsIkwiOiJNTS9ERC9ZWVlZIiwiTEwiOiJNTU1NIEQsIFlZWVkiLCJMTEwiOiJNTU1NIEQsIFlZWVkgaDptbSBBIiwiTExMTCI6ImRkZGQsIE1NTU0gRCwgWVlZWSBoOm1tIEEifSwiX2ludmFsaWREYXRlIjoiSW52YWxpZCBkYXRlIiwiX2RheU9mTW9udGhPcmRpbmFsUGFyc2UiOnt9LCJfcmVsYXRpdmVUaW1lIjp7ImZ1dHVyZSI6ImluICVzIiwicGFzdCI6IiVzIGFnbyIsInMiOiJhIGZldyBzZWNvbmRzIiwic3MiOiIlZCBzZWNvbmRzIiwibSI6ImEgbWludXRlIiwibW0iOiIlZCBtaW51dGVzIiwiaCI6ImFuIGhvdXIiLCJoaCI6IiVkIGhvdXJzIiwiZCI6ImEgZGF5IiwiZGQiOiIlZCBkYXlzIiwidyI6ImEgd2VlayIsInd3IjoiJWQgd2Vla3MiLCJNIjoiYSBtb250aCIsIk1NIjoiJWQgbW9udGhzIiwieSI6ImEgeWVhciIsInl5IjoiJWQgeWVhcnMifSwiX21vbnRocyI6WyJKYW51YXJ5IiwiRmVicnVhcnkiLCJNYXJjaCIsIkFwcmlsIiwiTWF5IiwiSnVuZSIsIkp1bHkiLCJBdWd1c3QiLCJTZXB0ZW1iZXIiLCJPY3RvYmVyIiwiTm92ZW1iZXIiLCJEZWNlbWJlciJdLCJfbW9udGhzU2hvcnQiOlsiSmFuIiwiRmViIiwiTWFyIiwiQXByIiwiTWF5IiwiSnVuIiwiSnVsIiwiQXVnIiwiU2VwIiwiT2N0IiwiTm92IiwiRGVjIl0sIl93ZWVrIjp7ImRvdyI6MCwiZG95Ijo2fSwiX3dlZWtkYXlzIjpbIlN1bmRheSIsIk1vbmRheSIsIlR1ZXNkYXkiLCJXZWRuZXNkYXkiLCJUaHVyc2RheSIsIkZyaWRheSIsIlNhdHVyZGF5Il0sIl93ZWVrZGF5c01pbiI6WyJTdSIsIk1vIiwiVHUiLCJXZSIsIlRoIiwiRnIiLCJTYSJdLCJfd2Vla2RheXNTaG9ydCI6WyJTdW4iLCJNb24iLCJUdWUiLCJXZWQiLCJUaHUiLCJGcmkiLCJTYXQiXSwiX21lcmlkaWVtUGFyc2UiOnt9LCJfZXJhcyI6W3sic2luY2UiOiIwMDAxLTAxLTAxIiwidW50aWwiOm51bGwsIm9mZnNldCI6MSwibmFtZSI6IkFubm8gRG9taW5pIiwibmFycm93IjoiQUQiLCJhYmJyIjoiQUQifSx7InNpbmNlIjoiMDAwMC0xMi0zMSIsInVudGlsIjpudWxsLCJvZmZzZXQiOjEsIm5hbWUiOiJCZWZvcmUgQ2hyaXN0IiwibmFycm93IjoiQkMiLCJhYmJyIjoiQkMifV0sIl9hYmJyIjoiZW4iLCJfY29uZmlnIjp7ImNhbGVuZGFyIjp7InNhbWVEYXkiOiJbVG9kYXkgYXRdIExUIiwibmV4dERheSI6IltUb21vcnJvdyBhdF0gTFQiLCJuZXh0V2VlayI6ImRkZGQgW2F0XSBMVCIsImxhc3REYXkiOiJbWWVzdGVyZGF5IGF0XSBMVCIsImxhc3RXZWVrIjoiW0xhc3RdIGRkZGQgW2F0XSBMVCIsInNhbWVFbHNlIjoiTCJ9LCJsb25nRGF0ZUZvcm1hdCI6eyJMVFMiOiJoOm1tOnNzIEEiLCJMVCI6Img6bW0gQSIsIkwiOiJNTS9ERC9ZWVlZIiwiTEwiOiJNTU1NIEQsIFlZWVkiLCJMTEwiOiJNTU1NIEQsIFlZWVkgaDptbSBBIiwiTExMTCI6ImRkZGQsIE1NTU0gRCwgWVlZWSBoOm1tIEEifSwiaW52YWxpZERhdGUiOiJJbnZhbGlkIGRhdGUiLCJkYXlPZk1vbnRoT3JkaW5hbFBhcnNlIjp7fSwicmVsYXRpdmVUaW1lIjp7ImZ1dHVyZSI6ImluICVzIiwicGFzdCI6IiVzIGFnbyIsInMiOiJhIGZldyBzZWNvbmRzIiwic3MiOiIlZCBzZWNvbmRzIiwibSI6ImEgbWludXRlIiwibW0iOiIlZCBtaW51dGVzIiwiaCI6ImFuIGhvdXIiLCJoaCI6IiVkIGhvdXJzIiwiZCI6ImEgZGF5IiwiZGQiOiIlZCBkYXlzIiwidyI6ImEgd2VlayIsInd3IjoiJWQgd2Vla3MiLCJNIjoiYSBtb250aCIsIk1NIjoiJWQgbW9udGhzIiwieSI6ImEgeWVhciIsInl5IjoiJWQgeWVhcnMifSwibW9udGhzIjpbIkphbnVhcnkiLCJGZWJydWFyeSIsIk1hcmNoIiwiQXByaWwiLCJNYXkiLCJKdW5lIiwiSnVseSIsIkF1Z3VzdCIsIlNlcHRlbWJlciIsIk9jdG9iZXIiLCJOb3ZlbWJlciIsIkRlY2VtYmVyIl0sIm1vbnRoc1Nob3J0IjpbIkphbiIsIkZlYiIsIk1hciIsIkFwciIsIk1heSIsIkp1biIsIkp1bCIsIkF1ZyIsIlNlcCIsIk9jdCIsIk5vdiIsIkRlYyJdLCJ3ZWVrIjp7ImRvdyI6MCwiZG95Ijo2fSwid2Vla2RheXMiOlsiU3VuZGF5IiwiTW9uZGF5IiwiVHVlc2RheSIsIldlZG5lc2RheSIsIlRodXJzZGF5IiwiRnJpZGF5IiwiU2F0dXJkYXkiXSwid2Vla2RheXNNaW4iOlsiU3UiLCJNbyIsIlR1IiwiV2UiLCJUaCIsIkZyIiwiU2EiXSwid2Vla2RheXNTaG9ydCI6WyJTdW4iLCJNb24iLCJUdWUiLCJXZWQiLCJUaHUiLCJGcmkiLCJTYXQiXSwibWVyaWRpZW1QYXJzZSI6e30sImVyYXMiOlt7InNpbmNlIjoiMDAwMS0wMS0wMSIsInVudGlsIjpudWxsLCJvZmZzZXQiOjEsIm5hbWUiOiJBbm5vIERvbWluaSIsIm5hcnJvdyI6IkFEIiwiYWJiciI6IkFEIn0seyJzaW5jZSI6IjAwMDAtMTItMzEiLCJ1bnRpbCI6bnVsbCwib2Zmc2V0IjoxLCJuYW1lIjoiQmVmb3JlIENocmlzdCIsIm5hcnJvdyI6IkJDIiwiYWJiciI6IkJDIn1dLCJhYmJyIjoiZW4ifSwiX2RheU9mTW9udGhPcmRpbmFsUGFyc2VMZW5pZW50Ijp7fX0sIl9kIjoiMjAyMS0wNy0xNlQwNzowODo0OS44MDdaIiwiX2lzVmFsaWQiOnRydWV9LCJ2ZXJpZmllZCI6dHJ1ZSwiZW1haWwiOiJtby5yYWhuYXZhcmRpQGdtYWlsLmNvbSIsImlhdCI6MTYzNzc2NDk4NCwiZXhwIjoxNjQwMzU2OTg0fQ.7vIpjv4rihIJOwckcB4_u3no02K_EEZWdwd758xlbZk" }]
baseUrl='https://www.platform.lexico.ac'

error_list=[]
for folder in list_subfolders_with_paths:
    dataBaseFile=None
    listOfVocabs=None
    ListOfSubtitles=None
    ListOfvideoId=None
    video_files=os.listdir(folder)
    for excel_file in video_files:
        if excel_file.endswith('.xlsx'):
            subtitle_excel_file=folder+'/'+excel_file
    
    
            dataBaseFile = pd.read_excel(subtitle_excel_file)
            listOfVocabs = dataBaseFile['vocab'].values
            ListOfSubtitles = dataBaseFile['subtitle'].values
            ListOfvideoId = dataBaseFile['videoId'].values
    # if counter>1:
    counter =0
    vocab_counter=0



    if ListOfvideoId is not None:

        for video_file in ListOfvideoId:
        #   if video_file.endswith('.mp4'):
            #   if counter<50:
                    # try:


        
                        url = baseUrl +'/api/v1/postVocabVideo?subtitle=' + str(ListOfSubtitles[vocab_counter]) +'&title=' + str(listOfVocabs[vocab_counter])
                        vidoSrcfile=str(listOfVocabs[vocab_counter])+'-'+ str(counter)+'-'+str(ListOfvideoId[vocab_counter])
                        if(os.path.exists(folder+'/'+ str(vidoSrcfile))):

   
                            myfile = {'file': ( str(vidoSrcfile), open(folder+'/'+ str(vidoSrcfile) ,'rb'), 'video/mp4')}
                            x = requests.post(url, files = myfile, headers =apiHeaders[0])

                            # print(x.status_code, x.reason)
                            # print(listOfVocabs[vocab_counter])
                            # print(vocab_counter)
                            vocab_counter=vocab_counter+1
                            counter=counter+1
                        else:
                            error_list.append(vidoSrcfile)
                            print(str(vidoSrcfile),'dosent exist')
                            vocab_counter=vocab_counter+1
                            counter=counter+1
                    # except:
                        # error_list.append(vidoSrcfile)

                        # vocab_counter=vocab_counter+1
                        # counter=counter+1
                        # print(listOfVocabs[vocab_counter],'Errrrrrrrrrrrrror')
                        # print(vocab_counter,'Errrrrrrrrror')

                    # print(x.text)
                   
print(len(error_list),'finish')

    # counter=counter+1