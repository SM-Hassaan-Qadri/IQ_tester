# import request module
import requests

#import HTML for clean text
import html

clean_text = html.unescape("Kanye West at 2009 VMA&#039;s interrupted which celebrity?")
print(clean_text)

# import random module
import random

# score pannel
score = 100
error = 0

# question counter
i = 0

print("Hello! This game will ask you 5 questions.\nYour score will hint at your IQ \n")

# Loop runs 5 times
while i < 5:
    # API URL
    url = "https://opentdb.com/api.php?amount=1&type=multiple"

    # Fetch question
    response = requests.get(url)
    data = response.json()
    question = data['results'][0]

    # Combine and shuffle options
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)

    print("\nCategory:", question['category'])
    print("\nQuestion:", question['question'])
    for idx, opt in enumerate(options, start=1):
        print(f"{idx}. {opt}")

    # Take user input
    user_input = input("\nEnter option number: ").strip()
    if not user_input.isdigit() or not (1 <= int(user_input) <= len(options)):
        print("Invalid input. Please enter a valid option number.")
        continue  # ask same question again

    chosen = options[int(user_input) - 1]

    # Check answer
    if chosen == question['correct_answer']:
        print("✅ Correct Answer!")
    else:
        print(f" Wrong! Correct answer is: {question['correct_answer']}")
        error += 10

    print(f"Your current score is: {score - error}")
    i += 1  # count this question

# After 5 questions
final_score = score - error

print("\n✅✅✅ Test complete!")
print(f"Your final score is: {final_score}")

# Fun IQ message
if final_score >= 90:
    print("🧠 Your IQ level: Genius! ")
elif final_score >= 70:
    print(" Your IQ level: Smart! ")
elif final_score >= 50:
    print(" Your IQ level: Average. Keep sharpening your mind!")
else:
    print(" Your IQ level: Keep practicing! ")

print("\nThanks for playing!")
