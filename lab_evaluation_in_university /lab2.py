cinema_name= input("Enter cinema name: ")
number_of_screenings = int(input("Enter the number of screenings: "))

total_tickets=0
high_screenings =0
low_screenings =0

for i in range(number_of_screenings):
    number_of_tickets = int(input(f"Enter the number of tickets sold for screen {i+1}: "))
    total_tickets+=number_of_tickets
    if(number_of_tickets>=50):
        high_screenings+=1
    else:
        low_screenings+=1
    
average_tickets = total_tickets / number_of_screenings

if(total_tickets>= 300 and average_tickets>=60):
    performance = "Excellent performance!"
elif(total_tickets>= 200):
    performance = "Good performance!"
elif(total_tickets>= 100):
    performance = "Need improvement!"
else:
    performance = "Low Sales!"

if total_tickets>= 300:
    target = "Target Achieved!"
else:
    target = "Target Not Achieved!"
    
print("Summary")
print("Cinema Name:", cinema_name)
print("Total Tickets Sold:", total_tickets)
print(f"Average Tickets per Screening: {average_tickets:.2f}")
print("High Screenings (>=50 tickets):", high_screenings)
print("Low Screenings (<50 tickets):", low_screenings)
print("Performance:", performance)
print("Target Status:", target)
