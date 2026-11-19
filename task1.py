import random
# n = [random.randint(4,600) for x in range(10)] #  для тестов
def data():
    try:
        a = int(input("Введите количество чисел в последовательности (4<=A<=600)"))
        if not(4<=a<=600):
            print("Ошибка! число должно быть заданного диапазона")
            return
        n = list(map(int,input(f"Введите {a} целых чисел через пробел").split()))
        if len(n)!= a:
            print(f"Ошибка! введите ровно {a} целых чисел")
            return
    except ValueError:
        print(f"Ошибка! Вводите только целые числва")
        return

    print(n)
    piks = []
    vpad = []


    # пики и впадины
    if a>=3:
        for x in range(1,a-1):
            nums = [n[x-1], n[x],n[x+1]]
            if n[x]>n[x-1] and n[x]>n[x+1]:
                piks+=[n[x]]
            if n[x]<n[x-1] and n[x]<n[x+1]:
                vpad+=[n[x]]
        print(f"Пики: {piks}\nВпадины: {vpad}")


    # сумма и произведение 
    summ = 0
    product = 1
    for x in range(a):       
        if (x+1)%2==0: summ+=n[x]
        if (x+1)%2!=0: product*=n[x]
    print(f"Суммы элементов на четных позициях: {summ}")
    print(f"Произведение элементов на нечетных позициях {product}")

    # прогрессия
    prog = 0
    if a>=3:
        for x in range(a-2):
            if n[x+1] - n[x] == n[x+2] - n[x+1]:
                prog+=1
    print(f"Арифметических прогрессий найдено: {prog}")

    # новый список
    new = []
    if a == 1:
        new+=[n[0]]
    elif a == 2:
        new+=[n[0]+n[1]]
        new+=[n[0]+n[1]]
    else:
        new+=[n[0]+n[1]]
        for x in range(1,a-1):
            new.append(n[x-1]+n[x]+n[x+1])
        new+=[n[-1]+n[-2]]
    print(f"Новый список: {new}")

    # медиана
    s = sorted(n)
    if a%2 == 1:
        median = s[a//2]
    else:
        median = (s[a//2-1]+s[a//2])/2.0
    otkl = sum(1 for x in n if abs(median-x)>10)
    print(f"Медиана: {median}")
    print(f"Количество элементов, отклоняющихся от медианы более чем на 10: {otkl}")

data()