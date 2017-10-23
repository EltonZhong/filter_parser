#utf-8
test_str = 'a+b*c+c+1=1!=true!=qbcc1'
KEY_WORDS= ['+', '-', '*', '/', '(', ')']
OPERATORES = ['=', '!=', '>', '<']
tokens = ['1', '*','(','asd', '+', '2', ')', '+', '1']
def transfer(tokens):
	suffix_tokens = []
	stack = []
	i = 0
	while(i < len(tokens)):
		if(tokens[i] not in KEY_WORDS):
			suffix_tokens.append(tokens[i])
		elif tokens[i] == '(':
			stack.append(tokens[i])
		elif tokens[i] == ')':
			while(stack[len(stack) -1 ] != '('):
				suffix_tokens.append(stack.pop())
			stack.pop()
		else:
			if(len(stack) == 0):
				stack.append(tokens[i])
			else:
				while(len(stack)):
					if(stack[len(stack) - 1: len(stack)][0] in ["+", "-"] and tokens[i] in ["*", "/"]) or stack[len(stack)-1] == '(':
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

	return suffix_tokens

def caculate(suffix_tokens):
	stack = []
	i = 0
	while i<len(suffix_tokens):
		result = None
		if(suffix_tokens[i] not in KEY_WORDS):
			stack.append(suffix_tokens[i])
		else:
			if('*' == suffix_tokens[i]):
				try:
					stack[len(stack)-1] = int(stack[len(stack)-1])
					stack[len(stack)-2] = int(stack[len(stack)-2])
				except Exception, e:
					try:
						stack[len(stack)-2] = int(stack[len(stack)-2])
					except Exception, e:
						pass
			a = stack.pop()
			b = stack.pop()
			eval('stack.append(b{}a)'.format(suffix_tokens[i]))
		i += 1
	print stack



caculate(transfer(tokens))