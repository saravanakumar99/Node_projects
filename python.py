def hexadecimal(n):
    hex_num = hex(n)
    return hex_num[2:]

def decimal(n):
    dec_num = n
    return dec_num

def binary(n):
    bin_num=bin(n)
    return bin_num[2:]

def octal(n):
    oct_num= oct(n)
    return oct_num[2:]

n=int(input())

for i in range(1,n+1):
    print(decimal(i),"  ",octal(i),"  ",hexadecimal(i),"  ",binary(i))

