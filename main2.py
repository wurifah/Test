
for num in range(101, 0, -1):
    if num < 2:
        print(num, end=" ")
        continue
    for i in range(2, num):
        if (num % i) == 0:
            if num % 3 == 0 and num % 5 == 0:
                num = 'FooBar'
            elif  num % 3 == 0:
                num = 'Foo'
            elif num % 5 == 0:
                num = 'Bar'
            print(num, end=" ")
            break
