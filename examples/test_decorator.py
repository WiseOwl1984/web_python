# функция - декоратор - обычная функция 
def dec(f_arg):
    def wrapper():
        # доп функциональность №1
        print("Before")
        f_arg()
        # доп функциональность №2
        print ("After")
    return wrapper  

# целевая функция 
@dec
def funk_1():
    print("hello")

funk_1()    