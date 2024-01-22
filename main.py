# Python quiz game



questions = ("How planet in your solar system?:",
             "Highest score in odi cricket by a player?:",
             "India current prime minister is?:",
             "How many elements are in the periodic table?:",
             "Percentage of water present in earth?:",)

options = (("A.8","B.9","C.7","D.13"),
           ("A.265","B.264","C.200","D.300"),
           ("A.Yogi Aditynath","B.Narendra Modi","C.Virat","D.Rohit"),
           ("A.116","B.117","C.118","D.119"),
           ("A.72","B.45","C.18","D.71"))

answers =("A","B","B","C","D")
guesses = []
score = 0
question_num =0

for question in questions:
    print("______________________")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}")
    question_num += 1

print("___________________________")
print("        RESULTS            ")
print("___________________________")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")

score = (score / len(questions) * 100)
print(f"Your score is : {score}%")


