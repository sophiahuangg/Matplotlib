import csv
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#plt.plot() uses line plot by default
#plt.bar() gives bar graph. plt.title() plt.xlabel() plt.ylabel()
with open('nba/nba2021_advanced.csv') as csv_file:
    read=csv.DictReader(csv_file)
    player_Counter=Counter()
    for row in read:
        player_Counter.update([row['Age']])
print("player_counter=", player_Counter)

#pie chart

figure,ax=plt.subplots()

age=[]
player=[]
for i in player_Counter.most_common(5):
    age.append(i[0])
    player.append(i[1]) 
print(age)
print(player)

plt.figure(1)
plt.suptitle("Most Common Ages of NBA Players")
plt.title("These are the five most common ages in the NBA (NOT all the ages). This pie chart tells you the percent each age constitutes in the five most common ages.", fontsize=8)
slices = player
labels = age
colors=['#FF9933', '#D0E3FF','#FF9999','#D3B1C2', '#94C973']
plt.pie(slices, labels=labels, startangle=90, colors=colors, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})

#using Pandas
#this data is a bit outdated, some of these players no longer play for the Spurs
plt.figure(2)
df=pd.read_csv('nba/nba2021_advanced.csv')
columns=df[['Player','Tm']]
print(columns)
a=df.iloc[[4, 13, 108, 117, 126, 268],[0,7,8,9]]
print(a)

print(a)
a.pivot(index='Player', columns=[]).plot(kind='bar')
plt.title("Player Performance")
plt.ylabel("Value")
plt.tight_layout()
plt.show()

'''
#bar graph: not going to do this one anymore


with open('nba/nba2021_advanced.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    position_Counter=Counter() 
    for row in csv_reader:
        position_Counter.update([row['Pos']])
position=[]
players=[]

for i in position_Counter.most_common(9):
    position.append(i[0])
    players.append(i[1]) 
print(position)
print(players)


plt.bar(position, players, color='#FF9933')
plt.title("Positions of NBA Players")
plt.xlabel("Positions")
plt.ylabel("Number of NBA Players Playing This Position ")
plt.tight_layout()
plt.show()
'''





