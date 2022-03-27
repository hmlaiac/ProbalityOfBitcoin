

if __name__ == '__main__':
    import math
    target = 0.9
    k = 5 # k is the length of leading zeros
    a = 1.0/(16**k)
    r = 1.0 - a
    print(r)
    print(a)
    ans = 1.0-target/a*(1-r)
    print(math.log(r))
    result = math.log(ans)/ math.log(r)
    print('The result is %d'%(result+1))
