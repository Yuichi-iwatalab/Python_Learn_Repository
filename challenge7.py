# prob1
movie_title = ["ウォーキングデッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for title_name in movie_title:
    print(title_name)

#prob2
# for i in range(25,51):
#     print(i)

#prob3
for i, title_name in enumerate(movie_title):
    print("{}:{}".format(i,title_name))


"prob4"
# correct_number_list = [1,2,7]
# # df = input("数字を入力してください（qで終了します）")
# while True:
#     df = input("数字を入力してください（qで終了します）")
    
#     if df == "q":
#         break
    
#     try:
#         df = int(df)
#     except ValueError:
#         print("数字を入力するか、qで終了します")

#     if df in correct_number_list:
#         print("Congraturaition")
#     else:
#         print("Incorrect")

#prob5
number_list1 = [8,19,148,4]
number_list2 = [9,1,33,83]
number_list3 = []

for i in number_list1:
    for j in number_list2:
        a = i*j
        number_list3.append(a)

print(number_list3)
    
