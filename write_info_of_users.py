#Open the text file as write
with open("personal_info.txt", "a") as user_info: #It should be justified as append to add more data
    while True: #Place a loop
        # Create five input statements (e.g. Fullname, Age, Address, Birthday, and Hobby)
        full_name= input("Please enter your fullname: ")
        while True: #Place another loop for the try and except condition to avoid errors
            try:
                age= int(input("Please enter your age: "))
                break
            except:
                print("Wrong format, please try again")

        birthday = input("Please enter your birthday in complete detail (month, day, and year): ")
        address= input("Please state your address: ")
        hobbies= input("Please enter any hobby that you like (If theres none, please state None): ")

        #Append all the data to the text file
        user_info.write(f"Fullname: {full_name}\nAge: {age}\nAddress: {address}\nBirthday: {birthday}\nCurrent Hobbies: {hobbies}\n")
        user_info.write(" \n")
        
#Place another input statement asking users whether they want to enter more data or not
#Create an if condition for the reentry input
#End all task if the user enters no