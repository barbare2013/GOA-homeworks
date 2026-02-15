# 5)შექმენით  ფუნქცია, რომელიც არგუმენტად იღებს  სახელს,  და  ესალმება მას

def name(name2):
    print('hello ' + name2)
name('babi')



# 6)შექმენით ფუნქცია, რომელიც არგუმენტად იღებს  სახელს და  მის სიგრძეს პრინტავს

def name(name2):
    print(len(name2))
name('babi')



# 7)შექმენით ფუნქცია, რომელიც არგუმენტად იღებს სიას ბევრი  სახელით და თითოეულს  ესალმება

def list(list2):
    for i in list2:
        print('hello '+ i)
list(['babi', 'lika', 'anastasia', 'sofia', 'elene', 'mariami'])
