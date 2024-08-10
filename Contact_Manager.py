import pandas as pd
import os

# defines file and columns
filename = "contacts.csv"
columns = ["first_name", "last_name", "phone", "email", "address"]

# checks if file exists and 
file_exists = os.path.isfile("contacts.csv")
write_header = not file_exists or os.path.getsize("contacts.csv") == 0

# creates csv file called "contacts" and a mode to add new data
with open("contacts.csv", mode="a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    
    if write_header:    # writes header only when neeeded
        writer.writeheader()
    
    
    while True:
        user_input = int(input("1. Add new contacts \n2. View existing contacts \n3. Update contact details \n4. Delete contacts"))
    
        if user_input == 1:
            pass
            
        elif user_input == 2:
            pass
        elif user_input == 3:
            
            pass
                
        elif user_input == 4:
            pass
            


        continue_input = input("Do you want to continue? Y/N").strip().lower()
        if continue_input == "N" or continue_input == "n":
            print("Thanks for your time.")
            break
        
    
    

    

