#rock paper sissor game (26/8/2024)
print("WHAT DO YOU CHOOSE?")
print("Type 0 for ROCK, 1 for PAPER,2 for SISSOR ")
inp= int(input())
import random
num= random.randint(1,3)
if(inp == "0"):
    (print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""))
    if(inp==0):

        print("Computer Chose ROCK: Draw")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif num==1:
        print("Computer chose: PAPER")
        print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
        print("You Lose")
    else:
        print("Computer chose : Sissor" )
        print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

        print("YOU WIN")
        #ppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
elif inp == "p":

    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
        if(inp==1):
            print("Computer chose Paper")
            print("""
                 _______
             ---'    ____)____
                         ______)
                     _______)
                     _______)
            ---.__________)
            """)
            print("Draw")
        elif(inp==0):
            print("Coputer chose : ROCK")
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
            print("You WIN")
        else:
            print("Computer chose:Sissor")
                print("""
                        _______
                    ---'   ____)____
                              ______)
                           __________)
                          (____)
                    ---.__(___)
                    """)
            print("YOU LOSE")
else:

    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    if(inp==0):
        print("Computer chose ROCK")
        print("""
                        _______
                    ---'   ____)
                          (_____)
                          (_____)
                          (____)
                    ---.__(___)
                    """)
        print("you lose")
    elif inp ==1:
        print

