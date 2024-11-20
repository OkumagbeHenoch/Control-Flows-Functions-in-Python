# # 1.
# # def large_power(base , exponent):    
 
# #  if base ** exponent > 5000 :
# #     print(True)
# #  else :
# #     print(False)
    
    
# #     print("Input two numbers the first takes the base value and the latter the exponent value")

# # large_power(base=int(input()) , exponent=int(input()))

# 2.
# def divisible_by_ten(num):
#   if num % 10 == 0 :
#     print(True)

#   else:
#     print(False)

# print("Input just one number and let the code check if it is divisible by 10")
# divisible_by_ten(num =int(input()))
    
# def calculate_discount(price, discount_percent):
#  if discount_percent ==  20% or > 20%: 
#         price 

# price=int(input())
# discount_percent=int(input())
         
# print("Input two values first the original price, the latter discount percentage")
# calculate_discount()

# def calculate_discount(price, discount_percent):
#     """
#     Calculate the final price after applying a discount.

#     :param price: The original price of the item (float or int)
#     :param discount_percent: The discount percentage (float or int)
#     :return: The final price after applying the discount, or the original price
#              if the discount percentage is less than 20%.
#     """
#     if discount_percent >= 20:
#         discount_amount = (discount_percent / 100) * price
#         return price - discount_amount
#     return price


# # Prompt the user for input
# try:
#     original_price = float(input("Enter the original price of the item: "))
#     discount_percentage = float(input("Enter the discount percentage: "))

#     # Calculate the final price
#     final_price = calculate_discount(original_price, discount_percentage)

#     # Print the result
#     if discount_percentage >= 20:
#         print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
#     else:
#         print(f"No discount applied. The original price is: {original_price:.2f}")
# except ValueError:
#     print("Invalid input. Please enter numeric values for price and discount percentage.")



def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        print(price - (discount_percent/100 * price))

    else:
        print(price)

calculate_discount(price=int(input("Original price :")) , discount_percent=int(input("Discount percentage :")))
