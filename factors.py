n = int(input("Enter any number:"))
sum1 = 0

#Loop through all numbers less than 'n' to find divisors
for i in range(1,n):
                if n%i == 0:
                                sum1 += i  #Add divisor to sum1

#Check if the sum of divisors equals the original number

if sum1 == n:
                print("the number is a perfect number")
else:
                print("the number is not a perfect number")
