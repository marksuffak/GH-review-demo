patients = [[70, 1.8], [80, 1.9], [150, 1.7], [90, 2.8]]

def calculate_bmis(weight, hweight):
    return wheight / (hweight ** 2)

for patient in patients:
    weight, height = patient[0], patient[1]
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f", % bmi)

