import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('digital_behaviour_data.csv')
# print(df)
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.describe())
print(df.info())
print(df['Instagram_Minutes'])
print(df[['Date','Instagram_Minutes']])
print(df['Instagram_Minutes'].sum())
print(df['Study_Minutes'].mean())
print(df['YouTube_Minutes'].max())
print(df[df['Instagram_Minutes']>100])
print(df[df['Study_Minutes']>180])
print(df[df['Instagram_Minutes']>df['Study_Minutes']])
df_insta_sorting=df.sort_values('Instagram_Minutes',ascending=False)
print(df_insta_sorting)
print(df_insta_sorting.head(5))
df_study_sorting=df.sort_values('Study_Minutes',ascending=False)
print(df_study_sorting.head(5))
df['Total_Screen_Time']=(df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes'])
print(df['Total_Screen_Time'])
df['Screen_Hours']=df['Total_Screen_Time']/60;
print(df['Screen_Hours'])
df['Digital_Balance']=df['Study_Minutes']/df['Total_Screen_Time']
print(df['Digital_Balance'])
df['Day_Type']='normal'
print(df['Day_Type'])
# loc method is used to select the data from the dataframe based on  the rows,columns 
# syntax=.loc[what rows condition,what columns condition] 
df.loc[df['Total_Screen_Time']>300,'Day_Type']="Heavy"
print(df['Day_Type'])
print(df.head(10))
# print(df.loc[''])
Total_Minutes={
    "Intasgram":df['Instagram_Minutes'].sum(),
    "Youtube":df['YouTube_Minutes'].sum(),
    "Whatsapp":df['WhatsApp_Minutes'].sum(),
    "LinkedIn":df["LinkedIn_Minutes"].sum()
    
}
print(Total_Minutes)
print(max(Total_Minutes,key=Total_Minutes.get))

# print((df['Day_Type']=='Heavy').sum())
# print(df['Day_Type'])
max_idx=df['Digital_Balance'].idxmax()
# print(df.loc[max_idx,''])
# print(df)
print(df.loc[max_idx,'Date'])
# df.to_csv('my_analysis.csv')
max_screen_time_idx=df['Total_Screen_Time'].idxmax()
print(df.loc[max_screen_time_idx,'Date'])
print(df.loc[max_screen_time_idx,'Study_Minutes'])
digital_avg=df['Digital_Balance'].mean();
print(digital_avg)
df['Day_Label']=[f'D{i+1}' for i in range(len(df))]
cols=df['Day_Label']
plt.tight_layout()
plt.bar(cols,df['Total_Screen_Time'])
plt.title('MY Screen Time by Day')
plt.xlabel('Day')
plt.ylabel('Minutes')
plt.xticks(rotation=90)

plt.close()
insta_total_time=df['Instagram_Minutes'].sum()
whatsapp_minutes=df['WhatsApp_Minutes'].sum()
youtube_minutes=df['YouTube_Minutes'].sum()
LinkedIn_Minutes=df['LinkedIn_Minutes'].sum()
plt.bar(['Instagram','WhatsApp','Youtube','LinkedIn'],[insta_total_time,whatsapp_minutes,youtube_minutes,LinkedIn_Minutes])
plt.title('Total Time by App')
plt.close()
plt.tight_layout()
plt.plot(df['Day_Label'],df['Study_Minutes'],color='green',label='study')
# plt.legend()
plt.plot(df['Day_Label'],df['Total_Screen_Time'],color='red',label='screen time')
plt.xlabel('Day')
plt.ylabel('Minutes')
plt.title('Study time vs screen time')
plt.legend()
# plt.show()
plt.close()
plt.pie([insta_total_time,whatsapp_minutes,youtube_minutes,LinkedIn_Minutes],labels=['Instagram','Whatsapp','youtube','LinkedIn'],autopct='%1.1f%%')
plt.savefig('pie_chart.png',dpi=100)
plt.show()


