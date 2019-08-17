USE THE LATEST RELEASE. NEVER JUST TAKE THE SOURCE CODE FROM THIS PAGE, GO TO THE RELEASES PAGE TO GET IT.
I ALWAYS IMMEDIATELY PUSH TO ORIGIN WHICH MEANS WHATEVER IS HERE CAN BE FULL OF BUGS.

Bots made with this tool:
- u/says_lmao_bot
- u/real_sarcasm_police

This is a tool to allow the easy creation of reddit bots.
There are 3 files you should edit.
	privateinfo.txt			for things like the bot password. username, and id
	config.txt			for the configuration (what subreddit, how far does it go back)
	instructions.txt		for the instructions (what to reply to, and what to reply)

There is a posibility your bot will get rate limited very quickly in the beginning, to avoid this you need to have some karma.
So I suggest making some comments until you have like 50 karma with the bot account, before activating the bot.
You need to open this file every time you want the bot to go active, but that can easily be automated.

privateinfo.txt
It should look like:

	client_id=??
	client_secret=??
	password=??
	user_agent=??
	username=??

pretty self explanatory 

Config:
Go in the "config.txt" file and edit the configs.
There are 3 things you can edit

subreddit=[subreddit]
type=[can be hot or new]
amount=[num]

Instructions:
You can add comments by prefacing them with ##
##This is a comments
Every line contains 2 elements:
condition:::action
The condition and action are split with :::
if you want to type ':::' in either the condition or the action, use '_triple_colons_'
if for some weird reason you want to type "_triple_colons_" in the condition or the action, place '[]' around it (you would get '[_triple_colons_]')
There are some examples in the instructions.txt

conditions:
	exact="text"
	If the comment is the same as the text
	
	keyword="text"
	text is a regex. Tries to find the regex in the test

actions:
	reply="text"
	Replies with the text
	
	blacklist
	Blacklists the comments author from further replies
	
	blacklistreply="text"
	Replies with the text then blacklists the user from further replies