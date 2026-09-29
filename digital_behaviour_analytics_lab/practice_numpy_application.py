import numpy as np
import csv 
insta_list=[]
study_time=[]
with open('digital_behaviour_data.csv','r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row['Instagram_Minutes']))
        study_time.append(int(row['Study_Minutes']))
insta=insta_list[:7]
study=study_time[:7]
insta_array=np.array(insta)
study_array=np.array(study)
# print(insta_array)
# total=np.sum(insta_array)
total=insta_array.sum()
average=insta_array.mean()
insta_max_value=insta_array.max()
insta_min_value=insta_array.min()
# print(insta_min_value)  
print(len(insta_array))      
# print(insta_array)
# take the first three days
print(insta_array[-2::])
# show me the days two,three,four
print(insta_array[2:5])
# print(insta_array/60)
hours=insta_array/60
diff=study_array-insta_array
# print(diff)
valid=insta_array>100
print(insta_array[insta_array>100])
print((insta_array>100).sum())

 
# str="GRIET College Nizampet Hyderabad"
# l=[]
# res=""
# l=str.split(" ");
# for i in l:
#     res+=i[::-1]
#     res+=" "
# print(res)
