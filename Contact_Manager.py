import pandas as pd
import os

# defines file and columns
filename = "contacts.csv"
columns = ["first_name", "last_name", "phone", "email", "address"]

df = pd.DataFrame(columns=columns)   
    
while True:
    user_input = int(input("1. Add new contacts \n2. View existing contacts \n3. Update contact details \n4. Delete contacts"))
       
    if user_input == 1:
            user_data = {col: input(f"Enter {col}: ") for col in columns} # user_data = {first_name: "John"}
            new_entry = pd.DataFrame([user_data], columns=columns)   # converts user data to df
            df = pd.concat([df, new_entry], ignore_index=True)  # adds new entry to df
            df.to_csv(filename, index=False)    # save df to file
            
            print("Contact added successfully.")
            
    elif user_input == 2:
        if df.empty:
            print("No contacts found")
        else:
            print("Here's all the existing contacts: ")
            print(df)
            
    elif user_input == 3:
        name_to_update = input("Enter the contact's first name to update: ")
        contact_index = df[df["first_name"] == name_to_update].index # finds index of contact who has the first name
        
        if not contact_index.empty:
             print("Found contact: ", df.loc[contact_index[0]]) # prints the contact details
             field_to_update = input(f"Enter the field to update ({', '.join(columns)}): ") 
             if field_to_update in columns: 
                df.at[contact_index[0], field_to_update] = input(f"Enter the new value for {field_to_update}: ")    # updates the field
                df.to_csv(filename, index=False)
                print("Contact updated successfully.")
                
             else:
                print("Invalid field name.")
        else:
            print("Contact not found.")
                
    elif user_input == 4:
        pass
            


    continue_input = input("Do you want to continue? Y/N").strip().lower()
    if continue_input == "N" or continue_input == "n":
        print("Thanks for your time.")
        break
        
    
    

    

