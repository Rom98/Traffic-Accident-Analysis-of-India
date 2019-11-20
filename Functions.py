import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

imgcnt = 1;
safestat = ""
df_year = pd.read_csv('TM.csv')
states_TM = df_year['STATE/UT'].tolist()
acc_cnt = df_year['TOTAL'].tolist()
year_tm = df_year['YEAR'].tolist()
df_time = pd.read_csv('TTY.csv')
acc_type = df_year['TYPE'].tolist()
total_counts = df_year['TOTAL'].tolist()
acc_year = df_time['YEAR'].tolist()
list_acc = []
states = df_time['SU'].tolist()
a_states = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh',
            'Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradhesh','Maharashtra','Manipur','Meghalaya',
            'Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh','Uttarakhand'
             'West Bengal','A & N Islands','Chandigarh','D & N Haveli','Daman & Diu','Delhi (Ut)','Lakshadweep','Puducherry']

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
year_gap = ['2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15']
label_time_periods = ['0-3 HRS','3-6 HRS','6-9 HRS','9-12 HRS','12-15 HRS','15-18 HRS','18-21 HRS','21-24 HRS']
types = ['Roadways', 'Railways', 'Other']
year_list = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
passV = ['669719','723330','989560','1209876','1309300','1545234','1777583','1838593','2357411','2987296','3146069','3233561','3087973','3220172']
commV = ['162508','203697','275040','353703','391083','520000','549006','416870','566608','752735','929136','831744','699035','697083'] 
threeW = ['212748	','276719','356223','374445','434423','556124','500660','497020','619093','799553','879289','839742','830108','949021']
twoW = ['4271327','5076221','5622741','6529829','7608697','8436186','8009292','8395613','10510336','13376451','15427532','15721180','16883049','18499970']
#--------------------------------------------------------------------------------------------------------------
N1 = df_time['1N'].tolist()
N2 = df_time['2N'].tolist()
N3 = df_time['3N'].tolist()
N4 = df_time['4N'].tolist()
N5 = df_time['5N'].tolist()
N6 = df_time['6N'].tolist()
N7 = df_time['7N'].tolist()
N8 = df_time['8N'].tolist()

M1 = df_year['JANUARY'].tolist()
M2 = df_year['FEBRUARY'].tolist()
M3 = df_year['MARCH'].tolist()
M4 = df_year['APRIL'].tolist()
M5 = df_year['MAY'].tolist()
M6 = df_year['JUNE'].tolist()
M7 = df_year['JULY'].tolist()
M8 = df_year['AUGUST'].tolist()
M9 = df_year['SEPTEMBER'].tolist()
M10 = df_year['OCTOBER'].tolist()
M11 = df_year['NOVEMBER'].tolist()
M12 = df_year['DECEMBER'].tolist()
#----------------------------------------------------------------------------------------------------------------
#pie plot for time-slot for given state and year
def state_time_pie(statename, year):
    fig,ax = plt.subplots(figsize=(5,5))
    count_list = [0,0,0,0,0,0,0,0]
    
    if(year == 111):
        for i in range(0,len(states)):
            if (statename == states[i]):
                count_list[0] += N1[i]
                count_list[1] += N2[i]
                count_list[2] += N3[i]
                count_list[3] += N4[i]
                count_list[4] += N5[i]
                count_list[5] += N6[i]
                count_list[6] += N7[i]
                count_list[7] += N8[i]
    
    else:
        for i in range(0,len(states)):
            if (statename == states[i] and year == acc_year[i]):
                count_list[0] += N1[i]
                count_list[1] += N2[i]
                count_list[2] += N3[i]
                count_list[3] += N4[i]
                count_list[4] += N5[i]
                count_list[5] += N6[i]
                count_list[6] += N7[i]
                count_list[7] += N8[i]
            
    plt.pie(count_list,labels=label_time_periods,autopct='%1.1f%%',shadow=True)
    fig.savefig('stp.png')

