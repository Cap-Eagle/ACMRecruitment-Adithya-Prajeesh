sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)


n=100
Sum_of_squares = n*(n+1)*(2*n+1)/6
sum2 = (n*(n+1))/2
square_of_sum = sum2**2
diff = square_of_sum-Sum_of_squares
print(diff)