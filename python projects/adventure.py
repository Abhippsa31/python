name = input("Enter your name:")
print("Welcome", name, "to a magical adventure")
answer = input("You are on a mysterious road. It has to come to an end, and you can go left or right: ")

if answer == "left":
    answer_left = input("You came to a cloudy path, and now you have to cross the invisible path to reach the mysterious box by walking or return back: ")

    if answer_left == "walk":
        print("Walking through the clouds, you found a monster, and you lost!")
    elif answer_left == "back":
        print("You can go back and quit if you are scared.")
    else:
        print("Invalid option")

elif answer == "right":
    print("You came to a forest in search of a mysterious box that may be dangerous because of wild animals. Would you like to walk or go back?: ")
    answer_right = input()

    if answer_right == "walk":
        print("Walking through the forest was a harsh journey, but did you get the box? Yes/No: ")
        answer_get_box = input()

        if answer_get_box == "yes":
            print("Yes, you got it!")
        elif answer_get_box == "no":
            print("You didn't get it.")
        else:
            print("Not a valid response!")

    elif answer_right == "back":
        print("You can walk back and quit.")
    else:
        print("Invalid option")

else:
    print("Invalid option! Eventually, you lost it.")
