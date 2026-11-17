#Gym Reception System 

name = input("Enter name: ")
age = int(input("Enter age: "))
classes = int(input("Enter classes: "))
fee = float(input("Enter fee: "))
active = True

classes += 1

print("Name:", name)
print("Age:", age)
print("Classes:", classes)
print("Fee:", fee)
print("Active:", active)

print("e in name:", "e" in name)

if age > 15 and classes < 4 and active is True:
    print("Eligible")
else:
    print("Not Eligible")