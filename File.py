import time

class BariKlass:
    eat = 100
    water = 100
    sleep = 100
    play = 100
    cash = 100
    while eat:
        print(f"Текущая еда: {eat}")
        a = input("Купить еду?:")
        if a == "Да":
            eat + 10
            cash =- 10
        else:
            eat - 10
            time.sleep(2)
        print(f"Текущая еда: {water}")
        a = input("Купить еду?:")
        if a == "Да":
            water + 10
            cash = - 10
        else:
            water - 10
            time.sleep(2)



