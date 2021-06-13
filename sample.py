"""複数行にわたる
　　コメントを残す際は
　　三重クォートを使用する
"""
authir = "Kafka"
print(authir[0])
print(authir[1])
print(authir[2])

print(authir.upper())
df = "sample"

print(authir.lower())

print(df.capitalize())

print("File{}".format(df))
print("Faile{}.{}".format(df,authir))

a = "私の名前は、佐藤猛です"
print(a.split("、"))

print(" ".join(a))
b = " ".join(a)
print(b.strip())
c = "     abcd     "
print(c.strip())

print(a.replace("私","あなた"))
try:
    "animals".index("z")
except:
    print("Not found.")