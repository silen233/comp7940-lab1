
def print_factors(x):
# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    #x = int(input('请输入一个整数\n'))
    #x = 52633
    for i in range(x+1):
        k = x%(i+1)
        if(k==0):
            print(i+1)
    print('\n')


if __name__ == '__main__':
    l = [52633, 8137, 1024, 999]
    for i in range(4):
        print_factors(l[i])
