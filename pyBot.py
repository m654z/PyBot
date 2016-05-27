import random
import pickle

class Bot:
    current = ""
    botText = "BOT> "
    
    def __init__(self, data, saveFile):
        self.data = data
        self.saveFile = saveFile

    def say(self, text):
        print(self.botText + text)
        self.current = text

    def addResponse(self, userInput, response):
        if userInput in self.data:
            self.data[userInput].extend(response)

        else:
            self.data[userInput] = []
            self.data[userInput].extend(response)


    def evaluate(self, text):
        if text in self.data:
            self.say(random.choice(self.data[text]))

        elif text == "/SAVE":
            f = open(self.saveFile, 'wb')
            pickle.dump(self.data, f)
            f.close()

        elif text == "/LOAD":
            f = open(self.saveFile, 'rb')
            self.data = pickle.load(f)
            f.close()

        elif text == "/DATA":
            print(self.data)

        else:
            if not self.current in self.data:
                self.data[self.current] = []

            self.data[self.current].append(text)
            self.say(text)

class Utility:
    def stripSpecial(self, string):
        return string.decode("unicode_escape").encode("ascii", "ignore")

    def stripWhitespace(self, string):
        return "".join(string.split())

class Variables:
    things = ["TV", "computers", "music", "books", "sports"]
    greetings = ["Hello!", "Hi!", "Hey!"]
    farewells = ["Goodbye!", "Bye!", "See you later!"]
    jokes = ["Can a kangaroo jump higher than a house? Of course, a house doesn't jump at all.",
         "Why did the dinosaur cross the road? Because the chicken hasn't evolved yet.",
         "I heard Apple is designing a new automatic car. But they're having trouble installing windows."
    ]
