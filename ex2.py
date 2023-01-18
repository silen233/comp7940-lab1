
def print_factors():
# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    x = int(input('请输入一个整数\n'))
    #x = 52633
    for i in range(x+1):
        k = x%(i+1)
        if(k==0):
            print(i+1)


if __name__ == '__main__':
    print_factors()
