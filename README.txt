Instructions:
Every line contains 2 elements:
condition#[#action
The condition and action are split with :::
if for some weird reason you want to type ':::' in either the condition or the action, use '_triple_colons_'
if you want to type "_triple_colons_" in the condition or the action, place '[]' around it (you would get '[_triple_colons_]')
Examples are at the bottom of this document

conditions:
	exact="text"
	If the comment is the same as the text
	
	keyword="text"
	If the comment contains the text

actions:
	blacklist
	Blacklists the comments author from further replies
	
	Reply="text"
	Replies with the text
	
	blacklistreply="text"
	Replies with the text then blacklists the user from further replies