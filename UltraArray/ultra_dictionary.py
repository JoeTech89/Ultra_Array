from _public import check_key

class UDictionary(dict):
	_name = 'Dictionary'

	def __init__(self, **kwargs):
		super().__init__()
		for k in kwargs:
			self[k] = kwargs[k]

	def __call__(self, **kwargs):
		for k in kwargs:
			self[k] = kwargs[k]

	def __str__(self):
		ret = ''
		end = '\n'
		if len(self) > 0:
			for k in self:
				ret = ret+f"{'[ '+str(k)+' ]':<10}"+f"{self[k]:>5}"+'\n'
		else:
			ret = '{EMPTY}'; end = ''
		print(self._name, ':', end=end)
		return ret
	
	def append(self, **kwargs):
		for k in kwargs:
			nk = check_key(k, self)
			self[nk] = kwargs[k]

	def set(self, what, value):
		what = what.lower()
		if what == 'name' or what == 'n':
			self._name = value
			return self
		else:
			print('Accepted values:', 'name or n')
			return self
# ================================================


class UDictionaryPlus(UDictionary):
	_inner = {}

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def append_key_value(self, key, value):
		self[key] = value

	def append_n(self, value):
		key = len(self)
		self[key] = self

	def append_deep(self, key, value):
		self._inner[key] = value

	def set_name(self, name):
		self._name = name

	def get_deep(self, key):
		if key in self._inner:
			return self._inner.get(key)
		else:
			raise Exception(f"{'['+key+']':<20}"f"{' was not found in dictionary':->80}")


if __name__ == '__main__':
	D=Udict(keyA=1, keyB=2, keyC=3).set('NAME', 'Test Dictionary')
	print()
	# obj = UDictionary(keyA=1, keyB=2, keyC=3).set('NAME', 'Test Dictionary')
	# print('Initialized with...')
	# print(obj)
	# print('Calling Adjustments')
	# obj(keyA=4, keyB=5, keyC=6)
	# print(obj)
	# print('After appending the same keys')
	# obj.append(keyA=1, keyB=2, keyC=3)
	# print(obj)
	# print(f"{'':-<20}")
