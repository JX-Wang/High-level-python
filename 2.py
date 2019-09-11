while True:
    try:
        n = input()
        if n < 1 or n > pow(10, 9):
            break

        while n & 1 == 0:
            n >>= 1

        print n

        ans = 1
        d = 3
        while d*d <= n:
            e = 0
            while n % d == 0:
                n /= d
                e += 1
            ans *= e + 1
            d += 2
        if n > 1: ans *= 2
        print ans
    except:
        break
