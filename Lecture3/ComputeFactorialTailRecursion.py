def main():
    n = int(input("Enter a nonnegative integer: "))
    print("Factorial of", n, "is", factorial(n))

# Return the factorial for a specified number 
def factorial(n):
    return factorialHelper(n, 1) # Call auxiliary function
  
# Auxiliary tail-recursive function for factorial 
def factorialHelper(n, result):
    if n == 0:
        return result
    else:
        return factorialHelper(n - 1, n * result) # Recursive call

main() # Call the main function

#dus neem als vb n = 4 ; factorial(4)
#                            =>factorialHelper(4, 1)

#eerste oproep; n = 4, result = 1     (result start bij 1, dit is eigen aan de fucntie)
# n nt= 0 => we gaan verder
#return factorialHelper(3, 4 * 1)  => n - 1, n * result
#                            nieuw result = 4

#tweede oproep; n = 3, result = 4
# n nt= 0 => we gaan verder
#return factorialHelper(2, 3 * 4)
#                           nieuw result = 12

#derde oproep; n = 2, result = 12
# n nt=0 => we gaan verder
#return factorialHelper(1, 2 * 12)
#                           nieuw result = 24

#vierde oproep; n = 1, result = 24
# n nt= 0 => we gaan verder
#return factorialHelper(0, 1 * 24)
#                            nieuw result = 24

#vijfde oproep; n = 0, result = 24
# n = 0 => stopconditie 
#return result 
# = 24

