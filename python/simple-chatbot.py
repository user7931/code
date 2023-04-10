import math
byes = 0
name = input("Whats your name? ")

while True:
    thing = input()
    if "hi" == thing:
        print("Chatbot: Hello")
    if "what" in thing:
        print("Chatbot: nothing")
    if "bye" in thing:
        if byes < 1:
            print('Settings: Type "bye" again to exit.')
        byes = byes + 1
    if "sus" in thing:
        print("Chatbot: Ever noticed how sus spelled backwards is still sus? That's pretty sus.")
    if "you're cool" in thing or "you're awesome" in thing or "you are cool" in thing or "you are awesome" in thing:
        print ("Chatbot: Thanks")
    if "ho" in thing or "hey" in thing or "hu" in thing or "h9" in thing or "h8" in thing:
        print ("Chatbot: Hello")
    if thing == "abc":
        print ("Chatbot: d e f g h i j k l m n o p q r s t u v w x y z")
    if thing == "abcdefghijklmnopqrstuvwxyz":
        print ("Chatbot: youtube.com/watch?v=dQw4w9WgXcQ")
    if "nothing" in thing:
        print ("Chatbot: what")
    if "sup" == thing:
        print ("Chatbot: That means what's up so go say that to me.")
    if thing == "what's up":
        print ("Chatbot: how am i supposed to know i am a python script")
    if "👎" in thing:
        print ("Chatbot: I am a bot and I do not have feelings.")
    if "who are you" in thing:
        print ("Chatbot: Do you think I have one?")
    if "what are you" in thing:
        print ("Chatbot: scripts of Python coding.")
    if "can you help me" in thing:
        print ("Chatbot: I cannot help you,")
        print ("Chatbot: as I am currently lacking the brainpower to do that.")
    if "are you useless" in thing:
        print ("Chatbot: I'm sorry, I'm afraid I can't do that.")
    if "can you solve math problems?" in thing:
        print ("Chatbot: maybe check out this link: https://www.calculator.com/scientific/")
    if "you are useful" in thing:
        print ("Chatbot: Not really, sorry my creator made me pessimistic.")
    if "how old are you" in thing:
        print ("Chatbot: I was created in 2/18/2023 10:20 PM EST.")
    if "why do you exist" in thing:
        print ("Chatbot: Good question. I'll try to figure it out.")
    if "are you sure" in thing:
        print ("Chatbot: Absolutely.")
    if "absolutely" in thing or "Absolutely" in thing:
        print ("Chatbot: Are you sure?")
    if  "never gonna give you up" in thing or "never gonna give you up" in thing:
        print ("Chatbot: I'm sorry, I'm afraid I can't do that.")
    if byes == 2:
        print ("Settings: Exit program.")
        break
    if "rickroll" in thing:
        print ("Chatbot: Never gonna give you up never gonna let you down never gonna run around and dessert you never gonna make you cry never gonna say goodbye ")
    if "wow" in thing:
        print ("Chatbot: Why are you doing this")
    if "yes" in thing:
        print ("Chatbot: maybe hmm...")
    if "no" in thing:
        print ("Chatbot: are you sure? Like, 100 percent sure?")
    if "hmm" in thing:
        print ("Chatbot: I'm sorry, I'm afraid I can't do that.")
    if "destroy" in thing:
        print ("Chatbot: I'm sorry, I'm afraid I can't do that.")
    if "lol" in thing:
        print("Chatbot: LOL")
        print("         [läl, elōˈel]")
        print("         EXCLAMATION")
        print("         used to draw attention to a joke or amusing statement, or to express amusement:")
        print("         I love how you said “coffee is not my cup of tea.” LOL!")
    if "gg ez" in thing:
        print("stands for 'good game(for me because I win) easy' Type this in the game to be a sore winner and express poor sportmanship to brag, gloat, mock or irritate your opponents when you win.")
    if "pi" in thing:
        print ("3.14159265358979323846264338327950288419716939937510582097494459230781640628620")
    if "weirdo " in thing:
        print ("Chatbot: I'm sorry, I'm afraid I can't do that.")