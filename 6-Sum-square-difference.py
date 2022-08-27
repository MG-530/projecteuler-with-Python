sumx=0
sum_of_the_squares=0
for x in range (1,101):
    sumx+=x
square_of_the_sum=sumx**2
print(square_of_the_sum)
for y in range (1,101):
    sum_of_the_squares+=y**2
print(sum_of_the_squares)
difference =square_of_the_sum-sum_of_the_squares
print(difference)