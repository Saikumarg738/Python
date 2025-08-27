# Provided user data
gross_salary = 1088928

# Home loan EMI components (April 2024 - March 2025)
principal_paid = 65064.27
interest_paid = 433881.7

# Other savings eligible under 80C
postoffice_lic_savings = 164704

# 80C limit
max_80C = 150000

# Section 24(b) limit (interest on home loan)
max_24b = 200000

# Calculate eligible deductions
eligible_80C = min(principal_paid + postoffice_lic_savings, max_80C)
eligible_24b = min(interest_paid, max_24b)

# Total deductions under old regime
total_deductions_old_regime = eligible_80C + eligible_24b

# Taxable income under old regime
taxable_income_old = gross_salary - total_deductions_old_regime

# Function to compute tax as per old regime slabs (for FY 2024-25)
def compute_old_regime_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3
    return tax

# Calculate tax under old regime
tax_old_regime = compute_old_regime_tax(taxable_income_old)

# New tax regime: no 80C or 24b deductions, flat slabs
def compute_new_regime_tax(income):
    tax = 0
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.1
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (income - 1200000) * 0.2
    else:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (300000 * 0.2) + (income - 1500000) * 0.3
    return tax

tax_new_regime = compute_new_regime_tax(gross_salary)
tax_savings = tax_new_regime - tax_old_regime

# Final results
print(f"Eligible 80C Deduction: ₹{eligible_80C}")
print(f"Eligible 24(b) Deduction: ₹{eligible_24b}")
print(f"Total Deductions (Old Regime): ₹{total_deductions_old_regime}")
print(f"Taxable Income (Old Regime): ₹{taxable_income_old}")
print(f"Tax (Old Regime): ₹{tax_old_regime}")
print(f"Tax (New Regime): ₹{tax_new_regime}")
print(f"Tax Saved by Choosing Old Regime: ₹{tax_savings}")
