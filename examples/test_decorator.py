# функция декоратор
def dec(f_arg):
    #функция обертка
    def wrapper():
        # доп. функциональность 1
        print("before")
        # вызов целевой функции
        f_arg()
        # доп. функциональность 2
        print("after")
    return wrapper
# новый синтаксис 
@dec    
# целевая функция
def func():
    print("hello!")

# старый синтаксис 
func = dec(func)

# вызов функции 
func()     