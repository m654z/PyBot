import random
import pickle

class Bot:
    def __init__(self, current, data, saveFile):
        self.current = current
        self.data = data
        self.saveFile = saveFile

    def say(self, text):
        print("BOT> " + text)
        self.current = text

    def addResponse(self, userInput, response):
        if userInput in self.data:
            self.data[userInput].append(response)

        else:
            self.data[userInput] = []
            self.data[userInput].append(response)

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
