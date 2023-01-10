def is_happy_num(n):
    past=set()
    while n !=1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print(is_happy_num(49))
print(is_happy_num(156))
print(is_happy_num(139))

