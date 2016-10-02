import urllib.request
import re
file = open('C:\\Users\\Christopher\\Desktop\\Hello.txt', 'r')
text = file.read().lower()
file.close()
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
lang = "ar";
print(words[2])

spliter = '%20'



	
link = 'https://www.googleapis.com/language/translate/v2?key=AIzaSyADn9aPVLksL-UA4RZKTvtTytB3aWJov1g&q='
for i in range(len(words)):
	if i == 0:
		link += words[0] 
	else:
		link += spliter + words[i]
link += '&source=en&target=zh-TW'
with urllib.request.urlopen(link) as response:
   html = response.read()
text_file = open("Output.txt", "w", encoding='utf-8')
Final_Text = html.decode('utf-8')
Final_Text = Final_Text.split("translatedText",1)[1] 
Final_Text = Final_Text.split('"',1)[1] 
Final_Text = Final_Text.split('"',1)[1] 
Final_Text = Final_Text.rsplit('"', 1)[0]
text_file.write(Final_Text)

text_file.close()


