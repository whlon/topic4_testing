"""
Exercise 4.2B -> fault order Processor

program processes a simple customer order,
this program contains several defects that ust be identified, 
corr and corrected suing debugging priocess
REQUIREMENTS
Order calculation rules:
1. subtotal = price * quantity
50*5

2. a 10% discount when subtotal is greater than 100, discount should 
be calculated from the subtotal
250 - 25 = 225
3. shipping in 5 when the amount after discount is below 50
4. quantity must be greater than 0
5. price must be negative
6. funcion should return the final order

"""
def calculate_order_order(price, quantity):
    subtotal = price + quantity
    if (subtotal > 100):
