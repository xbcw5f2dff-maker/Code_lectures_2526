try:
    number = float(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex: #valueerror; number is tekst en je geeft die error de naam ex zodat je bij de print("excpetion:" dus dat is lett tekst, als je dan ex zet dan zal hij nog zeggen could not convert string to float: drie
    print("Exception:", ex)


