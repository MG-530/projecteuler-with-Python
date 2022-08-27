end_number = 4000000
sum_fib_o = 2
first = 1
second = 2
fib = [1, 2]
while second <= end_number:  # Here is for select end number
    first = second + first
    if first >= end_number:
        break
    fib.append(first)
    second = first + second
    if second >= end_number:
        break
    fib.append(second)
    if second % 2 == 0:
        sum_fib_o += second
    elif first % 2 == 0:
        sum_fib_o += first
print(fib)
print(sum_fib_o)
