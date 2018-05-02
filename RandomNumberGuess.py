import random
#libary to genarate random numbers

play_list=["yes!", "yes", "Yes","Ya","Yep","yep","Yup","YAAAAAS","Totally","Totes","Sure","y","Y"]
leave_list=["No","no","nah","nope","totally not","n","N"]
#list for stay or leave answer for varible: playagain
#restart=0
uname=input("please enter your name: ")
#asks for user name
print("Hello", uname , ".This is a Game where you have to corectly guess a number, you are only allowed 3 guesses.")
#prints a greeting

#this looks wrong
#again




def game():
        rannum= random.randint(1,10)
        #generate random number between 1-10
        for i in range(3):
        #loop that run 3 times
            while True:
            #while loop for error checking
                try:
                    answer= int(input("please enter a number between 1-10\n:"))
                    break
                #asks for user input breaks program if a number is entered
                except ValueError:
                    print ("That is not a number, please enter a number")
                    continue
                #if not number will say wrong and than ask for answer varible again.
            if answer == rannum:
                print ("corect")
                break
            elif answer>rannum:
                print ("The number you entred was to high.")
                continue
            else:
                print ("The number you entred was to low.")
                continue
        #Checks if the guess the user gave is corect wrong or a incorect value. Than tells the user so
        print("The number was:",rannum)
       # return

#function

playagain = "Y"
#hard coded to run while loop below every time
while True:
        if playagain in play_list:
    #compare playagain to play_list
            game()
        #runs game function
        else:
            playagain in leave_list
        #compare playagain to leave_list
            print ("Good bye, ", uname ,".")
            quit()
        #quits program if user dosent want to play
            try:
                playagain = input("Play again? (y/n): ")
        #break
