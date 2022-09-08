import time


def add_100_wrapper(func):
    def improved_func(*args, **kwargs):
        ret = func(*args, **kwargs) + 100
        return ret

    return improved_func


@add_100_wrapper
def test_add_100(x):
    return x


def repeat_5_times_wrapper(func):
    def improved_func(*args, **kwargs):
        for i in range(5):
            func(*args, **kwargs)
        return
    return improved_func


@repeat_5_times_wrapper
def test_print():
    print('体面')


def write_func_name_time_wrapper(func):
    def improved_func(*args,**kwargs):
        with open('../timian.txt','w+') as file:
            run_time=str(time.localtime())
            file.write('runtime is %s, function name is %s' % (run_time,func.__name__))
        func(*args,**kwargs)

    return improved_func


@write_func_name_time_wrapper
def test_write_name_time():
    print('不体面')



def main():
    test_write_name_time()
    test_print()
    print( test_add_100(1))


if __name__ == '__main__':
   main()