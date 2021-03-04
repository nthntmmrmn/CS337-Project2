from parse_recipe import get_recipe


if __name__ == "__main__":
    print("CS337 Project 2\n")
    
    
    while True:
        
        url = input("Enter a url of a recipe: ")
        #need to check validity
        print("Here is your recipe:\n")
        print(get_recipe(url))
        print("-------\n")
        print("Transform your recipe:\n")
        print("Press 1 to transform your recipe to vegetarian.\n")
        print("Press 2 to transform your recipe to a healthy one.\n")
        print("Press 3 to transform your recipe to a ____ cuisine.\n")
        print("Press 4 to transform your recipe to a gluten-free option.\n")
        print("Press 5 to exit.\n")
        choice = input("Your option: ")
        if (choice == "5"):
            break
        elif (choice == "1"):
            print("Transforming to vegetarian.")
        elif (choice == "2"):
            print("Transforming to a healhty recipe.")
        elif (choice == "3"):
            print("Transforming to ____ cuisine.")
        elif (choice == "4"):
            print("Transforming to gluten-free.")
        #need to check validity
        
        
    
        
    
    
