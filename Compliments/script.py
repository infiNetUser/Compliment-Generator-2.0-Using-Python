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

print("Welcome to the Compliment Machine 2.0!")
start_machine = input("Type Q and then press Enter to start the machine! ")
if start_machine == "Q":
    for i in range(4):
        print(generate_compliment())
else:
    print("Error: Missing input!")
