import random
name=input("type your name here")
print("Hello %s" % name)
answers = ["yes", "NO", "maybe", "dunno"]
while True:
    question=input("type your question")
    print(random.choice(answers))
    if question=="quit":
        break
    
    
    

    

