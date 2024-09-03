#https://www.youtube.com/watch?v=FsAPt_9Bf3U&ab_channel=CoreySchafer

import time
from functools import wraps


def outer_func(msg):
    def inner_function():
        print (msg)

    return inner_function

hi_func = outer_func("Hi")
bye_func = outer_func("Bye")

hi_func()
bye_func()

#Decorator isa a function that takes another function as an argument, adds some kind of functionality, returns another function, all of this without altering the source code of the original function that was passed in
def decorator_func(original_function):
    def wrapper_function():
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

def display():
    print ('display function ran')

decorated_display = decorator_func(display)
decorated_display()

@decorator_func
def display2():
    print ('display function ran')

display2()

def display_info(name, age):
    print('display info run with arguments {} and {}'.format(name, age))

display_info('John', 25)


# @decorator_func
# def display_info(name, age):
#     print('display info run with arguments {} and {}'.format(name, age))
#
# display_info('John', 25)

def decorator_func2(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_func2
def display_info(name, age):
    print('display info run with arguments {} and {}'.format(name, age))

display_info('John', 21)

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
#
# @decorator_class
# def display_info3(name, age):
#     print('display info run with arguments {} and {}'.format(name, age))
#
# display_info3('John', 21)

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info2(name, age):
    print('display info run with arguments {} and {}'.format(name, age))

display_info2('John', 21)


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
def display_info3(name, age):
    time.sleep(1)
    print('display info run with arguments {} and {}'.format(name, age))

display_info3('John', 21)

@my_logger
@my_timer
def display_info4(name, age):
    time.sleep(1)
    print('display info run with arguments {} and {}'.format(name, age))

display_info4('Tom', 33)