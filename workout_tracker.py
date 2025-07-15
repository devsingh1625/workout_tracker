# Test git comment
workouts = [
    {"Exercise": "Lifting", "Duration": 40, "Completed": True},
    {"Exercise": "Running", "Duration": 40, "Completed": False}
]

# First round of user input
one_exercise = input("What is your exercise's name? ")
one_duration = int(input("How long did it take you to do the exercise? "))
one_complete = input("Did you complete it? yes/no: ")

if one_complete.lower() == "yes":
    new_complete = True
else:
    new_complete = False

new_workout = {
    "Exercise": one_exercise,
    "Duration": one_duration,
    "Completed": new_complete
}

workouts.append(new_workout)

# Loop to keep adding more exercises
while True:
    exercise = input("Enter another exercise (or type 'exit' to stop): ")
    if exercise.lower() == 'exit':
        break

    duration = int(input("How long did it take you in minutes: "))
    completed_input = input("Did you complete the workout (yes/no)? ").lower()

    if completed_input == "yes":
        complete = True
    else:
        complete = False

    new_workout = {
        "Exercise": exercise,
        "Duration": duration,
        "Completed": complete
    }

    workouts.append(new_workout)

# Final output
print("\nUpdated Workout List:")
for x in workouts:
    if x["Completed"] == True:
        print(x["Exercise"], "-", x["Duration"], "min -", "Completed:", "Yes")
    else:
        print(x["Exercise"], "-", x["Duration"], "min -", "Completed:", "No")
