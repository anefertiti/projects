begin= (input("Welcome to the interview simulator! Remember that your actions will have consequences. Type your name to start."))
print ("Ring! Ring! Ring! Your alarm wakes you up but you realize it’s been beeping for 20 minutes! What do you do?")
sleep_a= print("A: 30 more minutes :(")
sleep_b= print("B: Up and at 'em!")
sleep_1= "A"
sleep_2= "B"
alarm= input("Choice: ")
if (sleep_1==alarm): print ("Enjoy your rest sleepyhead!")
else: print("You use those 30 minutes to brush your teeth and take a quick shower.")

print ("You have a very important interview with a large tech company today. You’ve got to wear something to impress them. Go in your closet and pick out your favorite outfit!")
out_a= print("A: A suit")
out_b= print("B: Jeans and t-shirt")
out_c= print("C: A tracksuit")
out_1= "A"
out_2= "B"
out_3= "C"
outfit= input("Choice: ")
if (outfit==out_1):print ("I’m loving your style!")
else: print("You did remember this is a job interview… right?")

test= int(input("On the way to the interview, your Uber driver asks you to guess what number, 1-10, is in his head. You find no harm in it and answer. "))
if test >8 and test <10: 
    print("Too high. You've arrived at the location anyways.")
if test <8:
    print("Too low. You've arrived at the location anyways.")
elif test==8: 
    print("Right on the nose! He gives you a $5 bill as you exit")
else: 
    print("Wow that wasn't even in the ballpark. You've arrived at the location anyways")

print("You arrive to the interview on time and meet your employer. They give you a warm welcome")
print("Interviewer: Good afternoon, "+ begin)
input("You: ")
if(sleep_1==alarm): print("You realize you didn't have time to brush your teeth before you left! You hope the interviewer didn't notice...")
print("The interview is going well until they ask you: Why should we hire you? How do you answer?")
hire_a= print("A: Explain that you're a good person and you deserve the job")
hire_b= print("B: You blanked!!!")
hire_c= print("C: Detail your skills and how you represent the values of the company")
hire_1= "A"
hire_2= "B"
hire_3= "C"
hire= input("Choice: ")
if(hire==hire_1): print("Alright...")
if(hire==hire_2): print("That's okay. Dust yourself off.")
if(hire==hire_3): print("The interviewer smiled!")

if test==8:
    print("You finish the interview and buy yourself an icecream with the $5 your Uber driver gave you")
else:
    print("You finish the interview and go home.")

print("2 days later, you check your email and find a response from the company! Let's see what it says")
if (sleep_2==alarm) and (outfit==out_1) and (hire==hire_3): 
    print ("Congratulations! You got the job!")
else: print ("Sorry, you weren't the right fit for our company.")
