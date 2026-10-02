import csv
import numpy as np
python_score=[]
aptitude_score=[]
communication_score=[]
sql_score=[]
projects_number=[]
mock_interviews=[]
with open('C:\\Users\\Dines\\Desktop\\AIML_COURSE\\projects\\placement_readyness_tracker\\placement_data.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        python_score.append(int(row['Python_Score']))
        aptitude_score.append(int(row['Aptitude_Score']))
        communication_score.append(int(row['Communication_Score']))
        sql_score.append(int(row['SQL_Score']))
        projects_number.append(int(row['Projects_Completed']))
        mock_interviews.append(int(row['Mock_Interviews_Attended']))
# print(sql_score)
python_array=np.array(python_score)
aptitude_array=np.array(aptitude_score)        
communication_array=np.array(communication_score)
sql_array=np.array(sql_score)
projects_array=np.array(projects_number)
mock_array=np.array(mock_interviews)
avg_python=python_array.mean()
print(avg_python)
apt_max=aptitude_array.max()
apt_min=aptitude_array.min()
num_stds=(communication_array>70).sum()
# print(num_stds)
skill_array=np.array([python_array,aptitude_array,communication_array,sql_array])
# print(skill_array)
skill_gap=np.max(skill_array,axis=0)-np.min(skill_array,axis=0)
# print(skill_gap)