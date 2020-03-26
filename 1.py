import re 
address = '123add 333 21'
test1 = re.sub('[\d]+','',address)
test2 = re.sub('[\d]+','',address, 1)
print(test1)
print(test2)

