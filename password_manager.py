def view_mode():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:",user, "Password:",password)
def new_mode():
    name = input("Enter Account's name: ")
    password = input("Enter password: ")
    # file = open("passwords.txt","a")
    # file.close()
    #Instead of writing above, we can use the keyword 'with'...'as', which closes the file once the operation is performed on the file
    with open("passwords.txt",'a') as f:
        f.write(name + "|" + password + "\n") # | is the separator
original_m = "I_know"
n = 5
flag = True
while(n and flag):
    master_password = input("Enter your master password: ")

    if master_password == original_m:
        while True:
            mode = input("Select a mode: (New/View/Exit)-> ").lower()

            if mode == "exit":
                flag = False
                break
            if mode == "view":
                view_mode()
            
            elif mode == "new":
                new_mode()
            else:
                print("Invalid mode.\nNo such mode found.")
                continue
    else:
        n -= 1
        print("Sorry, we are unable to authenticate you.\nYou have",n,"attempts left.")