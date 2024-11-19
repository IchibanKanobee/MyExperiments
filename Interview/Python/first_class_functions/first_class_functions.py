#Functions are treated as any variable, they can be assigned to a variable, passes as an argument, returned from a function

def square(x):
    return x*x

f = square(5)
print(f)

#Assigning to a variable
f1 = square
print (f1)
print(f1(5))

#Passing as an argument
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])
print (squares)

def cube(x):
    return x*x*x

cubes = my_map(cube, [1,2,3,4,5])
print (cubes)

#Returning from a function
def logger(msg):

    def log_message():
        print("Log:", msg)

    return log_message()

log_hi = logger("Hi")
#log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1 ('Test headline')
print_h1 ('Another headline')

print_p = html_tag('p')
print_p("This is a paragraph")