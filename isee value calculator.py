def calculate_isee(isr, isp, family_size):
    # isee = annual income + 20% of (bank and real estate) / equivalence scale 
    equivalence_scale = {1: 1.00, 2: 1.57, 3: 2.04, 4: 2.46, 5: 2.85}
    scale = equivalence_scale.get(family_size, 3.50)  # default 3.50 for 6+ members
    ise = isr + 0.20 * isp  # ISE = income + 20% of total assets
    isee = ise / scale
    return round(isee, 2)

# === Input section ===
income_eur = float(input("Type your annual income in EUR: "))
bank_money_eur = float(input("Type your total bank assets in EUR: "))
real_state_eur = float(input("Type your real estate value in EUR: "))
family_members = int(input("Enter number of family members: "))

# Total assets = bank + real estate
assets_eur = bank_money_eur + real_state_eur

# Calculate ISEE
estimated_isee = calculate_isee(income_eur, assets_eur, family_members)
print(f"\nEstimated ISEE Parificato: €{estimated_isee}")





