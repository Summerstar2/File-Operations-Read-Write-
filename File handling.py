def Continue():
    Again=str(input("Would you like to use this program again? (Yes/No) "))
    if Again=="No":
        return False
    return True
print ("This program will let you make a file and then read the contents of the file if any.\nIt can also let you write your own contents into the file.")
while True:
    Use=str(input("Do you want to write into the file or read the contents? (Write/Read) "))
    if Use=="Write":
        with open("Testfile.txt","a") as W:
            Input=str(input("Enter what you want to write in the file - "))
            W.write(Input+"\n")
    if Use=="Read":
        with open("Testfile.txt","r") as R:
            print (R.read())
    if not Continue():
        break