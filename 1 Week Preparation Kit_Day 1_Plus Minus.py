def plusMinus(arr):
    # Write your code here
    n_of_pos = 0
    n_of_neg = 0
    n_of_zer = 0
    total_element = len(arr)
    for i in arr:
        if i>0:
            n_of_pos += 1
        elif i==0:
            n_of_zer += 1
        else:
            n_of_neg += 1
    print("{:.6f}\n{:.6f}\n{:.6f}".format(n_of_pos/total_element, n_of_neg/total_element, n_of_zer/total_element))
