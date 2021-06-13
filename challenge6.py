df = "カミュ"

for i in range(len(df)):
    print(df[i])

# what = input("昨日何を書いた？")
# when = input("誰に送った？")

# anaume = "私は昨日{}を書いて、{}に送った！".format(what,when)
# print(anaume)

df2 = "aldous Huxley was born in 1894"
print(df2.capitalize())

df3 = "どこで？　誰が？　いつ？"
print(df3.split("　"))

df4 = ["The","fox","jumped","over","the","fence","."]
print(" ".join(df4[:5]) + df4[6])

df5 = "A screaming comes across the sky."
print(df5.replace("s","$"))

df6 = "Hemingway"
print(df6.index("m"))

print("aaaaa\"aaa")

df7 = "Three" + "Three" + "Three"
print(df7)
print(df7*2)

df8 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた"
print(df8[:10])