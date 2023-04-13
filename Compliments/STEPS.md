Want to learn more about this Python Program, here are the steps of developing your own and how the whole Python thing works. 

**STEPS:**

Step 1:

Create a folder, and call it Compliments. Then add a file, name it whatever but if you want, name it script.py. The .py extension is a __module__ in Python.

You might want to install an IDE, or Intergrated Development Enviroment. Install **Visual Studio Code**. Then import your folder with your file in there. 

Step 2:

To check if you have Python installed in your operating system we must go to our terminal and type in this command. `python3 --version` or `python --version`
If not, you might have to install it but I will put the link next to this sentence: https://www.python.org/downloads/

Download the latest version of Python and follow the installation process once downloaded.

Step 3: 

Okay, now lets become more technical here. Open up Visual Studio code with your folder and file ready. Open your script.py file or whatever you named it and start typing this:

`import random

def generate_compliment():

  complist = [
  
  ]
`

So this code makes a list called complist. It store data like integers, and string and much more. Also there is a function which the function store the list. 


Step 4:

So here is the finished function:

import random

`
import random

def generate_compliment():
    complist = [
        "You have a beautiful smile.",
        "You're a great listener.",
        "You have a kind heart.",
        "You're intelligent and insightful.",
        "You have a wonderful sense of humor.",
        "You're an amazing friend.",
        "You're talented and creative.",
        "You have a contagious energy that uplifts others.",
        "You have a great work ethic.",
        "You're always willing to lend a helping hand.",
        "You're a great problem-solver.",
        "You're a fantastic communicator.",
        "You have a great eye for detail.",
        "You have a strong sense of empathy.",
        "You're a natural leader.",
        "You're thoughtful and considerate.",
        "You're incredibly organized and efficient.",
        "You're always willing to learn and grow.",
        "You have a unique perspective that adds value.",
        "You're a ray of sunshine on a cloudy day."
    ]

    return complist[random.randint(0,19)]
`

So the `return complist[random.randint(0,19)]` makes the list choose a random number integer from 0 to 19. Why 19 say, because in a list, we call this indexes and when the first index in a list, it's index 0, while its the 1st. I listed 20 of these compliments, but the indexs make it 19. 

Step 5:

Here comes our functionality:

`
print("Welcome to the Compliment Machine 2.0!")
start_machine = input("Type Q and then press Enter to start the machine! ")
`

So in this line of code, we have a print statement, it prints what this program is called and greets you. 
And in the next line, it creates a variable where it stores an input where the user can type the answer, so inside the input function, it says to us that we have to type Q uppercase and then press Enter to execute the command. 

To keep in mind whenever you are make the input function, inside at the end of the text you'd want to press space so that when the user types something, the cursor doesn't stay next to each other.

Step 6:

`
if start_machine == "Q":
    for i in range(4):
        print(generate_compliment())
else:
    print("Error: Missing input or Not Uppercase!")
`

So what this does is it has an if statement where when the user types in "Q" specifically uppercase, it checks and then executes the code using the for statement, in a range of 4, this makes 4 compliments. 

It then prints the list, remember it is also randomized. 

If the user hasn't typed in Q it prints Missing Input saying that you haven't type anything or You have't uppercased it and stops. 


Have fun! I hope you enjoyed. Do this in the Terminal!
