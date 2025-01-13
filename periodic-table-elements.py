# installing required packages
# pip install periodictable

# importing required packages
import periodictable

# main logic
def getInfo(symbol):
    if not periodictable.elements.symbol(symbol):
        print("Invalid Symbol")
        return
    
    element = periodictable.elements.symbol(symbol)
    print(f"Element : {element.name}")
    print(f"Symbol  : {element.symbol}")
    print(f"Density : {element.density}")
    print(f"Atomic Number : {element.number}")
    print(f"Atomic Weight : {element.mass}")

# taking input and showing output
ip_symbol = str(input("Enter the element's symbol: "))
ip_symbol = ip_symbol[:1].upper()+ip_symbol[1:].lower() # first letter in CAPS and rest in LOWER as required by library
print("Entered Symbol is: ",ip_symbol)
getInfo(ip_symbol)