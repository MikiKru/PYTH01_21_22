from d4.my_module import *
import d4.my_module as m

if __name__ == '__main__':              # determinuje, że od tego miejsca program/projekt jest uruchamiany
    print(global_value)
    print(power(2,3))
    a = Auto("BMW", "X5", "black")
    print(a)

    for k, v in m.__dict__.items():
        print(k, v)