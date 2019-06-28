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
Examples are at the bottom of this document

conditions:
	exact="text"
	If the comment is the same as the text
	
	keyword="text"
	If the comment contains the text

actions:
	reply="text"
	Replies with the text
	
	blacklist
	Blacklists the comments author from further replies
	
	blacklistreply="text"
	Replies with the text then blacklists the user from further replies