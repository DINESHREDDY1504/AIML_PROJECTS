import numpy as np
import pandas as pd
df=pd.read_csv('day02_usage.csv')
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
print(11%4)