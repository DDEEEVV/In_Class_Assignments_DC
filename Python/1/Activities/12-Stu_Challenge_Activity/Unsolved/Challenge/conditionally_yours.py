"""
Conditionally Yours

Pseudocode:


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = 290.31

# Create integer variable for current_price
current_price = 352.28

# Create float for threshold_to_buy
increase = current_price - original_price
percent_increase = increase / original_price * 100

if percent_increase < 20:
    print("sell")

# Create float for threshold_to_sell
increase = current_price - original_price
percent_increase = increase / original_price * 100

if percent_increase > 20:
    print("buy")

# Create float for portfolio balance


# Create float for balance check


# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price


# Calculate percent increase


# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price was ${current_price}")

# Print percent increase
print(f"Netflix's percentage increse is %{round(percent_increase,2)}")

# Determine if stock should be bought or sold


# Print recommendation
print("Recommendation: " + recommendation)
print()
print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance variable as a float


# Declare balance_check variable
balance_check = balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${balance} in excess equity available in your portfolio.")

# IF-ELSE Logic to determine recommendation based off of balance check
