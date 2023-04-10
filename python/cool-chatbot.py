

import spacy
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Load spaCy's English NLP model
nlp = spacy.load('en_core_web_sm')

# Load WordNetLemmatizer from NLTK
lemmatizer = WordNetLemmatizer()

# Define a list of greeting messages
greeting_messages = ["Hi there!", "Hello!", "Greetings!", "Hey!", "Hey, howdy!", "Hey hey HEY!", "Yo, nice to meet you!"]

# Define a list of goodbye messages
goodbye_messages = ["Goodbye!", "See you later!", "Bye!", "Have a nice day!"]

# Define a list of questions and their corresponding answers
qa_pairs = {
    "What is your name?": ["My name is Chatbot!", "I'm Chatbot!", "You can call me Chatbot!"],
    "How are you?": ["I'm doing well, thank you!", "I'm fine, thanks for asking!", "I'm great, how about you?"],
    "What do you like?": ["I like talking to people!", "I like learning new things!", "I like helping people!"]
}

# Define a function to process the user's input
def process_input(input_text):
    # Apply spaCy's NLP model to the input text
    input_doc = nlp(input_text)
    
    # Extract the lemmas of the input text
    input_lemmas = [token.lemma_ for token in input_doc]
    
    return input_lemmas

# Define the main function for the chatbot
def chatbot():
    # Greet the user with a random greeting message
    print(random.choice(greeting_messages))
    
    while True:
        # Get the user's input
        user_input = input("You: ").lower()
        
        # Check if the user wants to exit
        if user_input == 'exit':
            # Say goodbye with a random goodbye message
            print(random.choice(goodbye_messages))
            break
        
        # Process the user's input
        input_lemmas = process_input(user_input)
        
        # Look for a matching question in the QA pairs
        for question, answer_list in qa_pairs.items():
            # Process the question
            question_lemmas = process_input(question.lower())
            
            # Check if the input contains the question
            if set(question_lemmas).issubset(set(input_lemmas)):
                # Respond with a random answer from the answer list
                print(random.choice(answer_list))
                break
        else:
            # If no question matches, respond with a default message
            print("I'm sorry, I didn't understand what you said.")
chatbot()
# Run the chatbot