import csv

APP_NAME='Instagram_Minutes'
minutes=[]
with open('digital_behaviour_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        minutes.append(int(row[APP_NAME]))
minutes=minutes[-7:]
print(minutes)   
# find the sum of the values in the minutes  
total=sum(minutes)
print(total)
# find the average of the values in minutes 
average=total/len(minutes)
max_value=minutes[0]
# assume that max is the first value and find the max in minutes
for i in minutes:
    if(max_value<i):
        max_value=i
min_value=minutes[0]
# assume that min value is the first value and find min value in muntes 
for i in minutes:
    if(min_value>i):
        min_value=i
counter=0
# increase the counter value if the value in munutes is greater than the average of the minutes values 
for i in minutes:
    if i>average:
        counter+=1
print(counter) 






