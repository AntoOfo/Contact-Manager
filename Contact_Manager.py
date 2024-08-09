import csv
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
            user_data = {}
            for column in columns:
                value = input(f"Enter {column}: ")
                user_data[column] = value
            writer.writerow(user_data)
            csvfile.flush()  # makes sure data is written immediately
            print("Contact added succesfully")
            
        elif user_input == 2:
            
            print("Here's the existing contacts:")
            with open("contacts.csv", mode="r") as readfile:
                data_reader = csv.DictReader(readfile)
                
                for row in data_reader:
                    print(row)
                    
        elif user_input == 3:
            
            with open("contacts.csv", mode="r") as readfile:
                data_reader = csv.DictReader(readfile)
                contacts = list(data_reader) # turns read to a list
                
            name_to_update = input("Enter the first name of the contact to update: ")
            found = False
            for contact in contacts:
                if contact["first_name"] == name_to_update:
                    print("Found contact:", contact)
                    field_to_update = input(f"Enter the field to update ({', '.join(columns)}): ")
                    if field_to_update in columns:
                        contact[field_to_update] = input(f"Enter the new value for {field_to_update}: ")
                        found = True
                        break
                    else:
                        print("Invalid field name.")
                        
            if found:
                # saves updated contacts back to file
                with open(filename, mode='w') as writefile:
                    writer = csv.DictWriter(writefile, fieldnames=columns)
                    writer.writeheader()
                    writer.writerows(contacts)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")


        continue_input = input("Do you want to continue? Y/N").strip().lower()
        if continue_input == "N" or continue_input == "n":
            print("Thanks for your time.")
            break
        
    
    

    

