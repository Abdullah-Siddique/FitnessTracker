# project.py
import matplotlib.pyplot as plt
import pandas as pd

# Global variables
workouts_data = []
meals_data = []
water_intake_data = []
sleep_data = []

# Function to track workouts
def track_workouts(exercise_type, duration, intensity):
    workout = {'Exercise Type': exercise_type, 'Duration': duration, 'Intensity': intensity}
    workouts_data.append(workout)
    print("Workout tracked successfully!")

# Function to log meals
def log_meals(food_type, portion_size, nutritional_info):
    meal = {'Food Type': food_type, 'Portion Size': portion_size, 'Nutritional Info': nutritional_info}
    meals_data.append(meal)
    print("Meal logged successfully!")

# Function to monitor water intake
def monitor_water_intake(amount):
    water_intake_data.append(amount)
    print("Water intake monitored successfully!")

# Function to track sleep patterns
def track_sleep_patterns(duration, quality):
    sleep = {'Duration': duration, 'Quality': quality}
    sleep_data.append(sleep)
    print("Sleep pattern tracked successfully!")

# Function to generate dashboard
def generate_dashboard():
    # Create DataFrame for each dataset
    workouts_df = pd.DataFrame(workouts_data)
    meals_df = pd.DataFrame(meals_data)
    water_intake_df = pd.DataFrame({'Water Intake': water_intake_data})
    sleep_df = pd.DataFrame(sleep_data)

    # Plotting graphs
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.bar(workouts_df['Exercise Type'], workouts_df['Duration'])
    plt.title('Workout Duration')
    plt.xlabel('Exercise Type')
    plt.ylabel('Duration (mins)')

    plt.subplot(2, 2, 2)
    plt.pie(meals_df['Portion Size'], labels=meals_df['Food Type'], autopct='%1.1f%%')
    plt.title('Meal Portion Distribution')

    plt.subplot(2, 2, 3)
    plt.plot(water_intake_df, marker='o')
    plt.title('Water Intake')
    plt.xlabel('Day')
    plt.ylabel('Water Intake (ml)')

    plt.subplot(2, 2, 4)
    plt.plot(sleep_df['Duration'], sleep_df['Quality'], marker='o')
    plt.title('Sleep Patterns')
    plt.xlabel('Duration (hrs)')
    plt.ylabel('Quality')

    plt.tight_layout()
    plt.show()

# Function for goal setting
def set_goals():
    print("Set your fitness goals here!")

# Function for reminder feature
def send_reminders():
    print("Sending reminders to stay active!")

# Main function
def main():
    print("Welcome to Fitness Tracker!")
    while True:
        print("\n1. Track Workouts\n2. Log Meals\n3. Monitor Water Intake\n4. Track Sleep Patterns")
        print("5. Generate Dashboard\n6. Set Goals\n7. Send Reminders\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            exercise_type = input("Enter exercise type: ")
            duration = int(input("Enter duration (mins): "))
            intensity = input("Enter intensity (low, medium, high): ")
            track_workouts(exercise_type, duration, intensity)
        elif choice == '2':
            food_type = input("Enter food type: ")
            portion_size = int(input("Enter portion size: "))
            nutritional_info = input("Enter nutritional information: ")
            log_meals(food_type, portion_size, nutritional_info)
        elif choice == '3':
            amount = int(input("Enter water intake (ml): "))
            monitor_water_intake(amount)
        elif choice == '4':
            duration = float(input("Enter sleep duration (hrs): "))
            quality = float(input("Enter sleep quality (1-10): "))
            track_sleep_patterns(duration, quality)
        elif choice == '5':
            generate_dashboard()
        elif choice == '6':
            set_goals()
        elif choice == '7':
            send_reminders()
        elif choice == '8':
            print("Exiting Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
# cd FitnessTracker
# python project.py
# python test_project.py