#Open the text file as read
with open("personal_info.txt", "r") as user_info:

    #Create an input statement asking users for a name they want to look for
    locator= input("Please state the name you're looking for: ")

    #Place the data of the text file as read inside a variable
    data= user_info.read()

    #Split the data into separate lists
    personal_set= data.split(" \n")
#Create a loop for indicating whether the name is in the text file
#Create an if condition for the data to be extracted
