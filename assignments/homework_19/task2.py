def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be zero")
    current = start
    
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step

#Перевірка
print(list(in_range(0, 10, 2)))
print(list(in_range(10, 0, -2)))