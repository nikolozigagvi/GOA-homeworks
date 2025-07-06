import time
def start():
    print(" the life of Nika")
    time.sleep(1)
    print("you will live Nikas life from age 0 to 12 making choices along the way.")
    time.sleep(1)

def age_4():
    print("age 4 Kindergarten Time")
    time.sleep(1)
    print("youre starting kindergarten. Do you:")
    time.sleep(1)
    print("1. stay close to your teacher and observe.")
    time.sleep(1)
    print("2. run off to play with the other kids.")
    time.sleep(1)
    choice = input("choose 1 or 2: ")
    if choice == "1":
        print("you become the teachers helper and learn a lot early.")
    elif choice == "2":
        print("you make friends fast and love playtime!")
    else:
        print("you stare at the wall.you stupid or what?")

def age_6():
    print("age 6: First hobys")
    time.sleep(1)
    print("you feel curious about trying something new Do you:")
    time.sleep(1)
    print("1. start learning to draw.")
    time.sleep(1)
    print("2. join a soccer team.")
    time.sleep(1)
    choice = input("choose 1 or 2: ")
    if choice == "1":
        print("you begin drawing little houses youre creative!!")
    elif choice == "2":
        print("you become really active and love playing outdoors!!")
    else:
        print("you nap instead.you are now boring ass")

def age_9():
    print("age 9: A Small Challenge")
    time.sleep(1)
    print("you struggle a bit with school How do you handle it?")
    time.sleep(1)
    print("1. ask a teacher for help.")
    time.sleep(1)
    print("2. pretend you're fine and keep trying alone.")
    time.sleep(1)
    choice = input("Cchoose 1 or 2: ")
    if choice == "1":
        print("good move!!! your teacher supports you and things improve to a good way.")
    elif choice == "2":
        print("you get through it, but its a bit harder than it needed to be.")
    else:
        print("you invent a robot to do your homework.bruh you cant do homework but can do this jeez")

def age_12():
    print("age 12: figuiring Out Who You Are")
    time.sleep(1)
    print("you start thinking more about the future. Do you:")
    time.sleep(1)
    print("1. focus on creative things like art or music.")
    time.sleep(1)
    print("2. dive into tech and start coding.")
    time.sleep(1)
    choice = input("Choose 1 or 2: ")
    if choice == "1":
        print("you feel free expressing yourself and people enjoy your creations.")
    elif choice == "2":
        print("you build simple games  and feel excited about the digital world.")
    else:
        print("you decide to become a philosopher.what is wrong with you?")

def ending():
    print("end of chapter one")
    time.sleep(1)
    print("you lived 12 beautiful and questeneble years full of choices.")
    time.sleep(1)
    print("my story is just starting!!!!!")
    time.sleep(1)
    print("thanks for your atantion")

#daxmareba internetis
def main():
    start()
    age_4()
    age_6()
    age_9()
    age_12()
    ending()

if __name__ == "__main__":
    main()
