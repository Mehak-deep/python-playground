def greet(name):
    return f"Hello,{name}! Lets get started."
print(greet("Mehak"))

def calculate_savings(monthly_amount, months):
    total = monthly_amount * months
    return total

print( f"Annual Saving: ${calculate_savings(500, 12):,}")
