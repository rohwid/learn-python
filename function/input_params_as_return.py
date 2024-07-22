def func(a, b):
    for i in range(0, b):
        a.append(i)

if __name__ == "__main__":
    list_a = []
    func(a=list_a, b=10)
    print(list_a)