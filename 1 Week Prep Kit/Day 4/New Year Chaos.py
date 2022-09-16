def minimumBribes(q):
    # Write your code here
    #print(q)
    counter = {}
    while q != sorted(q):
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]

                try:
                    counter[q[i+1]] += 1

                    if counter[q[i+1]] > 2:
                        print("Too chaotic")
                        return
                except KeyError:
                    counter[q[i+1]] = 1
    #print("counter:",counter)
    print(sum(counter.values()))
