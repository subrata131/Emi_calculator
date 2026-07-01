loan_amount=int(input("Enter Loan amount:"))
interest=float(input("Enter Interest rate (%):"))
year=int(input("Enter Loan Tenure(Years):"))

#convert
monthly_interest=interest/(12*100)
months=year*12

#emi calculator rule
emi=(loan_amount*monthly_interest*(1+monthly_interest)**months)/((1+monthly_interest)**months-1)

#calculation
total_payment=emi*months
total_interest=total_payment-loan_amount

#printing 

print("\n.....EMI DETAILS.....")
print(f"Loan Amount: {loan_amount:,.2f}")
print(f"Monthly Emi: {emi:,.2f}")
print(f"Total Payment: {total_payment:,.2f}")
print(f"Total Interest: {total_interest:,.2f}")