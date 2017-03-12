# PyBot
Create a chatbot in five minutes! No, I'm not even joking.

## PyBot is a chatbot that can be built on to create an AI. PyBot can learn
## from the user.

Creating your own PyBot
=======================

Let's get started by creating a simple PyBot.
All you need is the pyBot.py file and a copy of Python 3.

To create a new bot, you'll want to do the following:

``import pyBot``

``myBot = pyBot.Bot({}, 'botSave.bot') # Creates a bot named myBot.``

``while 1:
	myBot.evaluate(input("Input > ")) # Evaluates the input and decides what to output.``
		
It's as easy as that. You now have your very own chatbot!

PyBot commands
==============

While chatting, you can use some commands to save or load the session, exit, and debug.

/SAVE
-----

Save saves the current session, and stores it in the specified save file.

/LOAD
-----

Load loads a saved session from the specified save file.

/DATA
-----

Data displays the bot's current database, as a Python dictionary. This command is useful for debugging.
