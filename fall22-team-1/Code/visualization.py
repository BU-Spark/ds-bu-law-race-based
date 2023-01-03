import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

input_path = './Prediction'
output_path = './img'

df = pd.read_csv(input_path+'/Nov_22_CN_Names_Gender_CN_EN.csv')

# print(df.columns)

def eng_gen(x):
    if x == 'mostly_male':
        return 'male'
    elif x == 'mostly_female':
        return 'female'
    return x

def cn_gen(x):
    if x == 'M=F=Undefined':
        return 'unknown'
    elif x == 'M':
        return 'male'
    elif x == 'F':
        return 'female'
    return 

df['english_gender'] = df['english_gender'].apply(eng_gen)
df['chinese_gender'] = df['chinese_gender'].apply(cn_gen)

gbyears = df.groupby(['year'])
female_percent = {}
female_count = {}
color_map = {'male' : 'lightcoral', 'female' : 'cornflowerblue', 'andy' : 'palegreen', 'unknown' : 'thistle'}
for y, data in gbyears:
    EN_gen = data['english_gender'].value_counts()
    CN_gen = data['chinese_gender'].value_counts()
    # print(y)
    # print(EN_gen)
    # print(CN_gen.sum())
    # print(EN_gen.keys())
    female_percent[y] = CN_gen.get('female') * 1.0 / CN_gen.sum()
    title = 'Gender Distribution'
    fig = plt.figure(title, figsize=(8, 7))
    ax = fig.add_subplot(121)
    ax.set_title('English Name', y=1.2)
    ax.pie(x=EN_gen.values, labels=EN_gen.keys(), autopct='%1.1f%%', colors=EN_gen.keys().map(color_map), shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
    ax = fig.add_subplot(122)
    ax.set_title('Chinese Name', y=1.2)
    ax.pie(x=CN_gen.values, labels=CN_gen.keys(), autopct='%1.1f%%', colors=CN_gen.keys().map(color_map),shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
    plt.savefig(output_path+'/CN'+str(y)+'.png')
    plt.close()

EN_gen = df['english_gender'].value_counts()
CN_gen = df['chinese_gender'].value_counts()
title = 'Gender Distribution'
fig = plt.figure(title, figsize=(8, 7))
ax = fig.add_subplot(121)
ax.set_title('English Name', y=1.2)
ax.pie(x=EN_gen.values, labels=EN_gen.keys(), autopct='%1.1f%%', colors=EN_gen.keys().map(color_map), shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
ax = fig.add_subplot(122)
ax.set_title('Chinese Name', y=1.2)
ax.pie(x=CN_gen.values, labels=CN_gen.keys(), autopct='%1.1f%%', colors=CN_gen.keys().map(color_map),shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
plt.savefig(output_path+'/CN_total.png')
plt.close()

title = 'The percentage of female inventors from 2017 to 2021'
fig = plt.figure(title, figsize=(8, 7))
ax1 = fig.add_subplot(111)
x = female_percent.keys()
y = female_percent.values()
ax1.plot(x, y, 'g-')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_xlabel('Year')
ax1.set_ylabel('Percentage of female inventors')
for a, b in zip(x, y):
    t = round(b, 4)
    ax1.text(a, b, t, ha='center', va='bottom')
plt.savefig(output_path+'/CN.png')
plt.close()


df = pd.read_csv(input_path+'/Nov_22_KR_Names_Gender_EN_KR.csv')

# print(df.columns)

df['english_gender'] = df['english_gender'].apply(eng_gen)

gbyears = df.groupby(['year'])
female_percent = {}
female_count = {}
for y, data in gbyears:
    EN_gen = data['english_gender'].value_counts()
    KR_gen = data['korean_likelyGender'].value_counts()

    female_percent[y] = KR_gen.get('female') * 1.0 / KR_gen.sum()
    title = 'Gender Distribution'
    fig = plt.figure(title, figsize=(8, 7))
    ax = fig.add_subplot(121)
    ax.set_title('English Name', y=1.2)
    ax.pie(x=EN_gen.values, labels=EN_gen.keys(), autopct='%1.1f%%', colors=EN_gen.keys().map(color_map), shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
    ax = fig.add_subplot(122)
    ax.set_title('Korean Name', y=1.2)
    ax.pie(x=KR_gen.values, labels=KR_gen.keys(), autopct='%1.1f%%', colors=KR_gen.keys().map(color_map), shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
    plt.savefig(output_path+'/KR'+str(y)+'.png')
    plt.close()

EN_gen = df['english_gender'].value_counts()
KR_gen = df['korean_likelyGender'].value_counts()
title = 'Gender Distribution'
fig = plt.figure(title, figsize=(8, 7))
ax = fig.add_subplot(121)
ax.set_title('English Name', y=1.2)
ax.pie(x=EN_gen.values, labels=EN_gen.keys(), autopct='%1.1f%%', colors=EN_gen.keys().map(color_map), shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
ax = fig.add_subplot(122)
ax.set_title('Korean Name', y=1.2)
ax.pie(x=KR_gen.values, labels=KR_gen.keys(), autopct='%1.1f%%', colors=KR_gen.keys().map(color_map),shadow=False, pctdistance=1.3, labeldistance=1.5, startangle=90)
plt.savefig(output_path+'/KR_total.png')

title = 'The percentage of female inventors from 2017 to 2021'
fig = plt.figure(title, figsize=(8, 7))
ax1 = fig.add_subplot(111)
x = female_percent.keys()
y = female_percent.values()
ax1.plot(x, y, 'g-')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_xlabel('Year')
ax1.set_ylabel('Percentage of female inventors')
for a, b in zip(x, y):
    t = round(b, 4)
    ax1.text(a, b, t, ha='center', va='bottom')
plt.savefig(output_path+'/KR.png')
