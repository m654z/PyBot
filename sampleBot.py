import pyBot

chatBot = pyBot.Bot({}, 'botSave.bot')      # Creates a new bot and specifies
                                            # the database ({}), and the save
                                            # file (botSave.bot)

# Let's add some data to the database!
chatBot.addResponse("Hello", ["Hi there!"])   # If the user inputs "Hello", the
                                            # bot will output "Hi there!".
                                            
chatBot.addResponse("How are you?", ["I'm fine.", "Alright."])
chatBot.addResponse("What is your name?", ["My name is Chatter!"])
chatBot.addResponse("Goodbye!", ["Goodbye, user!"])

chatBot.botText = "BOT> "   # botText is added to the beginning of all of
                            # bot's outputs.

while 1:      
    chatBot.evaluate(input("YOU> ")) # Gets input and makes the bot evaluate it.
