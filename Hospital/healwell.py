# HealWell Care Hospital Billing System

# Level 7: Admin Sets Services
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

# Level 1: Patient Details
patient_name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# Level 2: Display Services
print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i + 1}. {services[i]} - ₹{costs[i]}")

selection = input(
    "\nSelect services (comma separated numbers, e.g. 1,4): "
)

selected_indexes = [int(x.strip()) for x in selection.split(",")]

selected_services = []
selected_costs = []

# Level 3: Fetch Selected Services & Costs
for index in selected_indexes:
    if 1 <= index <= len(services):
        selected_services.append(services[index - 1])
        selected_costs.append(costs[index - 1])

# Level 4: Calculate Subtotal
subtotal = sum(selected_costs)

# Level 8: Apply Discounts
discount = 0

if age >= 60:
    discount += subtotal * 0.10

# High Bill Discount (5%)
if subtotal > 5000:
    discount += (subtotal - discount) * 0.05

discounted_subtotal = subtotal - discount

# Level 5: Apply GST (18%)
gst = discounted_subtotal * 0.18
grand_total = discounted_subtotal + gst

# Level 6: Generate Invoice
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("Patient Information:")
print(f"Name   : {patient_name}")
print(f"Age    : {age}")
print(f"Gender : {gender}")
print(f"Contact: {contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i + 1}. {selected_services[i]}: ₹{selected_costs[i]}")

print(f"\nSubtotal        : ₹{subtotal}")
print(f"Discount Applied: ₹{discount:.2f}")
print(f"GST (18%)       : ₹{gst:.2f}")
print(f"Grand Total     : ₹{grand_total:.2f}")

print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")
