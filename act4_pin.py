#Hannielen Faye Q. Caraig
#BMET 2101

CORRECT_PIN = "1234"
tries = 0
granted = False

while tries < 3 and not granted:
    pin = input("PIN: ")
    tries += 1
    if pin == CORRECT_PIN:
        granted = True

if granted:
    print("Access granted")
else:
    print("Card blocked")