#---------------------------------------------------------------------------------------------------------------
#pie plot for month for given state and year
def state_month_pie(statename, year):
    fig,ax = plt.subplots(figsize=(5,5))
    clist = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    if (year == 111):
        for i in range(0,len(states_TM)):
            if (statename == states_TM[i]):
                clist[0] += M1[i]
                clist[1] += M2[i]
                clist[2] += M3[i]
                clist[3] += M4[i]
                clist[4] += M5[i]
                clist[5] += M6[i]
                clist[6] += M7[i]
                clist[7] += M8[i]
                clist[8] += M9[i]
                clist[9] += M10[i]
                clist[10] += M11[i]
                clist[11] += M12[i]
    
    else:   
        for i in range(0,len(states_TM)):
            if (statename == states_TM[i] and year == year_tm[i]):
                clist[0] += M1[i]
                clist[1] += M2[i]
                clist[2] += M3[i]
                clist[3] += M4[i]
                clist[4] += M5[i]
                clist[5] += M6[i]
                clist[6] += M7[i]
                clist[7] += M8[i]
                clist[8] += M9[i]
                clist[9] += M10[i]
                clist[10] += M11[i]
                clist[11] += M12[i]
    
    plt.pie(clist,labels=months,autopct='%1.1f%%',shadow=True)
    fig.savefig('smp.png')
    
#----------------------------------------------------------------------------------------------------------------
#pie plot for type of accidents
def acctype_piechart(year):
    fig,ax = plt.subplots(figsize=(5,5))  
    cnt_Rail = int(0)
    cnt_Road = int(0)
    cnt_other = int(0)  
    if (year == 111):
        for i in range(0,len(acc_type)):
            if acc_type[i] == 'Road Accidents':
                cnt_Road = cnt_Road + total_counts[i]
            elif acc_type[i] == 'Other Railway Accidents':
                cnt_other = cnt_other + total_counts[i]
            else:
                cnt_Rail = cnt_Rail  + total_counts[i]
    
    else:
        for i in range(0,len(year_tm)):
            if (year == year_tm[i]):
                if acc_type[i] == 'Road Accidents':
                    cnt_Road = cnt_Road + total_counts[i]
                elif acc_type[i] == 'Other Railway Accidents':
                    cnt_other = cnt_other + total_counts[i]
                else:
                    cnt_Rail = cnt_Rail  + total_counts[i]
    
    #print(cnt_other,' ',cnt_Road,' ',cnt_Rail)
    cnt_list = []
    cnt_list.append(cnt_Road)
    cnt_list.append(cnt_Rail)
    cnt_list.append(cnt_other)
    list_types = ['ROAD','RAIL-ROAD','OTHER']
    co = ['g','r','c']
    plt.pie(cnt_list,labels=list_types,colors=co,startangle=90,shadow=True,explode=(0,0.1,0.3),autopct='%1.1f%%')
    fig.savefig('pieg2.png')
    
#----------------------------------------------------------------------------------------------------------------
#month-barchart
def monthlyAcc(statename,year):
    fig,ax = plt.subplots(figsize=(10,10))
    month_acc = [0,0,0,0,0,0,0,0,0,0,0,0]
    if(year == 111):
        for i in range(len(states_TM)):
            if (statename == states_TM[i]):
                month_acc[0] += M1[i]
                month_acc[1] += M2[i]
                month_acc[2] += M3[i]
                month_acc[3] += M4[i]
                month_acc[4] += M5[i]
                month_acc[5] += M6[i]
                month_acc[6] += M7[i]
                month_acc[7] += M8[i]
                month_acc[8] += M9[i]
                month_acc[9] += M10[i]
                month_acc[10] += M11[i]
                month_acc[11] += M12[i]

    else :        
        for i in range(len(states_TM)):
            if (statename == states_TM[i] and year == year_tm[i]):
                month_acc[0] += M1[i]
                month_acc[1] += M2[i]
                month_acc[2] += M3[i]
                month_acc[3] += M4[i]
                month_acc[4] += M5[i]
                month_acc[5] += M6[i]
                month_acc[6] += M7[i]
                month_acc[7] += M8[i]
                month_acc[8] += M9[i]
                month_acc[9] += M10[i]
                month_acc[10] += M11[i]
                month_acc[11] += M12[i] 

    index1 = []
    for ind in range(0, len(month_acc)):
        index1.append(ind)
    
    plt.bar(index1, month_acc, width=0.6)    
    plt.xticks(index1, months,rotation=45)
    plt.xticks(size=8)
    plt.xlabel('MONTHS')
    plt.ylabel('TOTAL ACCIDENTS')
    fig.savefig('mA.png')

