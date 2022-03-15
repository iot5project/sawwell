import random

def cust():
    print('INSERT INTO `cust` (`ids`, `password`, `name`, `address`, `email`) VALUES')
    for i in range(1, 101):
        ids = 'id' + str(i)
        password = 'id' + str(i)
        name = 'name' + str(i)
        address = 'addres' + str(i)
        email = 'email' + str(i)
        split = "'" + ',' + "'"
        print("('" + ids + split + password + split + name + split + address + split + email + "'),")
        if i == 100:
            print("('" + ids + split + password + split + name + split + address + split + email + "');")


def food():
    print('INSERT INTO `food` (`name`, `price`) VALUES')
    for i in range(1, 101):
        names = 'food' + str(i)
        price = random.choice(range(1000, 10000))
        split = "'" + ',' + "'"
        print("('" + names + split + str(price) + "'),")
        if i == 100:
            print("('" + names + split + str(price) + "');")


food()


def marketno():
    print('INSERT INTO `food` (`marketname`, `marketaddress`, `open`, `close`,`holiday`,`hit`, `cid`, `foodid` ) VALUES')
    for i in range(1, 101):
        names = 'food' + str(i)
        price = random.choice(range(1000, 10000))
        split = "'" + ',' + "'"
        print("('" + names + split + str(price) + "'),")
        if i == 100:
            print("('" + names + split + str(price) + "');")


food()


# print('INSERT INTO `review` (`reviewno`, `content`, `star`, `custno`, `marketno`) VALUES')
# for i in range(1, 101):
#     content = 'test' + str(i)
#     star = random.choice(range(1, 5))
#     name = 'name' + str(i)
#     custno = i
#     marketno = i
#     split = "'" + ',' + "'"
#     print("('" + ids + split + password + split + name + split + address + split + email + "'),")
#     if i == 100:
#         print("('" + ids + split + password + split + name + split + address + split + email + "');")
#
# for i in range()

