def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    Min = 0
    Max = 0
    for i in range(4):
        Min += arr[i]
        Max += arr[4-i]
    result = str(Min) + " " + str(Max)
    print(result)
