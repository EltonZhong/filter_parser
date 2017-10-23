#utf-8
test_str = 'a+b*c+c+1=1!=true!=qbcc1'
KEY_WORDS= ['+', '-', '*', '/']
OPERATORES = ['=', '!=', '>', '<']
tokens = ['1', '*','asd', '+', '2']
def transfer(tokens):
	suffix_tokens = []
	stack = []
	i = 0
	while(i < len(tokens)):
		if(tokens[i] not in KEY_WORDS):
			suffix_tokens.append(tokens[i])
		else:
			if(len(stack) == 0):
				stack.append(tokens[i])
			else:
				while(len(stack)):
					if(stack[len(stack) - 1: len(stack)][0] in ["+", "-"] and tokens[i] in ["*", "/"]):
						stack.append(tokens[i])
						break
					else:
						suffix_tokens.append(stack.pop())
						if(len(stack) == 0):
							stack.append(tokens[i])
							break
		i += 1
	while(len(stack)):
		suffix_tokens.append((stack.pop()))

	print suffix_tokens


transfer(tokens)