#Open the text file as write
with open("personal_info.txt", "a") as user_info: #It should be justified as append to add more data
    personalized_information= {}
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

        personalized_information= {
            full_name:{
                "age": str(age),
                "birthday": birthday,
                "address": address,
                "hobbies": hobbies
            }
        }

        #Create a new variable for storing all the info
        for person, info in personalized_information.items():
            user= person
            user_age= (info["age"])
            user_birthdate= info["birthday"]
            user_address= info["address"]
            user_hobbies= info["hobbies"]

            #Append the data in the text file
            user_info.write(f'Fullname: {user}\n'
                            f'Age: {user_age}\n'
                            f'Birthday: {user_birthdate}\n'
                            f'Address: {user_address}\n'
                            f'Hobbies: {user_hobbies}\n')

            user_info.write(" \n")
        
        #Place another input statement asking users whether they want to enter more data or not
        reentry= input("Would you like to store another set of data (y or n)? ")

        #Create an if condition for the reentry input
        while reentry != "y" and reentry != "n":
            print("Wrong format, please try again")
            reentry = input("Would you like to store another set of data (y or n)? ")

        if reentry == "y":
            print ("Please input a new set of data")
            personalized_information.clear()
        else: #End all task if the user enters no
            break