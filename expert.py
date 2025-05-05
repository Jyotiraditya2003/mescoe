# Define a simple rule-based Expert System for disease diagnosis

# A dictionary of diseases and their symptoms (in reality, this would be much more complex)
diseases = {
    "Flu": {"fever", "headache", "cough", "body aches"},
    "Cold": {"cough", "sore throat", "runny nose", "sneezing"},
    "COVID-19": {"fever", "cough", "shortness of breath", "fatigue", "loss of taste or smell"},
    "Malaria": {"fever", "chills", "sweating", "headache", "nausea"},
    "Chickenpox": {"fever", "itchy rash", "blisters", "headache"}
}

# Extract all unique symptoms from all diseases, ensuring no duplicates.
all_symptoms = set()
for symptom_set in diseases.values():
    all_symptoms.update(symptom_set)

# Function to ask the user for symptoms and diagnose
def diagnose():
    print("Welcome to the Hospital Expert System.")
    print("Please answer the following questions with 'yes' or 'no'.")

    # Initialize a set to store symptoms entered by the user
    user_symptoms = set()

    # Ask about all known symptoms
    for symptom in all_symptoms:
        answer = input(f"Do you have {symptom}? (yes/no): ").lower()
        if answer == 'yes':
            user_symptoms.add(symptom)

    # Diagnose disease based on symptoms
    matched_diseases = []
    # Check which diseases match user's symptoms
    for disease, disease_symptoms in diseases.items():
        if disease_symptoms.issubset(user_symptoms):  # If the user's symptoms match a disease
            matched_diseases.append(disease)

    if matched_diseases:
        print("\nBased on your symptoms, you may have the following diseases:")
        for disease in matched_diseases:
            print(f"- {disease}")
    else:
        print("\nSorry,  no disease could be confidently diagnosed based on the symptoms.")
        print("It is recommended to consult a doctor for further tests and evaluation.")
# Main function to start the expert system
if __name__ == "__main__":
    diagnose()

# def evaluate_employee():
#     print("🔍 Employee Performance Evaluation System\n")

#     # Input section
#     attendance = input("1. Attendance (Good / Average / Poor): ").strip().lower()
#     project = input("2. Project Completion (On Time / Delayed / Incomplete): ").strip().lower()
#     teamwork = input("3. Teamwork (Excellent / Good / Poor): ").strip().lower()
#     punctuality = input("4. Punctuality (Always on time / Often late): ").strip().lower()

#     # Score system
#     score = 0

#     # Attendance score
#     if attendance == "good":
#         score += 3
#     elif attendance == "average":
#         score += 2
#     elif attendance == "poor":
#         score += 0

#     # Project completion score
#     if project == "on time":
#         score += 3
#     elif project == "delayed":
#         score += 1
#     elif project == "incomplete":
#         score += 0

#     # Teamwork score
#     if teamwork == "excellent":
#         score += 3
#     elif teamwork == "good":
#         score += 2
#     elif teamwork == "poor":
#         score += 0

#     # Punctuality score
#     if punctuality == "always on time":
#         score += 2
#     elif punctuality == "often late":
#         score += 0

#     # Decision logic
#     print("\n📊 Evaluation Result:",score)
    
#     if score >= 9:
#         print("⭐ Performance: Excellent")
#     elif score >= 6:
#         print("✅ Performance: Good")
#     elif score >= 3:
#         print("⚠️ Performance: Needs Improvement")
#     else:
#         print("❌ Performance: Poor")

# # Run the expert system
# evaluate_employee()
