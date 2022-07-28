def operate(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and k != j and k != i:
                    print(L[i], L[j], L[k])


myList = [1, 2, 3]
operate(myList)
