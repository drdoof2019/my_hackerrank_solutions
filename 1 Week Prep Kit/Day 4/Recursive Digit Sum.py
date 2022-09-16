def superDigit(n, k=1):
    # Write your code here
    print("n:",n, "\nk:",k)
    p = list(str(n))
    sum = 0
    for i in p:
        sum += int(i)
    sum = sum*k
    if sum<10:
        print("inside here")
        return sum
    else:
        return superDigit(sum)
