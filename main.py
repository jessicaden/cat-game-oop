from cat import Cat

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour=input("enter colour of cat:")

mycat= Cat(name,colour)
# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats 4. feed it 5. put it to sleep")

    if option == "1":
        mycat.play()
    elif option=="2":
        mycat.train()
    elif option=="3":
        mycat.stats()
    elif option=="4":
        mycat.feed()
    elif option=="5":
        mycat.sleep()
    else:
        "enter number 1-5"

    if mycat.energy< 5:
        break
    elif mycat.intelligence<5:
        break
    elif mycat.weight<2 or mycat.weight>10:
        break

if mycat.energy<5:
        print("your cat,",mycat.name, "has died due to critical energy levels. Current energy level:",mycat.energy)
elif mycat.intelligence<5:
        print("your cat,",mycat.name, "has died due to severely lacking intelligence. Current intelligence level:",mycat.intelligence)
elif mycat.weight<2:
        print("your cat,",mycat.name, "has died due to malnutrition. Current weight:",mycat.weight)
elif mycat.weight>10:
        print("your cat,",mycat.name, "has died due to being severely overweight. Current weight:",mycat.weight)