#----------------------------------------------------------------------------------------------------------------
#time_period_accidents bar-chart
def time_acc(statename, year):
    time_period = [0,0,0,0,0,0,0,0]
    fig,ax = plt.subplots(figsize=(10,20))
    if (year == 111):
        for i in range(0,len(states)):
            if (statename == states[i]):
                time_period[0] += N1[i]
                time_period[1] += N2[i]
                time_period[2] += N3[i]
                time_period[3] += N4[i]
                time_period[4] += N5[i]
                time_period[5] += N6[i]
                time_period[6] += N7[i]
                time_period[7] += N8[i]
    
    else:
        for i in range(0,len(states)):
            if (statename == states[i] and year == acc_year[i]):
                time_period[0] += N1[i]
                time_period[1] += N2[i]
                time_period[2] += N3[i]
                time_period[3] += N4[i]
                time_period[4] += N5[i]
                time_period[5] += N6[i]
                time_period[6] += N7[i]
                time_period[7] += N8[i]

    index1 = []
    for ind in range(0, len(time_period)):
        index1.append(ind)
    
    plt.bar(index1, time_period, width=0.5,color='Red')    
    plt.xticks(index1, label_time_periods,rotation=45)
    plt.xticks(size=14)
    plt.xlabel('TIME OF THE DAY (24 HR FORMAT)',fontsize = 15)
    plt.ylabel('TOTAL ACCIDENTS',fontsize = 15)
    fig.savefig('cb.png')

#----------------------------------------------------------------------------------------------------------------
#type of accidents bar chart
def type_barchart(statename, year):
    type_list = [0,0,0]
    fig,ax = plt.subplots(figsize=(10,20))
    if (year == 111):
        for i in range(len(states_TM)):
            if (statename == states_TM[i]):
                if acc_type[i] == 'Road Accidents':
                    type_list[0] += total_counts[i]
                elif acc_type[i] == 'Rail-Road Accidents':
                    type_list[1] += total_counts[i]
                else:
                    type_list[2] += total_counts[i]
    
    else:
        for i in range(len(states_TM)):
            if (statename == states_TM[i] and year == year_tm[i]):
                if acc_type[i] == 'Road Accidents':
                    type_list[0] += total_counts[i]
                elif acc_type[i] == 'Rail-Road Accidents':
                    type_list[1] += total_counts[i]
                else:
                    type_list[2] += total_counts[i]
                    
    index1 = []
    for ind in range(0, len(type_list)):
        index1.append(ind)
    
    plt.bar(index1, type_list, width=0.5)    
    plt.xticks(index1, types)
    plt.xticks(size=20)
    plt.xlabel('TYPE OF ACCIDENT', fontsize=18)
    plt.ylabel('TOTAL NUMBER OF ACCIDENTS',fontsize=18)
    fig.savefig('tb.png')
    
#----------------------------------------------------------------------------------------------------------------


