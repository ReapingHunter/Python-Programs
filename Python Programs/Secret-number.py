secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

userNum = int(input())
while(userNum != secret_number):
    print("Ha ha! You're stuck in my loop!")
    userNum = int(input())

print(secret_number)
print("Well done, muggle! You are free now.")