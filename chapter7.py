people = {"G.Bluth":"A.Development","Barney":"HIMMY","Dennis":"Alwayas Sunny"}

for i in people:
    print(i)

for i, df in enumerate(people):
    print("{}:{}".format(i,df))