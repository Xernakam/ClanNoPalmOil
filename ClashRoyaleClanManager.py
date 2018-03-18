import requests
import json
import pandas as pd
import xlsxwriter
import csv
myKey= 'b0cab65a56f141d28fb04a4ee29aa8f10230573afbb149f3a6bbf160a68de0a7'
player=['8RLVV20PY']
url='https://api.royaleapi.com/player/'+player[0]
urlclan='https://api.royaleapi.com/clan/2GRV8JVY'
#writer = csv.writer(open("output3.csv", "w"))

#downloading API as .json
headers = {
    'auth': myKey
}
response = requests.request('GET', url, headers=headers)
responseclan  = requests.request('GET', urlclan, headers=headers)

dataclan=responseclan.json()
data = response.json()

dataclan_pd =  pd.DataFrame(list(dataclan.items()))
dataclan_pd.columns = ['field', 'values']

listclan_fields_2_keep = ['members']

clan_2_keep=dataclan_pd[dataclan_pd['field'].isin(listclan_fields_2_keep)][['values']].values.item()

newsubsetclan = pd.DataFrame()
for i in range(1,len(clan_2_keep)):
    subsetclan = pd.DataFrame(list(clan_2_keep[i].items()))
    subsetclan.columns = ['field', 'values']
    newsubsetclan = newsubsetclan.append(subsetclan, ignore_index=True)

clanfields_2_keep=['tag']
clanfinal=newsubsetclan[newsubsetclan['field'].isin(clanfields_2_keep)]['values'].values

print (clanfinal)


#creating dataframe structure
data_pd =  pd.DataFrame(list(data.items()))
data_pd.columns = ['field', 'values']

list_fields_2_keep = ['name','trophies','tag']

keep_as_are = data_pd[data_pd['field'].isin(list_fields_2_keep)]
keep_as_are['from'] = pd.Series('parent',index=keep_as_are.index)
newsubset = keep_as_are

list_fields_2_change = ['clan','stats']
for i in list_fields_2_change:
    dict_2_tf = data_pd[data_pd['field']== i][['values']].values.item()
    subset = pd.DataFrame(list(dict_2_tf.items()))
    subset.columns = ['field', 'values']
    subset['from'] = pd.Series(i,index=subset.index)
    newsubset=newsubset.append(subset,ignore_index=True)

fields_2_keep = ['name', 'trophies','donations','donationsReceived', 'donationsDelta','totalDonations', 'level']
finalkeep = newsubset[newsubset['field'].isin(fields_2_keep)]

print(finalkeep)
