import os
import csv

st = open("st.txt","w")
st.write("Hi from python!")
st.close()

st = open("st.txt","w",encoding="utf-8")
st.write("Pythonからこんにちは")
st.close()

with open("st.txt","w") as f:
    f.write("Hi from Python")

my_list = []
with open("st.txt","r",encoding="utf-8") as f:
    my_list.append(f.read())
    print(f.read())

print(my_list)

with open("st.csv","w",encoding="utf-8",newline="") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

with open("st.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    # my_list.append(r)
    for row in r:
        print(",".join(row))

print(r)