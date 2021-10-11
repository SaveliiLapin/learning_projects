def reversal():
    a = int(input())

    if a != 0:
        reversal()
        print(a, end=' ')
    else:
        print(a, end=' ')


reversal()
