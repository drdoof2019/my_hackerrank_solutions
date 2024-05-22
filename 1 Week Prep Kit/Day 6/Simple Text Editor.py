# Enter your code here. Read input from STDIN. Print output to STDOUT
def append(s, text):
    return s+text
def delete(s, k):
    return s[:-k]
def printchar(s, k):
    return s[k-1]
s=""
archive = []
Q = int(input())  # read the number of operations
# print(Q)
archive.append(s)
for _ in range(Q):
    op = input().split()  # read the operation and its arguments
    # print(op)
    # print(archive)
    if op[0] == "1":
        s = append(s, op[1])
        archive.append(s)
        # print(s)
    elif op[0] == "2":
        s = delete(s, int(op[1]))
        archive.append(s)
        # print(s)
    elif op[0] == "3":
        print(printchar(s, int(op[1])))
    else:
        archive.pop()
        s = archive[-1]
        # print("afterundos:",s)