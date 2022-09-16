def lonelyinteger(a):
    # Write your code here
    print(a)

    while True:
        i = a[0]
        try:
            a.remove(i)
            a.remove(i)
            print("after remove a", a)
        except:
            return i
