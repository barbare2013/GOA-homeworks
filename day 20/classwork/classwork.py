# 1)მომხარებელს შემოატანინეთ სახელი, შეამოწმეთ თუ ეს სახელი უდრის "Aleksandre", მაშინ დაპრინტეთ "Mentor", სხვა შემთხვევაშ დაპრინტეთ "student"

name= input('enter your name: ')

if name == 'Aleksandre':
    print('mentor')
else:
    print('student')


# 2)მომხარებელს შემოატანინეთ სახელი, და შეამოწმეთ, თუ ეს სახელი უდრის "ana" ს, დაპრინტეთ 3, სხვა შემთხვევაში კი დაპრინტეთ "idk"

name=input("enter your name: ")

if name=="ana":
    print(3)
else:
    print("idk")


# 3)მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ შექმენით ცვლადი  და შგნით შეინახე რომელიმე რიცხვი 1 დან 10 მდე, შემდეგ მომხარებელს
#  უსასრულოდ შემოატანინეთ რიცხვი და შეამოწმეთ უდრის თუ არა იმ ცვლადში შენახულ რიცხვს, თუ უდრის მაშინ დაპრინტეთ "win" და გათიშეთ
#  პროგრამა quit() ფუნქციით, სხვა შემთხვევაში კი დაპრინტეთ 'lose"


while True:
    number=int(input("enter your number: "))
    pasword=5
    if number ==pasword:
        print("win")
        quit()
    else:
        print('lose')

