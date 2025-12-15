# Retail Shopping Application
# Covers Coding Challenges 25 to 33

PROMO_CODE = "PROMO10"
MIN_PURCHASE = 500

grand_total = 0.0
total_quantity = 0

print("=== Retail Shopping Application ===")

# Coding Challenge 25 & 26
# Basic Item Entry, Iterative Entry, and Grand Total
while True:
    code = input("\nEnter item code (or 'q' to finish): ")
    if code.lower() == 'q':
        break

    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    item_total = quantity * price
    total_quantity += quantity

    # Coding Challenge 30: Promotional Discount on Items
    if code.upper() == PROMO_CODE:
        promo_discount = item_total * 0.10
        item_total -= promo_discount
        print("Promotional discount (10%) applied:", promo_discount)

    grand_total += item_total
    print("Item total:", item_total)

print("\nSubtotal:", grand_total)

# Coding Challenge 27: Purchase & Quantity Discounts
if grand_total > 10000:
    discount = grand_total * 0.10
    grand_total -= discount
    print("Bulk purchase discount (10%):", discount)

if total_quantity > 20:
    qty_discount = grand_total * 0.05
    grand_total -= qty_discount
    print("Quantity discount (5%):", qty_discount)

# Coding Challenge 28: Membership Discount
member = input("Is the customer a member? (y/n): ")
if member.lower() == 'y':
    member_discount = grand_total * 0.02
    grand_total -= member_discount
    print("Membership discount (2%):", member_discount)

# Coding Challenge 29: Tax Calculation
if grand_total < 5000:
    tax_rate = 0.05
elif grand_total <= 20000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

tax_amount = grand_total * tax_rate
grand_total += tax_amount
print("Tax applied:", tax_amount)

# Coding Challenge 31: Payment Mode Rules
payment_mode = input("Payment mode (cash/card): ").lower()
surcharge = 0.0

if payment_mode == "card":
    surcharge = grand_total * 0.02
    grand_total += surcharge
    print("Credit card surcharge (2%):", surcharge)

# Coding Challenge 32: Minimum Purchase Requirement
print("\nFinal Amount:", grand_total)

if grand_total < MIN_PURCHASE:
    print("Minimum purchase of ₹500 not met.")
    print("Invoice cannot be generated.")
else:
    # Coding Challenge 33: Loyalty Points
    loyalty_points = int(grand_total // 100)

    print("\n===== INVOICE GENERATED =====")
    print("Total Quantity:", total_quantity)
    print("Payment Method:", payment_mode.capitalize())
    print("Final Payable Amount: ₹", grand_total)
    print("Loyalty Points Earned:", loyalty_points)
