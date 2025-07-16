# 🧠 Python IQ Quiz Game

This is a simple Python quiz game that fetches **random multiple-choice questions** from the **Open Trivia Database (opentdb.com)** API.  
It asks the player **5 questions**, scores their answers, and gives them a **fun IQ message** at the end!

---

## 🚀 How it works

- ✅ Fetches **one random question** at a time using the `requests` module.
- ✅ Cleans up any **HTML symbols** in the question text using `html.unescape`.
- ✅ Shuffles the answer options.
- ✅ Lets the user pick an answer by typing a number.
- ✅ Tracks the score: each wrong answer reduces the score by 10 points.
- ✅ After 5 questions, it shows a **fun IQ level** based on the final score.

---

## 📂 How to run

1️⃣ Make sure you have **Python** installed (3.x).  
2️⃣ Install the required module (only `requests` is needed):

```bash
pip install requests

3️⃣ Save the Python script (for example: iq_quiz.py).
4️⃣ Run the game:

python iq_quiz.py

🧩 Example output

Hello! This game will ask you 5 questions.
Your score will hint at your IQ 

Category: Entertainment: Music

Question: Kanye West at 2009 VMA's interrupted which celebrity?
1. Taylor Swift
2. Beck
3. Beyonce
4. MF DOOM

Enter option number: 1
✅ Correct Answer!
Your current score is: 100

...

✅✅✅ Test complete!
Your final score is: 80
🧠 Your IQ level: Smart!

📚 What you learn

    Using requests to fetch live data from an API.

    Decoding HTML symbols with html.unescape.

    Using random.shuffle to mix up answer options.

    Basic input validation.

    Using loops and conditionals.

    Writing clear, simple Python logic for a real project.

📜 License

This game is for learning and fun — feel free to modify and share!
