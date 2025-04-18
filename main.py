from pet import Pet, create_pet

def main():
    my_pet = create_pet()
    
    while True:
        print("\nACTIONS:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Train")
        print("5. Check Status")
        print("6. Show Tricks")
        print("7. Quit")
        
        choice = input("Choose action (1-7): ")
        
        if choice == "1":
            print(my_pet.eat())
        elif choice == "2":
            print(my_pet.play())
        elif choice == "3":
            print(my_pet.sleep())
        elif choice == "4":
            trick = input("Enter trick to teach: ")
            print(my_pet.train(trick))
        elif choice == "5":
            print(my_pet.get_status())
        elif choice == "6":
            print(my_pet.show_tricks())
        elif choice == "7":
            print(f"Goodbye! {my_pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()