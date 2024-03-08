price = input("Enter the original price")
price = int(price)

discount_percent = input("Enter the percentage discount")
discount_percent = int(discount_percent)

def calculate_discount(original_price, discount_percent_given):
    discount = (discount_percent_given/100) * original_price
    return original_price - discount

new_price = calculate_discount(price, discount_percent)
print(new_price)

