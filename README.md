# Similar Phrase Generation using glove, NLTK, Spacy Flask

## Architechture

## Flow diagram

Code Description phrase_generation.py : 
	Initially I will load glove model. As Glove model size is more than 150MB it takes little time. Then maim code execution will be started.
	I am passing the user entered phrase to my main function. Cleaning process will be started. Part of cleaning process any punctuation in phrase will be removed and any non-alphabet letter/word will be removed. Once cleaning is code will move forward for generating similar phrases. Phrase will be tokenized into word label.
	
	Next, for each word synonyms and related domain will be collected using Textblob and Spacy Library which will be pass as dictionary format where each words are key and synonyms & domains will be values.
	
	Next, phrases will be created based on generated synonyms & domains. It will use all combination of generated words.
	Next, We need to find out most related phrases out of all Sentences. Where we need find out threshold value of similarity above that threshold values phrases will be consider as most related phrases. I have decided lowest threshold value will be 75 percentage and default threshold value will be 88 percentage.
	
	Next, We will clean generated most related phrase and pass to front-end.
	
Code Description main_app.py : 
	I have used flask library for end point connection and routing html pages.
	
Code Description for Front-end : sample_input.html will receive the phrase and sample_output.html will populate the generated similar phrases.

Future Improvement: I will working on front-end for better visualization. 

Suggestions: I will be glad to hear if any improvement suggestion hop in other-than mentioned one.
