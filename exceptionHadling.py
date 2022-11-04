# Exception handling - Caused by the internal events in the code. Exception is the base call for all the exceptions.

# a = ["1" "223", "12342", "242"]
# try:
#     print("Second Index in the array : %s" %(a[1]))
#     print("Fifth Index in the array : %s" %(a[4]))
# except:
#     print("Avoid an error if occurs")

# def fun(fact):
#     if fact < 4:
#         newFact = fact/(fact-3)
#
#     print("Value for Fact 1 : ", newFact)
#
# try:
#     fun(3)
#     fun(10)
# except ZeroDivisionError:
#     print("Zero division error occured and handled")
# except NameError:
#     print("Name error occured and handled")

def abyB(a, b):
    try:
        c = (a+b)/(a-b)
        print(c)
    except ZeroDivisionError:
        print("Zero division error due to divisible by 0")
    finally:
        print("Always be executed for my time")

abyB(3,2)