# This program reads daily step counts, calculates the average steps, counts active days, and displays the final report.

# Define the global constant ACTIVE_DAY_STEPS with the value 8000 outside every function
ACTIVE_DAY_STEPS = 8000

def get_steps(num_days):
    """Reads num_days whole-number step counts using a loop, stores them in a new list, and returns the list."""
    steps_list = []
    for i in range(num_days):
        step_count = int(input(f"Enter step count for day {i + 1}: "))
        steps_list.append(step_count)
    return steps_list

def calculate_average_steps(steps):
    """Receives the list and returns the average number of steps."""
    if not steps:
        return 0.0
    return sum(steps) / len(steps)

def count_active_days(steps, active_day_steps):
    """Returns how many step counts are at least the supplied target."""
    active_count = 0
    for step_count in steps:
        if step_count >= active_day_steps:
            active_count += 1
    return active_count

def display_report(average_steps, active_days):
    """Prints the average to one decimal place and the number of active days[cite: 3]."""
    print("\n--- Daily Steps Report ---")
    print(f"Average steps: {average_steps:.1f}")[cite: 3]
    print(f"Active days: {active_days}")[cite: 3]

# Main program execution
def main():
    NUM_DAYS = 5[cite: 3]
    step_records = get_steps(NUM_DAYS)[cite: 3]
    average_steps = calculate_average_steps(step_records)[cite: 3]
    active_days = count_active_days(step_records, ACTIVE_DAY_STEPS)[cite: 3]
    display_report(average_steps, active_days)[cite: 3]

if __name__ == "__main__":
    main()
