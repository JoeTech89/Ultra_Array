
class ultra_dict(dict):
	_inner={}
	_name='Dictionary'

	def __init__(self,**kwargs):
		for k in kwargs:
			self[k]=kwargs[k]


	def append(self,**kwargs):
		for k in kwargs:
			self[k]=kwargs[k]

	def appendKeyValue(self,key,value):
		self[key]=value

	def append_N(self,value):
		key=len(self)
		self[key]=self

	def append_deep(self,key,value):
		self._inner[key]=value

	def set_name(self,name):
		self._name=name

	def get_deep(self,key):
		if key in self._inner:
			return self._inner.get(key)
		else: raise Exception(f"{'['+key+']':<20}"f"{' was not found in dictionary':->80}")

	def __str__(self):
		ret=''
		end='\n'
		if len(self)>0:
			for k in self:
				ret=ret+f"{'['+str(k)+']':-<15}"+f"{'':^5}"+f"{self[k]:<20}"+'\n'
		else:ret='{EMPTY}';end=''
		print(self._name,':',end=end)
		return ret

if __name__=='__main__':
	m=ultra_dict(look='value',I='can',just='add',things='!!!!')
	print(m)