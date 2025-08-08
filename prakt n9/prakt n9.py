def min_steps(x, y):
    dist = y - x
    step = 1
    total = 0
    steps = 0

    while total < dist:
        steps += 1
        total += step
        if steps % 2 == 0:
            step += 1
    return steps


x, y = map(int, input("Введіть x та y через пробіл: ").split())
print("Мінімальна кількість кроків:", min_steps(x, y))
input()  