#Plotting data on  Indian Map
def india_map(year):
    
    fig,ax = plt.subplots(figsize=(20,40))
    india = Basemap(resolution='h', # c, l, i, h, f or None
                projection='merc',
                lat_0=27.90, lon_0=29.4,
                llcrnrlon=68.03, llcrnrlat= 7.78, urcrnrlon=97.43, urcrnrlat=35.76)
    india.drawcountries(linewidth=0.5, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    india.drawcoastlines()
    india.bluemarble()
    india.readshapefile('C:\Users\Amod\Desktop\ACCSDL\StatPlanet_India_Hindi\map\map','areas')
    
    df_states = pd.read_csv('st.csv')
    
    df_poly = pd.DataFrame({
            'shapes': [Polygon(np.array(shape), True) for shape in india.areas],
            'State': [area['NAME_1'] for area in india.areas_info]
        })
    df_poly = df_poly.merge(df_states, on='State', how='left')
    
    
    
    cmap = plt.get_cmap('Reds')   
    pc = PatchCollection(df_poly.shapes, zorder=2)
    norm = Normalize()
    
    pc.set_facecolor(cmap(norm(df_poly[year].fillna(0).values)))
    ax.add_collection(pc)
    
    mapper = mp.cm.ScalarMappable(norm=norm, cmap=cmap)
    
    mapper.set_array(df_poly[year])
    plt.colorbar(mapper, shrink=0.4)
    #plt.show()
    
    fig.savefig(year + '.png')    
#----------------------------------------------------------------------------------------------------------------


#scatter plot for  No.of Vehicles sold in a particular year
def vehicle_type_sales():
    inx=[]
    for i in range(0,len(passV)):
        inx.append(i)

    plt.figure(figsize=(8,8))
    a=plt.scatter(inx,passV,color='red',s=80)
    plt.plot(inx,passV,'-',color='Black')
    
    b=plt.scatter(inx,commV,color='darkblue',s=80)    
    plt.plot(inx,commV,'-',color='Black')
    
    c=plt.scatter(inx,threeW,color='lime',s=80)   
    plt.plot(inx,threeW,'-',color='Black')
    
    d=plt.scatter(inx,twoW,color='orange',s=80)  
    plt.plot(inx,twoW,'-',color='Black')
    
    
    plt.legend((a,b,c,d),
           ('Passenger Vehicles', 'Commercial Vehicles', 'Three Wheelers','Two Wheelers'),
           scatterpoints=1,
           loc='upper left',
           ncol=1,
           fontsize=12)
    plt.xticks(inx,year_gap,rotation=45)
    plt.xlabel('YEARS(2001-2014)')
    plt.ylabel('Total No of Vehicles(IN CRORES)')
    plt.grid(True)
    plt.savefig('veh.png')
    
        
#----------------------------------------------------------------------------------------------------------------
def total_acc_scatter():
    
   plt.figure(figsize=(10,20))
   list_tot = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   for i in range(0,len(states_TM)):
       if year_tm[i] == 2001:
           list_tot[0] += acc_cnt[i]
       elif year_tm[i] == 2002:
           list_tot[1] += acc_cnt[i]
       elif year_tm[i] == 2003:
           list_tot[2] += acc_cnt[i]
       elif year_tm[i] == 2004:
           list_tot[3] += acc_cnt[i]
       elif year_tm[i] == 2005:
           list_tot[4] += acc_cnt[i]
       elif year_tm[i] == 2006:
           list_tot[5] += acc_cnt[i]
       elif year_tm[i] == 2007:
           list_tot[6] += acc_cnt[i]
       elif year_tm[i] == 2008:
           list_tot[7] += acc_cnt[i]
       elif year_tm[i] == 2009:
           list_tot[8] += acc_cnt[i]
       elif year_tm[i] == 2010:
           list_tot[9] += acc_cnt[i]
       elif year_tm[i] == 2011:
           list_tot[10] += acc_cnt[i]
       elif year_tm[i] == 2012:
           list_tot[11] += acc_cnt[i]
       elif year_tm[i] == 2013:
           list_tot[12] += acc_cnt[i]
       elif year_tm[i] == 2014:
           list_tot[13] += acc_cnt[i]
               
   plt.figure(figsize=(8,8))   
   plt.plot(year_list,list_tot,'-',color='Black')      
   plt.scatter(year_list,list_tot,s=140, facecolors='red', edgecolors='white',cmap='spectral')
   plt.xlabel('YEARS(per state)')
   plt.ylabel('TOTAL NUMBER OF ACCIDENTS')
   plt.grid(True)
   plt.savefig('TOTacc.png')
   
#-----------------------------------------------------------------------------------------------------------------
#Safe time sugestion
def safest_month_time(statename):
    global safestat
    global statekk
    statekk = statename
    jan = int(0)
    feb = int(0)
    march = int(0)
    april = int(0)
    may = int(0)
    june = int(0)
    july = int(0)
    aug = int(0)
    sept = int(0)
    octo = int(0)
    nov = int(0)
    dec = int(0)
    min_val = int(0)
    
    for i in range(len(states_TM)):
        if statename == states_TM[i]:
            jan += M1[i]
            feb += M2[i]
            march += M3[i]
            april += M4[i]
            may += M5[i]
            june += M6[i]
            july += M7[i]
            aug += M8[i]
            sept += M9[i]
            octo += M10[i]
            nov += M11[i]
            dec += M12[i]
    
    min_val = min(jan, feb, march, april, may, june, july, aug, sept, octo, nov, dec)
    if min_val == jan:
        safestat = "January is the safest for you!"
    elif min_val == feb:
        safestat="February is the safest for you!"
    elif min_val == march:
        safestat="March is the safest for you!"
    elif min_val == april:
        safestat="April is the safest for you!"
    elif min_val == may:
        safestat="May is the safest for you!"
    elif min_val == june:
        safestat="June is the safest for you!"
    elif min_val == july:
        safestat="July is the safest for you!"
    elif min_val == aug:
        safestat="August is the safest for you!"
    elif min_val == sept:
        safestat="September is the safest for you!"
    elif min_val == octo:
        safestat="October is the safest for you!"
    elif min_val == nov:
        safestat="November is the safest for you!"
    elif min_val == dec:
        safestat="December is the safest for you!"

#---------------------------------------------------------------------------------------------------
#Causes Bar chart
defect = pd.read_csv('Defect_in_Condition_Of_MotorVehicle-2006-14.csv')
defect_states = defect['States/UT'].tolist()
defect_total = defect['Total 2006-14'].tolist()

weather = pd.read_csv('Due_to_Weather_Condition-2006-14.csv')
weather_total = weather['Total 2006-14'].tolist()

driver_fault = pd.read_csv('Fault_of_Driver-2006-14.csv')
driver_fault_total = driver_fault['Total 2006-14'].tolist()

def cause_barchart(statename):
    plt.subplots(figsize=(10,20))
    defect_count = int(0)
    weather_count = int(0)
    driver_fault_count = int(0)
    cause_list = []
    
    for i in range(len(defect_states)):
        if (statename == defect_states[i]):
            defect_count = defect_total[i]
            weather_count = weather_total[i]
            driver_fault_count = driver_fault_total[i]
            break
    
    cause_list = [defect_count, weather_count, driver_fault_count]
    #print (cause_list)
    index1 = []
    causes = ['Vehicle Defects','Weather Conditions','Fault of Driver']
    for ind in range(0, len(cause_list)):
        index1.append(ind)
    plt.figure(figsize=(8,8))
    plt.bar(index1, cause_list, width=0.5)    
    plt.xticks(index1, causes)
    plt.xlabel('\nTYPE OF CAUSE')
    plt.ylabel('TOTAL ROAD ACCIDENTS')
    plt.savefig('tt.png')           
#---------------------------------------------------------------------------------------------------
#Function Calls
#acctype_piechart(111)
#state_time_pie('Gujarat', 111)
state_month_pie('Lakshadweep', 2002)
#monthlyAcc('Goa', 111)
#time_acc('Maharashtra', 111) 
#type_barchart('Uttar Pradesh', 111)
#total_acc_scatter('Gujarat')
#safest_month_time('Goa')
#cause_barchart('All India')
#vehicle_type_sales()
#india_map('2001')















