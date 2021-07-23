import colorama
import sys
from colorama import Fore, Back
colorama.init()
print("Enter Y if you can differentiate the text colours or N if you cannot or have trouble in doing so")
print(Fore.RED + "This text is red in colour")
print(Fore.GREEN + "This text is green in colour")
print(Fore.WHITE)
x=input("Y/N ")
if x.lower()=="y":
    pass
elif x.lower()=="n":
    print(Fore.RED + Back.GREEN +"This text is red in colour on green background")
    print(Fore.WHITE + Back.RESET)
    x=input("Can you make out the text? Y/N ")
    if x.lower()=="y":
        print("You have Red-Green colourblindness, it should not hamper daily activities, you don't need to take any actions")
        quit()
    if x.lower()=="n":
        print("You are unable to distinguish Red and Green. Red and green are not as important colours and so daily activities should not be hampered but if you feel abnormal you can take lenses")
        quit()
print(Fore.BLUE + "This text is blue in colour")
print(Fore.GREEN + "This text is green in colour")
print(Fore.WHITE + "Enter H if it is hard to differentiate")
x=input("Y/N/H ")
if x.lower()=="y":
    print("You have no colourblindness")
    quit()
elif x.lower()=="h":
    print(Fore.YELLOW + "This text is yellow in colour")
    print(Fore.RED + "This text is red in colour")
    print(Fore.WHITE)
    x=input("Y/N ")
    if x.lower()=="y":
        print("You have Blue-Green colourblindness, it could cause hindrance in everyday activities and if you observe so get contact lenses")
        quit()
    elif x.lower()=="n":
        print("You have tritanomaly a rare condition which can hamper your daily activities adn contact lenses are recommended")
        quit()
elif x.lower=="n":
    print(Fore.Purple + "This text is purple in colour")
    print(Fore.RED + "This text is red in colour")
    print(Fore.WHITE)
    x=input("Y/N ")
    if x.lower()=="y":
        print(Fore.YELLOW + "This text is yellow in colour")
        print(Fore.PINK + "This text is pink in colour")
        print(Fore.WHITE)
        x=input("Y/N ")
        if x.lower()=="y":
            print("You have trouble differentiating between blue and green, contact lenses are recommended if you feel troubled in daily life")
            quit()
        elif x.lower()=="n":
            print("You are Blue-Green as well as Yellow-Pink colourblind, contact lenses are recommended")
            quit()
    elif x.lower()=="n":
        print(Fore.YELLOW + "This text is yellow in colour")
        print(Fore.PINK + "This text is pink in colour")
        print(Fore.WHITE)
        x=input("Y/N ")
        if x.lower()=="y":
            print("You are Blue-Green as well as Purple-Red colourblind, daily activities could be hampered and lenses can be used if need arises otherwise action is not required")
            quit()
        elif x.lower()=="n":
            print("You have Tritanopia, daily activities will be hampered and you should seriously consider getting lenses")
        
    
            
            