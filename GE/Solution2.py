import string

#i. Rule for consonant
def caesarCipherEncryptor(_string):
	key = 3
	alphabet_dic_indexing_key = dict(zip(string.ascii_lowercase, range(1,27)))
	alphabet_dic_indexing_key.update(dict(zip(string.ascii_uppercase, range(1,27))))
	alphabet_dic_indexing_number = dict( zip(range(1,27),string.ascii_lowercase))
	alphabet_dic_indexing_number.update(dict( zip(range(1,27),string.ascii_uppercase)))
	cipher_text = ''
	for s  in _string.replace('\n','').replace('\r',''):
		if s != ' ':
			_index = (alphabet_dic_indexing_key[s] + key) % 26
			if _index == 0:
				_index = 26
			cipher_text = cipher_text + alphabet_dic_indexing_number[_index]
		else:
			cipher_text = cipher_text + ' '
	return cipher_text

with open(r'SolutionTestCase.txt') as fp:
	line = fp.readline()
	while line:
		print(caesarCipherEncryptor(line))
		line = fp.readline()