"""
Script that creates an ASCII-art magic 8-Ball
"""
# import nessicary module
from random import choice

# Clear the screen
print("\033c")
# Initalize all of the possible answers
ANSWERS = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]
# Get the ASCII-art form ball.txt
HANDLE = open("ball.txt", "r")
BALL = HANDLE.read()
HANDLE.close()


def main():
    """
    main process
    """
    # Ask user for question
    input("Enter a Yes or No question:  ")
    # initalize varible
    words = []
    # choose a random answer
    answer = choice(ANSWERS)
    # make that answer into a list by splitting the string by spaces
    answer = answer.split()
    # Blue square in 8-ball is 5 rows tall, iterate over each one
    for i in range(0, 5):
        try:
            # Add the current word to the list, colored and padded with $s for later formatting
            words.append("\033[48;2;0;0;150m" + str(answer[i].ljust(11, "$")))
        # Unless there are no more entries in the answer list, in wich case add a 'blank' string
        except IndexError:
            words.append("\033[48;2;0;0;150m$$$$$$$$$$$")

    def fstr(template, **kwargs):
        """
        Definition for using an f-string format for a varible, taken from
        https://stackoverflow.com/questions/54351740/how-can-i-use-f-string-with-a-variable-not-with-a-string-literal
        """
        return eval(f"f'{template}'", kwargs)

    # Use the f-string definition to format the 8-Ball ASCII-art
    ball = fstr(BALL, words=words)

    def str_to_matrix(string):
        """
        Definition that takes a string and turns it into a matrix
        """
        inner_list = []
        final_list = []
        for char in string:
            inner_list.append(char)
            if char == "\n":
                final_list.append(inner_list)
                inner_list = []
        return final_list

    # Apply the definition to the fromatted string
    # (Def keeps formatting)
    ball = str_to_matrix(ball)
    # Clear the screen again
    print("\033c")
    # Print the magic 8-ball, fully formatted
    for row in ball:
        for char in row:
            if char == "@":
                print("\033[48;2;0;0;0m \033[m", end="")
            elif char == " ":
                print("\033[48;2;0;0;75m" + str(char) + "\033[m", end="")
            elif char == "/":
                print("\033[48;2;0;100;0m \033[m", end="")
            elif char == "$":
                print("\033[48;2;0;0;150m \033[m", end="")
            else:
                print(char, end="")


if __name__ == "__main__":
    # Game loop
    while True:
        # main process
        main()
        # Ask if user wants to ask the 8-Ball again
        if input("Ask again?   ").lower() == "n":
            # if not, break the loop
            break
