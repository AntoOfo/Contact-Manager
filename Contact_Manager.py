import pandas as pd
import os

# defines file and columns
filename = "contacts.csv"
columns = ["first_name", "last_name", "phone", "email", "address"]

df = pd.DataFrame(columns=columns)
    
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
        
    
    

    

