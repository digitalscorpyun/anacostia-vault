import random
import datetime
import os

# Define the chunks as a dictionary
book_chunks = {
    "Grandfather's Memory": {
        "quote": "Having no name to call on was having no past; having no past pointed to the fissure between the past and the present.",
        "question": "What does the narrator say about the impact of having no ancestral name?"
    },
    "Guayguayare Sea": {
        "quote": "The sea sounded like a thousand secrets, all whispered at the same time.",
        "question": "How does the narrator describe the sound of the sea in Guayguayare?"
    },
    "Maps and Door": {
        "quote": "The Door of No Return is of course no place at all but a metaphor for place.",
        "question": "How does the narrator define the Door of No Return in the Maps section?"
    },
    "Forgetting and Door": {
        "quote": "The door signifies the historical moment which colours all moments in the Diaspora.",
        "question": "What does the Door of No Return signify for the Diaspora?"
    },
    "Caribana and Black Body": {
        "quote": "The Black body is a domesticated space as much as it is a wild space.",
        "question": "How does the narrator describe the Black body in the Diaspora?"
    }
}

# Set up logging
log_dir = r"C:\Users\digitalscorpyun\Anacostia\logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "memorize_book_log.txt")

def log_response(question, user_answer, correct_answer):
    with open(log_file, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - Question: {question}\n")
        f.write(f"User Answer: {user_answer}\n")
        f.write(f"Correct Answer: {correct_answer}\n\n")

# Quiz function
def run_quiz():
    print("Welcome to the Memorization Quiz for 'A Circumstantial Account of a State of Things'!")
    score = 0
    total = len(book_chunks)
    
    # Shuffle the questions
    chunk_keys = list(book_chunks.keys())
    random.shuffle(chunk_keys)
    
    for chunk in chunk_keys:
        data = book_chunks[chunk]
        print(f"\nQuestion: {data['question']}")
        user_answer = input("Your answer: ").strip()
        
        correct_answer = data['quote']
        log_response(data['question'], user_answer, correct_answer)
        
        if user_answer.lower() in correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    
    print(f"\nQuiz complete! Your score: {score}/{total}")
    with open(log_file, "a") as f:
        f.write(f"Quiz Score: {score}/{total}\n{'-'*50}\n")

if __name__ == "__main__":
    run_quiz()