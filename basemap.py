import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
 
df_year = pd.read_csv('TM.csv')
states_TM = df_year['STATE/UT'].tolist()
acc_cnt = df_year['TOTAL'].tolist()
df_time = pd.read_csv('TTY.csv')
type = df_year['TYPE'].tolist()
total_counts = df_year['TOTAL'].tolist()
list_acc = []
states = df_time['SU'].tolist()
a_states = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh',
            'Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradhesh','Maharashtra','Manipur','Meghalaya',
            'Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh','Uttarakhand'
             'West Bengal','A & N Islands','Chandigarh','D & N Haveli','Daman & Diu','Delhi (Ut)','Lakshadweep','Puducherry']
#--------------------------------------------------------------------------------------------------------------
def states_avgAcc():
    indexes = []
    for si in range(0,len(a_states)):
        tot = 0
        for i in range(0,len(states_TM)):
            if a_states[si] == states_TM[i]:
                tot += acc_cnt[i]
        list_acc.append(tot)

    for si in range(0, len(a_states)):
        indexes.append(si)

    #s= plt.subplot(111)
    #num_items = len(a_states)
    #ind = np.arange(num_items)
    plt.bar(indexes,list_acc,width=0.8)
    #s.set_xticks(ind + 10)
    plt.xticks(indexes,a_states)
    plt.xticks(indexes,a_states)
    plt.xlabel('States')
    plt.ylabel('Total Accidents')
    plt.show()
#--------------------------------------------------------------------------------------------------------------
N1 = df_time['1N'].tolist()
N2 = df_time['2N'].tolist()
N3 = df_time['3N'].tolist()
N4 = df_time['4N'].tolist()
N5 = df_time['5N'].tolist()
N6 = df_time['6N'].tolist()
N7 = df_time['7N'].tolist()
N8 = df_time['8N'].tolist()
#----------------------------------------------------------------------------------------------------------------
#pie plot for time per state
def state_time_pie(statename):

    cnt_n1 = 0
    cnt_n2 = 0
    cnt_n3 = 0
    cnt_n4 = 0
    cnt_n5 = 0
    cnt_n6 = 0
    cnt_n7 = 0
    cnt_n8 = 0


    for i in range(0,len(states)):
        if statename == states[i]:
            cnt_n1 += N1[i]
            cnt_n2 += N2[i]
            cnt_n3 += N3[i]
            cnt_n4 += N4[i]
            cnt_n5 += N5[i]
            cnt_n6 += N6[i]
            cnt_n7 += N7[i]
            cnt_n8 += N8[i]
    count_list = [cnt_n1,cnt_n2,cnt_n3,cnt_n4,cnt_n5,cnt_n6,cnt_n7,cnt_n8]
    label_time_periods = ['0-3hrs','3-6hrs','6-9hrs','9-12hrs','12-15hrs','15-18hrs','18-21hrs','21-24hrs']
    plt.pie(count_list,labels=label_time_periods,autopct='%1.1f%%',shadow=True)
    plt.show()

#----------------------------------------------------------------------------------------------------------------
#pie plot for type of accidents
cnt_Rail = int(0)
cnt_Road = int(0)
cnt_other = int(0)
for i in range(0,len(type)):
    if type[i] == 'Road Accidents':
        cnt_Road = cnt_Road + total_counts[i]
    elif type[i] == 'Other Railway Accidents':
        cnt_other = cnt_other + total_counts[i]
    else:
        cnt_Rail = cnt_Rail  + total_counts[i]

print(cnt_other,' ',cnt_Road,' ',cnt_Rail)
cnt_list = []
cnt_list.append(cnt_Road)
cnt_list.append(cnt_Rail)
cnt_list.append(cnt_other)
list_types = ['ROAD','RAILWAY','OTHER-RAILWAY']
co = ['g','r','c']
plt.pie(cnt_list,labels=list_types,colors=co,startangle=90,shadow=True,explode=(0,0.1,0.3),autopct='%1.1f%%')
plt.show()
#----------------------------------------------------------------------------------------------------------------
state_time_pie('Andhra Pradesh')
states_avgAcc()


m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='h')
m.drawcoastlines()
m.fillcontinents()
m.drawmapboundary()
plt.title("Quick Basemap Example!")
plt.show()




