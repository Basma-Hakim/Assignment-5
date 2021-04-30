def name():
    import string
    import random
    list1=''
    for i in range(6):
        list1=list1+random.choice(string.ascii_letters)
        
    return ''.join(list1)