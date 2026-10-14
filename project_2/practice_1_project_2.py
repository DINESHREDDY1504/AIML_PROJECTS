import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\Users\\Dines\\Desktop\\AIML_COURSE\\projects\\project_2\\day02_usage.csv')
chat_arr=df['Chat'].to_numpy()
study_array=df['Study'].to_numpy()
vid_arr=df['Video'].to_numpy()
games_arr=df['Games'].to_numpy()
print(len(chat_arr))
print(chat_arr.sum())
print(vid_arr.sum())
print(games_arr.sum())
print(f'Mean of the each app over thirty apps {round(chat_arr.mean(),1),round(vid_arr.mean(),1),round(games_arr.mean(),1)}')
effective_time=study_array-games_arr
# print(effective_time)
max_ind=effective_time.argmax()
min_ind=effective_time.argmin()
print(f'MAX effective day that spent more time on study D{max_ind+1}')
print(f'MIN effective day that spent on the study D{min_ind+1}')
list1=['Chat','Video','Study','Games']
won=[]
for i in range(len(vid_arr)):
    won_ind=[chat_arr[i],vid_arr[i],study_array[i],games_arr[i]]
    w_ind=0
    for ind in range(0,4):
        if(won_ind[w_ind]<won_ind[ind]):
            w_ind=ind
    won.append(list1[w_ind])
print(won)    
print(study_array)
total=chat_arr+vid_arr+study_array+games_arr
chat_share=(chat_arr/total)*100
vid_share=(vid_arr/total)*100
study_share=(study_array/total)*100
games_share=(games_arr/total)*100
print(f'DAY 1 share of chat is {round(chat_share[0],1)}, share of video is {round(vid_share[0])},share of study is {round(study_share[0],1)}, share of games is {round(games_share[0],1)}')
# print(11%4)
# l1=[10,20,30,40,50]
# l2=['hi','bye','dinesh','reddy']
# l3=[(1000,2000),(-1,-2),(10000,20000),(40,50),(10,20),(24,19)]
# print(list(zip(l1,l2,l3)))
apps_arr=df.loc[:,'Chat':].to_numpy()
apps=df.loc[:,'Chat':]
print(apps)
print(apps_arr)
app_sum=apps_arr.sum(axis=0)
print(app_sum)
total_usage_per_day=apps_arr.sum(axis=1)
print(total_usage_per_day)
print(f'Mean of the each app {apps_arr.mean(axis=0)}')
print(f'Mean of the usage per each day {apps_arr.mean(axis=1)}')
print(f'Max usage of the each app {apps_arr.max(axis=0)}')
print(f'Max use of the each day {apps_arr.max(axis=1)}')
print(f'min for usage of each app {apps_arr.min(axis=0)}')
print(f'min usage of each day {apps_arr.min(axis=1)}') 
# max usage of the app in each day
max_index=apps_arr.argmax(axis=1)
# print(max_index)
list1=np.array(list1)
win_apps=list1[apps_arr.argmax(axis=1)]
print(win_apps)
print(np.unique(win_apps))
apps,freq=np.unique(win_apps,return_counts=True)
tup=dict(zip(apps,freq))
print(tup)
total_minutes=apps_arr.sum(axis=1)
print(total_minutes)
apps_share_each_day=(apps_arr/total_usage_per_day[:,None])*100
print(apps_share_each_day)
print(app_sum)
app_share=apps_arr/app_sum
print(app_share)
weekend=((df['Day']%7==6) | (df['Day']%7==0))
print(df[weekend].mean(axis=0))
print(df[~weekend].mean(axis=0))
busy_ind=total_minutes.argmax()
print(busy_ind+1)
print(df.loc[busy_ind])
days=df['Day']
std=df['Study']
print(apps_share_each_day.sum(axis=1))
# print(total_minutes)
fig,ax=plt.subplots(2,1,figsize=(11,8))
for i,app in enumerate(list1):
    ax[0].plot(days,apps_arr[:,i],marker='o',markersize='2',label=app)
peak_day=int(total_minutes.argmax())
ax[0].annotate(f'max usage day is {peak_day+1}',xy=(days[peak_day],apps_arr[peak_day].max()),xytext=(days[peak_day]+10,apps_arr[peak_day].max()+20),arrowprops=dict(arrowstyle='->'))    

# plt.plot(df['Day'],df['Study'])
# min_study=df['Study'].argmax()
# plt.annotate(f'Most studied day {days[min_study]+1}',xy=(days[min_study],std[min_study]),xytext=(days[min_study]+10,std[min_study]+10),arrowprops=dict(arrowstyle='->'))
# plt.grid(alpha=0)
ax[0].legend(ncol=4)
ax[0].set_title("total time for each app during 30 days",fontsize=6,fontweight='bold')
ax[0].set_xlabel('Days')
ax[0].set_ylabel('Minutes')
ax[0].grid(alpha=0.4)

bottom=np.zeros(len(days))
for i,app in enumerate(list1):
    ax[1].bar(days,apps_share_each_day[:,i],bottom=bottom,label=app)
    bottom=bottom+apps_share_each_day[:,i]
ax[1].set_title("Bar plot of each apps shares on 100%",fontsize=4,fontweight='bold')
ax[1].set_ylabel("percantage%")
ax[1].set_xlabel("Days")
ax[1].set_ylim(0,100)
ax[1].legend(ncol=4,frameon=False,loc='best')
plt.tight_layout()
plt.savefig('day02_usage_chart.png')
plt.show()
plt.close()

