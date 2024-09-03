#A closure is a record storing a function together with an environment

#inner_function is aware of a free variable message
def outer_func():
    message = "Hi"
    def inner_function():
        print (message)

    return inner_function()

outer_func()

def outer_func1():
    message = "Hi"
    def inner_function():
        print (message)

    return inner_function

my_func = outer_func1()
print(my_func)

my_func()
my_func()
my_func()
#A closure is an inner function that remembers and has access to variables of the outer function, even if the outer funcion is finished executing

def outer_func2(msg):
    message = msg
    def inner_function():
        print (message)

    return inner_function

hi_func = outer_func2("Hi")
hello_func = outer_func2("Hello")

hi_func()
hello_func()

