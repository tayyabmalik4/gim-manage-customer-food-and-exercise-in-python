import datetime
def getdate():
    return datetime.datetime.now()

print("Welcome to my health jim")
choose = int(input("1 for write and 2 for read: "))
# if choose==1:
    # choose11=int(input("Enter 1 for food and 2 for exercise"))
    # reading(choose11)
# else:
    # choose11=int(input("Enter 1 for food and 2 for exercise"))
    # writing(choose11)

if choose==1:
    def writing(w):
        if w==1:
            print("Welcome to diet plane")
            c = int(input("Enter 1 for Tayyab 2 for junaid and 3 for zahid: "))
            
            if c==1:
                value = input("Please enter the food: ")
                f1= open("tayyab-food.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            elif c==2:
                value = input("Please enter the food: ")
                f1=open("junaid-food.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            elif c==3:
                value = input("Please enter the food: ")
                f1 = open("zahid-food.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            print("Thanks to add the food")
        
        elif w==2:
            print("Welcome to excercise plane")
            c = int(input("Enter 1 for Tayyab 2 for junaid and 3 for zahid: "))
            if c==1:
                value = input("Please enter the excercise plane: ")
                f1= open("tayyab-exe.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            elif c==2:
                value = input("Please enter the excercise plane: ")
                f1=open("junaid-exe.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            elif c==3:
                value = input("Please enter the excercise plane: ")
                f1 = open("zahid-exe.txt","a")
                f1.write(str([str(getdate())])+":"+value+"\n")
                f1.close()
            print("Thanks to add the exercise")
        print("if you run again then press 1 and for exit press any key")
        key = input()
        if key==1:
            writing(w)
        else:
            print("thanks for adding the values")
    w=int(input("Enter 1 for food and 2 for exercise"))
    writing(w)
else:
    def reading(re):
        if re==1:
            print("Welcome   to food reading")
            c=int(input("Enter 1 for Tayyab and 2 for Junaid and 3 for zahid"))
            if c==1:
                f1=open("tayyab-food.txt")
                content=f1.read()
                print(content)
                f1.close()
            elif c==2:
                f1=open("junaid-food.txt")
                content=f1.read()
                print(content)
                f1.close()
            elif c==3:
                f1=open("zahid-food.txt")
                content=f1.read()
                print(content)
                f1.close()
        elif re==2:
            print("Welcome to excercise reading")
            c=int(input("Enter 1 for Tayyab and 2 for Junaid and 3 for zahid"))
            if c==1:
                f1=open("tayyab-exe.txt")
                content=f1.read()
                print(content)
                f1.close()
            elif c==2:
                f1=open("junaid-exe.txt")
                content=f1.read()
                print(content)
                f1.close()
            elif c==3:
                f1=open("zahid-exe.txt")
                content=f1.read()
                print(content)
                f1.close()
        print("if you run again then press 1 and for exit press any key")
        key=input()
        if key==1:
            reading()
        else:
            print("Thanks for using this app")
    re=int(input("Enter 1 for food and 2 for exercise"))
    reading(re)            

