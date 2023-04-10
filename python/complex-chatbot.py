import time
response_tense = "neutral"
def is_in_sentence(words, sentence):
    for word in words:
        if word in sentence:
            return True
    return False

while True:
    message = input("Enter a message: ") # get the message from the user
    if is_in_sentence(["was", "did", "were", "didn't", "weren't", "hadn't"], message): # check if the message is in the sentence
        tense = "past"
    else:
        if is_in_sentence(["is", "are", "we are", "am", "now", "isn't", "right now"], message):
            tense = "present"
        else:
            if is_in_sentence(["will", "will be", "will not", "will not be"], message):
                tense = "future"
            else:     
                if response_tense == "past":
                    if message == "That was hard." or message == "That was very hard." or message == "That was very hard." or message == "That was really hard.." or message == "That was difficult." or message == "That was very difficult." or message == "That was quite difficult." or message == "That was quite hard.":
                        print("Chatbot: Congratulations for completing that task that you claim was difficult.")
                    if message == "That was easy." or message == "That was very easy." or message == "That was really easy." or message == "That was easy-peasy." or message == "That was quite easy." or message == "That was very easy.":
                        print("Chatbot: I cannot understand feelings, or anything. I do not even hear your voice, so I do not and can not understand you, but congratulations on completing the task.")