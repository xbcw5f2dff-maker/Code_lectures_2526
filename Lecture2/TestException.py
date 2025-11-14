def main():
    try:
        number1 = int(input("Enter an integer: "))      
        number2 = int(input("Enter an integer: "))      
        result = number1 / number2 #als dit geen probleem geeft dan springt het naar else, wel probleem => 1 van de excepts wordt uitgevoerd 
        print("Result is " + str(result))
    except ZeroDivisionError: # Catch zero divisor error
        print("Division by zero!")
    except:
        print("Something wrong in the input")
    else:
        print("No exceptions")
    finally: #wordt altijd uitgevoerd 
        print("The finally clause is executed")

main()
