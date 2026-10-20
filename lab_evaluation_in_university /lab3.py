# This program reads five daily temperatures, calculates required statistics, and stores them in a tuple.

# Read five daily temperatures into a list using a loop and append()
temperatures = []
for i in range(5):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temperatures.append(temp)

# Calculate the lowest temperature, highest temperature, and average
lowest_temp = min(temperatures)
highest_temp = max(temperatures)
average_temp = sum(temperatures) / len(temperatures)

# Calculate how many readings are above 40 degrees
hot_days_count = 0
for temp in temperatures:
    if temp > 40:
        hot_days_count += 1

# Store the three statistics in a tuple in the required order
summary = (lowest_temp, highest_temp, average_temp)

# Display a labeled summary using f-strings, format average to two decimal places
print("\n--- Temperature Analysis Summary ---")
print(f"Entered temperatures: {temperatures}")
print(f"Lowest temperature: {lowest_temp}")
print(f"Highest temperature: {highest_temp}")
print(f"Average temperature: {average_temp:.2f}")
print(f"Readings above 40 degrees: {hot_days_count}")
print(f"Summary tuple: {summary}")
