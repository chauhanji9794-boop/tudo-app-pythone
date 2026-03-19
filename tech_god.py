# HEALTH ASSISTANT APP

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Function to give BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😟"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 😊"
    elif 25 <= bmi < 29.9:
        return "Overweight 😐"
    else:
        return "Obese ⚠️"


# Function for health tips
def health_tips():
    print("\n🩺 Health Tips:")
    print("1. Drink enough water 💧")
    print("2. Exercise daily 🏃")
    print("3. Eat balanced diet 🥗")
    print("4. Sleep 7-8 hours 😴")


# Function for symptom checker (basic)
def symptom_checker(symptom):
    symptom = symptom.lower()

    if "fever" in symptom:
        return "You may have an infection. Stay hydrated and consult a doctor."

    elif "headache" in symptom:
        return "It could be stress or dehydration. Rest and drink water."

    elif "cough" in symptom:
        return "Possible cold or flu. Monitor symptoms."

    else:
        return "Not sure. Please consult a healthcare professional."


# Main program
def main():
    print("🏥 Welcome to Health Assistant App 🏥")

    while True:
        print("\nChoose an option:")
        print("1. Calculate BMI")
        print("2. Health Tips")
        print("3. Symptom Checker")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (meters): "))

            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {category}")

        elif choice == "2":
            health_tips()

        elif choice == "3":
            symptom = input("Enter your symptom: ")
            result = symptom_checker(symptom)
            print(result)

        elif choice == "4":
            print("Stay healthy! Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


# Run app
if __name__ == "__main__":
    main()