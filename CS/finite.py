'''
state = 0

print("Symbol menu:")
print("1. hello world")
print()

symbol = str(input("Enter a symbol> "))

if state == 0 and symbol == "1":
    state = 1
    print("Hello world!")
else:
    print("The symbol doesn't exist")

# Task 1

def take_return_bin(s):
    s = int(input("Enter binary string> "))
    return s

s = 0
take_return_bin(s)
print(s)

# Task 2

binary = int(input("Enter binary string> "))

new_binary = [0, 0, 0, 0]

i = 0
for i in len(str(binary)):
    if binary[i] == "0":
        new_binary += 1
    if binary[i] == "1":
        new_binary += 0

print(new_binary)
'''

# Task 10
def menu():
    gateOpen = False
    print("1. Use a proper ticket")
    print("2. Use an expired ticket")
    action = int(input("> "))

if action == 1:
    print("You have entered through the gate")

if action == 2: 
    print("You couldn't go through the gate")
    
    print("1. Buy a ticket")
    print("2. Walk away in shame")
    ticketBuying = int(input("> "))
    
    if ticketBuying == 1:
        print("You have entered through the gate")

    if tickerBuying == 1:
        menu()


