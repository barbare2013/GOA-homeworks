# # 1) დაწერეთ შეიძლება თუ არა რომ for loopით გადავუაროთ listებს და stringებს? თუ კი მაშინ როგორ?
# # დიახ შძლება რომ for loop-ით გადავუაროთ list-ს და string-ს, მაგ:

# name='babi'
# for i in name:
#     print(i)

# list=['babi', 'anastsasia', 'sofia']
# for i in list:
#     print(i)



# # 2) შექმენით name ცვლადი, შეინახეთ მასში თქვენი სახელი, გადაუარეთ ამ სახელს for ციკლით და ყველა ასო ცალ-ცალკე ჩაამატეთ სხვა სიაში.
# #  შემდეგ ეს სია დაპრინტეთ

# name='babi'
# name2=[]
# for i in name:
#     name2.append(i)
# print(name2)



# # 3) შექმენით სია სადაც შეინახავთ 1-10მდე რიცხვებს, ამ სიას გადაუარეთ for ციკლით და ყველა ლუწი ელემენტი ჩაამატეთ სხვა სიაში.
# #  საბოლოოდ კი ეს სია დაპრინტეთ

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 =[]
# for i in list:
#     if i % 2 ==0:
#         list2.append(i)
# print(list2)



# 4) შექმენით სია სადაც შეინახავთ სახელებს, შემდეგ კი ჩაამატეთ სხვა სიაში მხოლოდ ის სახელები, რომელთა სიგრძე მეტია 4ზე
# list = ['babi', 'anastasia', 'sofia', 'lika', 'elene']
# list2 = []
# for i in list:
#     if len(i) > 4:
#         list2.append(i)
# print(list2)



# 5) შექმენით სახელების სია და ცვლადი სადაც შეინახავთ სახელს, შემდეგ for ციკლით გადაუარეთ სიას და თუ რომელიმე სახელი უდრიდა 
# ჩვენს შექმნილ ცვლადს, მაშინ დაპრინტეთ ეს სახელი

list = ['babi', 'anastasia', 'sofia', 'lika', 'elene']
name = 'babi'
for i in list:
    if i == name:
        print(name)