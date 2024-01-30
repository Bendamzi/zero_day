# Allocated char for various order
small_coffee = "small" 
medium_coffee = "medium"
large_coffee = "large"

# create variable for size
small = 2.00
medium = 3.00
large = 4.00
Extra = 1.00
No_extra = 0.00

# prompt the customer to enter their name
user_name = input("Hello there! kindly enter your name: ")
print("Welcome to Benjamin coffee shop")

while True:
    # prompt the customer to order
    order = input("What size of coffee are you ordering from us today; small,medium or large? ")

    # confirm the order for small size only
    if order == "small":
        print("Hello!", user_name, ", your order for small coffee size has been confirmed, your bill is: $%s" % (small))
        order = small
        break

    # confirm the order for medium size only
    elif order == "medium":
        print("Hello!", user_name , ", your order for medium coffee size has been confirmed, your bill is: $%s" % (medium))
        order = medium
        break
        
    # confirm the order for large size only
    elif order == "large":
        print("Hello!", user_name , ", your order for medium coffee size has been confirmed, your bill is $%s" % (large))
        order = medium
        break
    
    # error message for wrong input
    else:
        print("invalid input, choose either small or medium or large")
        
total_price = order
while True:
    extra_coffee = input("Do you want an extra? (Yes/No): ")

    if extra_coffee == "Yes":
        total_price += Extra
        break
    elif extra_coffee == "No":
        total_price += No_extra
        break
    else:
        print("Invalid input!, Please enter Yes or No.")


"""Display the total price"""
if total_price > 0:
    print(f"Your total price is: ${total_price:.2f}")

print("Order Completed")