# 🚨 Don't change the code below 👇
print("Welcome to the health Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_names = name1+name2
lower_case = combine_names.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e 
l = lower_case.count("l")
o = lower_case.count("0")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e
add = str(true)+str(love)
new_add = int(add)
if new_add <10 or new_add >90:
    print(f"Your score is {add}, you go together like coke and mentos.")
elif new_add >= 40 and new_add<=50:
    print(f"Your score is {add}, you are alright together. ")
else:
    print(f"Your score is {add}.") 
 