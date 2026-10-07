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
won=np.array([])
for i in range(len(vid_arr)):
   