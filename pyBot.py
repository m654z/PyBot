import pickle
import random

class Bot:
    def __init__(self, lastOutput, database, saveFile):
        self.lastOutput = lastOutput
        self.database = database
        self.saveFile = saveFile

    def save(self):
        f = open(self.saveFile, 'wb')
        pickle.dump(self.database, f)
        f.close()

    def load(self):
        f = open(self.saveFile, 'wb')
        self.database = pickle.load(f)
        f.close()

    def say(self, text):
        print("BOT> " + text)
        self.current = text

    def evaluate(self, text):
        if text in self.database:
            self.say(random.choice(self.database[text]))

        if text == "/QUIT":
            print("If you quit, you will lose your current database! Are you sure?")
            userInput = input("y/n> ")
            if userInput.lower().startswith("n"):
                exit
            else:
                bot.say("...")

        if text == "/SAVE":
            self.save()
            self.say("...")

        if text == "/LOAD":
            self.load()
            self.say("Hi!")

        if text == "/DATA":
            print(self.database)
            self.say("...")
