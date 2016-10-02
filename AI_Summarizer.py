#A Simple script that implements Machine learning algorithms to summarize text

import Algorithmia


input = open('Commas.txt', 'r').read()
client = Algorithmia.client('sim+fiwkxhdy48CoJcu1EonLOI61')
algo = client.algo('nlp/Summarizer/0.1.3')
result = algo.pipe(input) 

print(result.result)   










