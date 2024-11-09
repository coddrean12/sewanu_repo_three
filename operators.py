# Arithmetic operators
a = 6
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Arithmetic operators end


# Comparision / Relational Operators

a = 5  
b = 8
c = 5
d = "8"

print(a > b)
print(a < b)
print(a >= c)
print(c <= b)
print(a == c)
print(b != d)

# Comparision / Relational Operators end

# Compound assignment Operators

num = 4
num1 = 5
result = num + num1
result += num
print(result)
result -= num1
print(result)

# Compound assignment Operators end

coding = True
if coding == True:
    print("Yes we are coding in python")
else:
    print("No we are not coding in python")

#Logical operators

i_am_learning_python = True
i_am_10_yrs_old = False
i_am_learning_operators = True
i_hate_coding = False

if i_am_learning_python and i_am_10_yrs_old == True:
    print("I am ten years old learing python.")
else:
    print("I am not either learning python or not 10 yrs old")

if i_hate_coding or i_am_learning_operators == True:
    print("I am ten years old learing python.")
else:
    print("I am not either learning python or not 10 yrs old")
print(not i_am_10_yrs_old)

# Logical operators end

# Membership operators

letter1 = "b"
letter2 = "q"
text = "I am learning Python"

if letter1 in text:
    print(f"{letter1} is in {text}.")
else:
    print(f"{letter1} is not in {text}.")

if letter2 not in text:
    print(f"{letter2} is not in {text}")
else:
    print(f"{letter2} is in {text}")

# Membership operators end

# Identity operators

x = 20
y = 30

if x is y:
    print("x & y SAME identity")

y = 30

if x is not y:
    print("x & y DIFFERENT identity")

# Identity operators end

course_status = input("Please input your coarse status for the Python coarse")
if course_status == "in progress":
    print("I am happy that we have started")
    print("Continue well")
elif course_status == "not started":
    print("The python course will teach you to python to create simple applications")
    print("I advice you to start now")
elif course_status == "finished":
    print("Thanks for going through the course.")
    print("I how you are building applications with your knowledge")
elif course_status == "start but not in progress":
    print("Hurry up and continue")
    print("It is very vital")
else:
    print("You put in a wrong courase")