#!/usr/bin/env python3

def challenge1():
    print("Challenge 1: Encrypted Military Message")
    print("-------------------------------------------------")
    print("The Military commander sent you a message regarding the upcoming mission.")
    print("However, he encrypted it so the enemy would not be able to find it useful.")
    print("Message: Hi Mhglgw Og Oeib!")
    print("Hint: LEMON\n")
    
    correct_answer = "WE ATTACK AT DAWN!"
    while True:
        answer = input("Enter the decoded message: ").strip().upper()
        if answer == correct_answer:
            print("Challenge 1 captured! Congratulations!\n")
            break
        else:
            print("Incorrect answer. Try again.\n")

def challenge2():
    print("Challenge 2: Morse Code Message")
    print("-------------------------------------------------")
    print("You are receiving a message from the military units on the front lines.")
    print("Decode it so you can act accordingly…")
    print("Message: .-- . / -. . . -.. / .... . .-.. .--. / .- ... / ... --- --- -. / .- ... / .--. --- ... ... .. -... .-.. . -.-.--")
    print("Hint: Decode the Morse Code using standard Morse Code mappings.\n")
    
    correct_answer = "WE NEED HELP AS SOON AS POSSIBLE!"
    while True:
        answer = input("Enter the decoded message: ").strip().upper()
        if answer == correct_answer:
            print("Challenge 2 captured! Congratulations!")
            break
        else:
            print("Incorrect answer. Try again.\n")

def main():
    print("Welcome to the Military Message Challenges!\n")
    challenge1()
    challenge2()
    print("\nAll Messages Decrypted. Well done!")

main()
