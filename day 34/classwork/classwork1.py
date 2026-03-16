# 1) ახსენით რაში გამოვიყენებთ და რატომ არიან კარგი custom ფუნქციები
# cusom ფუნქციით შეგვიძია შევქმნათ საკუთარი ფუნქცია და დავარქვათ სასურველი სახელი.


# 2) ახსენით რაში ვიყენებთ return და რატომ უნდა გამოვიყენოთ ისინი
# return გამოიყენება print-ის მაგივრად რადგან ის უფრო კარგი საშუალებაა.
# return გამოიყენება მაშინ როცა ვქმნით ფუნქციას.


# 3) შექმენით Custom ფუნქცია სახელად greet რომელსაც ექნება ერთი პარამეტრი - name და return-ით დააბრუნებს "Hello, {name}!".

def greet(name):
    return 'hello ' + name

print(greet('babi'))


# 4) შექმენით Custom ფუნქცია სახელად sum_number რომელსაც ექნება ორი პარამეტრი - num1, num2 და return-ით დააბრუნებს მათ ჯამს.

def sum_number(num1, num2):
    return num1 + num2

print(sum_number(10, 15))


# 5) შექმენით Custom ფუნქცია სახელად multiply რომელსაც ექნება ორი პარამეტრი - num1, num2 და return-ით დააბრუნებს მათ ნამრავლს.


def multiply(num1, num2):
    return num1 * num2

print(multiply(15, 2))


# 6) შექმენით ფუნქცია რომელსაც ექნება 1 პარამეტრი - num და return-ით დააბრუნებს მის კვადრატს

def number(num):
    return num * num

print(number(3))

# 7) შექმენით ფუნქცია რომელიც მიიღებს სიტყვას პარამეტრად და დააბრუნებს მის სიგრძეს

def name(name2):
    print(len(name2))

name('babi')


# 8) შექმენით ფუნქცია რომელიც მიიღებს რიცხვს პარამეტრად და დააბრუნებს ეს რიცხვი კენტია თუ ლუწი

def number(number2):
    if number2 % 2 ==0:
        print('ლუწი')
    else:
        print('კენტი')
number(10)


# 9) შემქმენით ფუნქცია რომელიც მიიღებს არგუმენტად 3 რიცხვს და დააბრუნებს რომელია მათ შორის ყველაზე დიდი

def num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num(1, 2, 3)

# # 10) შექმენით ფუნქცია რომელიც მიიღებს სიტყვას და დააბრუნებს ამ სიტყვას შებრუნებულს

# def name(name1):



# name('goa')