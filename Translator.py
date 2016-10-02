#@Author: Christopher Zaremba
#A script that calls the google translate api and translates English to Chinese(Traditional)

import urllib.request
import re
file = open('C:\\Users\\Christopher\\Desktop\\Hello.txt', 'r') #Input Original Text

#Break up inputed txt into individual words
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())

#Declare values
spliter = '%20'
link = 'https://www.googleapis.com/language/translate/v2?key=AIzaSyADn9aPVLksL-UA4RZKTvtTytB3aWJov1g&q='

#Modify link to include the words from input text
for i in range(len(words)):
	if i == 0:
		link += words[0] 
	else:
		link += spliter + words[i]
#Finalize Text
link += '&source=en&target=zh-TW'

#Read Html from link page
with urllib.request.urlopen(link) as response:
   html = response.read()

#Decode Html
text_file = open("Output.txt", "w", encoding='utf-8')
Final_Text = html.decode('utf-8')

#Trim Decoded Html to include only translated text
Final_Text = Final_Text.split("translatedText",1)[1] 
Final_Text = Final_Text.split('"',1)[1] 
Final_Text = Final_Text.split('"',1)[1] 
Final_Text = Final_Text.rsplit('"', 1)[0]

#Output Translated Text
text_file.write(Final_Text) #Final_Text Is Translated Text
text_file.close()


