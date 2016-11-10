#@Author: Christopher Zaremba
#Random period generator; adds a ton of periods to a periodless text 

input = open('Input.txt', 'r').read()


n = 30

for x in range(0, len(input)):
	groups = input.split(' ')
	input = ' '.join(groups[:n]) + ". " + ' '.join(groups[n:])
	n += 25

	
text_file = open("Commas.txt", "w", encoding='Latin-1')
text_file.write("".join(input)) #Final_Text Is Translated Text
text_file.close()
