import secrets, time, random
from colorama import Fore

address = input("Input your BTC address here: ")

def findAccounts():
    for i in range(150):
        print(Fore.RED + secrets.token_hex(nbytes=32), ' - 0 BTC')
        time.sleep(0.08)

    BTCAmount = random.uniform(0.002, 1.000)
    print(Fore.GREEN + secrets.token_hex(nbytes=32), ' - ', BTCAmount, "BTC")
    print(Fore.WHITE + "Found unused BTC, do you want to request it? (Y or N)")

findAccounts()

request = input("")
if request == "y":
    print(Fore.YELLOW + "Sending unused BTC to " + address + "...") 
    time.sleep(5)
    print(Fore.GREEN + "BTC succesfullt sent to " + address)
    time.sleep(2)
    print(Fore.GREEN + "Trying to search bitcoin...")
    findAccounts()

exit()