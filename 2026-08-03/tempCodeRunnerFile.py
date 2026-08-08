bills = [100, 200, 300, 400, 500]
total = 0
while total < 600:
    for bill in bills:
        total += bill
print(f'total {total}')
