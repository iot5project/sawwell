import random


def cust():
    print('INSERT INTO `cust` (`id`, `password`, `name`, `address`, `email`) VALUES')
    for i in range(1, 316):
        ids = 'id' + str(i)
        password = 'id' + str(i)
        name = 'name' + str(i)
        address = 'addres' + str(i)
        email = 'email' + str(i)
        split = "'" + ',' + "'"
        print("('" + ids + split + password + split + name + split + address + split + email + "'),")
        if i == 315:
            print("('" + ids + split + password + split + name + split + address + split + email + "');")


cust()


def food():
    print('INSERT INTO `food` (`name`, `price`) VALUES')
    for i in range(1, 101):
        names = 'food' + str(i)
        price = random.choice(range(1000, 10000))
        split = "'" + ',' + "'"
        print("('" + names + split + str(price) + "'),")
        if i == 100:
            print("('" + names + split + str(price) + "');")


def marketno():
    print('INSERT INTO `food` (`marketname`, `marketaddress`, `open`, `close`,`holiday`,`hit`, `cid`, `foodid` ) VALUES')
    for i in range(1, 101):
        names = 'food' + str(i)
        price = random.choice(range(1000, 10000))
        split = "'" + ',' + "'"
        print("('" + names + split + str(price) + "'),")
        if i == 100:
            print("('" + names + split + str(price) + "');")


# food()

def review():
    print('INSERT INTO `review` ( `content`, `star`, `custno`, `seochono`) VALUES')
    for i in range(1, 316):
        content = 'markettest' + str(i) + 'user' + str(i)
        star = random.choice(range(1, 5))
        custno = i
        seochono = i
        split = "'" + ',' + "'"
        print("('" + content + split + str(star) + split + str(custno) + split + str(seochono) + "'),")
        if i == 315:
            print("('" + content + split + str(star) + split + str(custno) + split + str(seochono) + "');")


# review()


def ceo():
    print('INSERT INTO `ceo` ( `id`, `password`, `name`, `seochono`) VALUES')
    for i in range(1, 316):
        id = 'ceo' + str(i) + 'id' + str(i)
        password = 'password' + str(i)
        name = 'ceo' + str(i)
        seochono = i
        split = "'" + ',' + "'"
        print("('" + id + split + password + split + name + split + str(seochono) + "'),")
        if i == 315:
            print("('" + id + split + password + split + name + split + str(seochono) + "');")


# ceo()


def reply():
    print('INSERT INTO `reply` ( `content`, `ceoid`, `reviewno`) VALUES')
    for i in range(1, 316):
        content = 'market' + str(i) + 'ceo' + str(i) + 'id' + str(i)
        ceoid = i
        seochono = i
        split = "'" + ',' + "'"
        print("('" + content + split + str(ceoid) + split + str(seochono) + "'),")
        if i == 315:
            print("('" + content + split + str(ceoid) + split + str(seochono) + "');")


# reply()