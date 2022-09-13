# import sys

# def inrange(a):
#     package = []
#     a = int(a)
#     for i in range(3000, 5001, 1):
#         if (i % a == 0) and (i % (a+7) == 0) and (i % (a ** 2) == 0):
#             package.append(i)


#     print(package)

# inrange(6)


import sys

def inrange():
    package = []
    a = int(sys.argv[1])
    for i in range(3000, 5001, 1):
        if (i % a == 0) and (i % (a + 7) == 0) and (i % (a ** 2) == 0):
            package.append(i)


    print(package)

inrange()