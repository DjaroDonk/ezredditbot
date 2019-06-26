Instructions:
Every line contains 2 elements:
condition#[#action
The condition and action are split with #[#
You can use multiple conditions or actions, split with -[-
Inside of conditions and actions you can sometimes enter multiple arguments. 
In this case the arguments are split with :[:
If an argument is optional the documentation will show it as ?(argument=default_answer)
The ? and the () should not be entered in the instructions.txt'
True and False should start with a capital letter
Examples are at the bottom of this document

Conditions:
	exact=text:[:?(case_sensitive=True)
		Is true if the comment is the same as the text
	keyword=text:[:?(case_sensitive=True)
		Is true if the comment contains the keyword
	regex=text
		Is true if the comment contains the regex
	author=name
		Is true if the author of the comment has this name
	not_author=name
		Is true if the author of the comment does not have this name

Actions:
	reply:[:the_text
		replies with text to the comment. the_text can consist of multiple fields, split with :[:
		Text arguments:
			"some_string"          :  adds the text to the reply
			author		       :  adds the comment's author to the reply     
	blacklist
		blacklists the author of the comment






Examples:

If the keyword "walter" is found, reply with "I like fire trucks and moster trucks":
keyword=walter#[#reply:[:"I like fire trucks and moster trucks"

If the comment is "I like trains", reply with "I like trains too":
exact=I like trains#[#reply:[:"I like trains too"

If the comment is "blacklist", blacklist the user:
exact=blacklist#[#blacklist

If the comment is "blacklist", blacklist the user and reply with "you are now blacklisted"
exact=blacklist#[#blacklist-[-reply:[:"you are now blacklisted"

If the keyword "apple" or "peach" is found, 
reply with "banana":
keyword=apple:[:case_sensitive=False-[-keyword=peach:[:case_sensitive=False#[#reply:[:"banana"

If the comment is "hello" or "hi",
 reply with "Hello [comment author], how are you":
exact=hello:[:case_sensitive=False-[-exact=hi:[:case_sensitive=False#[#reply:[:"Hello ":[:author:[:", how are you"