
# coding: utf-8

# In[ ]:


def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select operations")
print("1)add")
print("2)sub")
print("3)mult")
print("4)div")

choice = input("enter choice")

num1 = int(input("1st num"))
num2 = int(input("2nd num"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
           print(num1, "-", num2, "=", sub(num1, num2))
elif choice == '3':
           print(num1, "*", num2, "=", mult(num1, num2))
elif choice == '4':
           print(num1, "/", num2, "=", div(num1, num2))
else:
           print("invalid input")
           
           


# In[ ]:




