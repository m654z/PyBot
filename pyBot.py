import random
import pickle

class Bot:
    current = ""
    botText = "BOT> "
    
    def __init__(self, data, saveFile):
        self.data = data
        self.saveFile = saveFile

    def say(self, text, botText):
        print(botText + text)
        self.current = text

    def addResponse(self, userInput, response):
        if userInput in self.data:
            self.data[userInput].append(response)

        else:
            self.data[userInput] = []
            self.data[userInput].append(response)

    def evaluate(self, text):
        if text in self.data:
            self.say(random.choice(self.data[text]), self.botText)

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
            self.say(text, self.botText)
