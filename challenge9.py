import os
import csv

my_list = []
with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())
    my_list.append(f.read())

df = input("あなたの好きな食べ物は何ですか？")
with open("favorite_food.txt","w",encoding="utf-8") as f:
    f.write(df)
    # f.write(df + "\n")

with open("favorite_food.txt","r",encoding="utf-8") as f:
    print(f.read())
    my_list.append(f.read())

lists = [["Top Gun","Risky Business","Minority Report"],["Titaniv","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("title.csv","w",encoding="utf-8",newline="") as f:
    a = csv.writer(f,delimiter=",")
    for i in lists:
        a.writerow(i)



