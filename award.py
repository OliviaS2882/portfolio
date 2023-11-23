#Store times for each event as integer variables.
swimming_time = int(input("What time did you achieve in the swimming event to the nearest minute?:\n"))
cycling_time = int(input("What time did you achieve in the cycling event to the nearest minute?:\n"))
running_time = int(input("What time did tou achieve in the running race to the nearset minute?:\n"))

#calculate total time and store as a new variable.
total_time = swimming_time + cycling_time + running_time

#Output total time and award achieved.
print(f"Your total time taken to complete the triathlon was {total_time} minutes.")

if total_time <= 100:
    print("You achieved Provincial Colours, well done!")
elif total_time <= 105:
    print("You achieved Provincial Half Colours, well done!")
elif total_time <= 110:
    print("You achieved a Provicial Scroll.")
else:
    print("You did not qualify for an award, better luck next time.")
