import random
from datetime import datetime

def generate_bill(patient_name, doctor_name, patient_number):
    # Generate a random bill ID
    bill_id = random.randint(1000, 9999)
    
    # Current date
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Sample services and prices
    services = {
        "Consultation": 50.00,
        "Blood Test": 30.00,
        "X-Ray": 70.00,
        "Prescription": 15.00,
        "MRI Scan": 200.00
    }

    # Generate random services
    selected_services = random.sample(list(services.items()), random.randint(1, len(services)))
    total_amount = sum(price for service, price in selected_services)

    # Create the bill
    bill = f"""
    -------------------------
          DOCTOR BILL
    -------------------------
    Bill ID: {bill_id}
    Patient Name: {patient_name}
    Patient Number: {patient_number}
    Doctor Name: {doctor_name}
    Date: {date}
    
    Services Rendered:
    -------------------------
    """
    
    for service, price in selected_services:
        bill += f"{service}: ${price:.2f}\n"
    
    bill += "-------------------------\n"
    bill += f"Total Amount Due: ${total_amount:.2f}\n"
    bill += "-------------------------"

    return bill

# Example Usage
if __name__ == "__main__":
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    patient_number = input("Enter patient number: ")
    
    bill = generate_bill(patient_name, doctor_name, patient_number)
    print(bill)
