input1 = input("input1: ")
input2 = input("input2: ")

print("\n")

if input1.isdigit():
    input1intcheck = input("Do you want input1 to be an int? (y/n) ").lower()
    if input1intcheck == "y":
        input1 = int(input1)
    elif input1intcheck != "y":
        input1floatcheck = input("Do you want input1 to be a float? (y/n) ").lower()
        if input1floatcheck == "y":
            input1 = float(input1)
else:
    print("Not digit.")
            
if input2.isdigit():
    input2intcheck = input("Do you want input2 to be an int? (y/n) ").lower() 
    if input2intcheck == "y":
        input2 = int(input2)
    elif input2intcheck != "y":
        input2floatcheck = input("Do you want input2 to be a float? (y/n) ").lower()
        if input2floatcheck == "y":
            input2 = float(input2)
else:
    print("Not digit.")


print("\n")

print(f"input1 = {input1} = {type(input1)}")
print(f"input2 = {input2} = {type(input2)}")

print("\n")

################################################################################################

if input1 == str(input1):
    print(f"Len input1 = {len(input1)}")
else:
    print(f"Not str")
    
if input2 == str(input2):
    print(f"Len input2 = {len(input2)}")
else:
    print(f"Not str")
    
print("\n")

word = input("Find word = ")

print("\n")

if input1 == str(input1):
    print(f"Find {word} input1 = {input1.find(word)}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Find {word} input2 = {input2.find(word)}")
else:
    print(f"Not str")

print("\n")

if input1 == str(input1):
    print(f"Capital input1 = {input1.capitalize()}")
else:
    print(f"Not str")

if input2 == str(input2):
   print(f"Capital input2 = {input2.capitalize()}")
else:
    print(f"Not str")

print("\n")

if input1 == str(input1):
    print(f"Lower input1 = {input1.lower()}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Lower input2 = {input2.lower()}")
else:
    print(f"Not str")

print("\n")

if input1 == str(input1):
    print(f"Upper input1 = {input1.upper()}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Upper input2 = {input2.upper()}")
else:
    print(f"Not str")

print("\n")
    
if input1 == str(input1):
    print(f"Isdigit input1 = {input1.isdigit()}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Isdigit input2 = {input2.isdigit()}")
else:
    print(f"Not str")

print("\n")

if input1 == str(input1):
    print(f"Isalpha input1 = {input1.isalpha()}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Isalpha input2 = {input2.isalpha()}")
else:
    print(f"Not str")

print("\n")

if input1 == str(input1):
    replace1 = input("Replace1 = ")
elif input2 == str(input2):
    replace1 = input("Replace1 = ")
if input1 == str(input1):
    replace2 = input("Replace2 = ")
elif input2 == str(input2):
    replace2 = input("Replace2 = ")

print("\n")

if input1 == str(input1):
    print(f"Replace input1 = {input1.replace(replace1, replace2)}")
else:
    print(f"Not str")

if input2 == str(input2):
    print(f"Replace input2 = {input2.replace(replace1, replace2)}")
else:
    print(f"Not str")

print("\n")

multiply = int(input("Multiply = "))

print("\n")

print(f"Multiply input1 = {input1*multiply}")

print(f"Multiply input2 = {input2*multiply}")

print("\n")


