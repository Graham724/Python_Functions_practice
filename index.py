#Question 1
def say_hello():
    print("Hello!")

say_hello()

#Question 2
def pack(thing1, thing2, thing3):
    return [thing1, thing2, thing3]

print(pack("thing1","thing2","thing3"))

#Question 3
def eat_lunch(lunch_list):
  if len(lunch_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(lunch_list)):
      if i == 0:
        print(f"First I eat {lunch_list[0]}")
      else:
        print(f"Next I eat {lunch_list[i]}")


eat_lunch(["Sandwich","Cheeseburger","Pizza","Noodles","Fries"])