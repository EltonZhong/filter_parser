print 'hello parser'

test_str = 'a+b*c+c+1=1!=true!=qbcc1'

KEY_WORDS= ['+', '-', 'x', '/']
OPERATORES = ['=', '!=', '>', '<']
class Tokenizer:
	def __init__(self, _str):
		self.str = _str.strip()
		self.tokens = []
		self.index = 0
	def check_str_is_operator(self):
		index = 0
		while index < len(self.str[self.index:]):
			# import pdb; pdb.set_trace()
			if self.str[self.index: self.index+index+1] in OPERATORES:
				return (True, index+1)
			if self.str[self.index: self.index+index+1] not in filter(lambda a: len(a)>index, map(lambda a: a[0: index+1], OPERATORES)):
				return (False, index)
			else:
				index += 1
	def parse_string_to_tokens(self):
		if(self.index == len(self.str)):
			print self.tokens
			return
		cur_str = self.str[self.index]
		if self.str[self.index] in KEY_WORDS:
			cur_str += self.str[self.index]
			self.tokens.append(self.str[self.index])
			self.index += 1
		# elif self.str[self.index] in OPERATORES:
			# self.tokens.append(self.str[self.index])
		# elif self.str[self.index] == '!' and self.index+1 != len(self.str) and self.str[self.index+1] == '=':
		elif self.check_str_is_operator()[0]:
			old_index = self.index
			self.index += self.check_str_is_operator()[1]
			self.tokens.append(self.str[old_index: self.index])
		else:
			self.tokens.append(self.str[self.index])
			self.index += 1
		return 	self.parse_string_to_tokens()
m = Tokenizer(test_str)
m.parse_string_to_tokens()


