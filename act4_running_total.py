count = 0 
total = 0

price = float(input("Price (0 to stop): "))
while price != 0:
    count += 1
    total += price
    price = float(input("Price (0 to stop): "))

print(f"items: {count} Total: {total:.2f}")
if count > 0:
    print(f"Average: {total / count:.2f}")