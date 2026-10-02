import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('placement_data.csv')
print(df.head())
print(df.columns)
print(df.describe())
print(df.shape)
print(df[df['Python_Score']>75])
df_sorted_by_aptitude=df.sort_values('Aptitude_Score',ascending=False)
print(df_sorted_by_aptitude)
df_sorted_by_python=df.sort_values('Python_Score',ascending=False)
print(df_sorted_by_python)
print(df[(df['Python_Score']>=75) & (df['Communication_Score']<50)])
df['Total_Score']=(df['Communication_Score']+df['Python_Score']+df['SQL_Score']+df['Aptitude_Score'])
print(df['Total_Score'])
df['Average_Score']=df['Total_Score']/4;
print(df['Average_Score'])
df['Weakest_Skill']=df[['Communication_Score','Python_Score','Aptitude_Score','SQL_Score']].min(axis=1)
print(df['Weakest_Skill'])
df['Readiness_Score']=(df['Average_Score']+df['Projects_Completed']*2+df['Mock_Interviews_Attended']*1)
print(df['Readiness_Score'])
df['Readiness_Band']='Ready'
df.loc[(df['Readiness_Score']>=60)& (df['Readiness_Score']<=74),'Readiness_Band']='Almost Ready'
df.loc[df['Readiness_Score']<60,'Readiness_Band']='Needs Work'
print((df['Readiness_Band']=='Ready').sum())
# plt.bar(['Aptitude_Score ','Python_Score      ','    Communication_Score     ','   SQL_Score '],df[['Aptitude_Score','Python_Score','Communication_Score','SQL_Score']].mean(axis=0))
# plt.xlabel("Skill")
# plt.ylabel('Average Score Out Of(100)')
# plt.title("Average Score Of Each Skill")
# plt.show()
# plt.bar(['Ready','Almost Ready','Needs Work'],[(df['Readiness_Band']=='Ready').sum(),(df['Readiness_Band']=='Almost Ready').sum(),(df['Readiness_Band']=='Needs Work').sum()])
# plt.show()
# plt.bar(['CSE','IT','ECE','MECH'],[df.loc[df['Branch']=='CSE','Readiness_Score'].mean(),df.loc[df['Branch']=='IT','Readiness_Score'].mean(),df.loc[df['Branch']=='ECE','Readiness_Score'].mean(),df.loc[df['Branch']=='MECH','Readiness_Score'].mean()],color=['blue','green','yellow','red'])
# plt.xlabel('Branch')
# plt.ylabel('Average Readiness Score')
# plt.title('Average Readiness Score By Branch')  
# plt.show()