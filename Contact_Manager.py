import pandas as pd
import os

# defines file and columns
filename = "contacts.csv"
columns = ["first_name", "last_name", "phone", "email", "address"]

df = pd.DataFrame(columns=columns)   
while True:
    try:
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
            contacts_to_update = df[df["first_name"] == name_to_update] # index of contacts to update
    
            if not contacts_to_update.empty:
                print("Found contacts:")    
                print(contacts_to_update)
        
            
                index_to_update = int(input("Enter the index of the contact to update: "))
        
                if index_to_update in contacts_to_update.index:
                    print("Updating contact:", df.loc[index_to_update])
                    field_to_update = input(f"Enter the field to update ({', '.join(columns)}): ")
            
                    if field_to_update in columns:
                        new_value = input(f"Enter the new value for {field_to_update}: ")
                        df.at[index_to_update, field_to_update] = new_value
                        df.to_csv(filename, index=False)
                        print("Contact updated successfully.")
                    else:
                        print("Invalid field name.")
                else:
                    print("Invalid index.")
            else:
                print("Contact not found.")
                
        elif user_input == 4:
            name_to_delete = input("Enter the contact's first name to delete: ")
            contacts_to_delete = df[df["first_name"] == name_to_delete]
    
            if not contacts_to_delete.empty:
                print("Found contacts:")
                print(contacts_to_delete)
        
                # Optionally, let the user choose which record(s) to delete
                delete_all = input("Do you want to delete all matching contacts? (Y/N): ").strip().lower()
        
                if delete_all == 'y':
                    df = df[df["first_name"] != name_to_delete]
                    df.to_csv(filename, index=False)
                    print("All contacts with that first name have been deleted.")
                elif delete_all == 'n':
                    index_to_delete = int(input("Enter the index of the contact to delete: "))
            
                    if index_to_delete in contacts_to_delete.index:
                        df.drop(index_to_delete, inplace=True)
                        df.to_csv(filename, index=False)
                        print("Contact deleted successfully.")
                    else:
                        print("Invalid index.")
            else:
                print("Contact not found.")
            


        continue_input = input("Do you want to continue? Y/N").strip().lower()
        if continue_input == "N" or continue_input == "n":
            print("Thanks for your time.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
        
    
    

    

