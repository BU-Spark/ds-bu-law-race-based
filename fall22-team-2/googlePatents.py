# -*- coding: euc-kr -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import sys
import io
import codecs


# url = "https://patents.google.com/patent/US6451348B1/en?oq=US6451348"
# r = requests.get(url)
# # put r.text into a file
# with open("googlePatent.html", "w") as f:
#     f.write(r.text)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

df = pd.read_csv("inventors_filtered_by_cn_kr.csv")
df2 = df[['inventor_country_code', 'pat_no']]
# remove duplicate pat_no in df2
df2 = df2.drop_duplicates(subset=['pat_no'])
count = 0
baseurl = "https://patents.google.com/patent/##PLACEHOLDER##/en?oq=##PLACEHOLDER##"


for patNo in df2['pat_no']: 
    patNo = "US" + patNo
    print("patNo: ", patNo)
    count += 1   
    # replace ##PLACEHOLDER## with patNo
    url = baseurl.replace("##PLACEHOLDER##", patNo)
    soup = BeautifulSoup(open("googlePatent.html"), "html.parser")
    documentId = soup.find_all("span", itemprop="documentId")
    for d in documentId:
        if "KR" in d.text:
            new = d.text.split("/")[1]
            newUrl = url.replace(patNo, new, 1)
            r = requests.get(newUrl)
            soup = BeautifulSoup(r.text, "html.parser")
            # find all occurrences of <dd itemprop="inventor" in the html
            inventors = soup.find_all("dd", itemprop="inventor")
            # f2 = open('test.txt', 'a')
            for inventor in inventors:
                # print(inventor.text)
                print(inventor.text.encode('utf-8'))
                # f2.write(inventor.text + "\n")
            # f2.close()
            break
    print("-----")
    if count == 3:
        break