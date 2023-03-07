
class UArray(list):
	_name='List'
	def __init__(self,*args):
		for a in args:
			self.append(a)

	def __str__(self):
		ret=''
		end='\n'
		if len(self)>0:
			for i in range(0,len(self)):
				#print('--:',self[i])
				ret+=f"{str(i):>5}"+f"{'['+str(self[i])+']':<10}"+'\n'
				#ret=ret+str(i)
		else: ret = '{EMPTY}'; end = ''
		print(self._name,':',end=end)
		return ret

	def set(self, what, value):
		what = what.lower()
		if what == 'name' or what == 'n':
			self._name = value
			return self
		else:
			print('Accepted values:', 'name or n')
			return self

if __name__=='__main__':
	print(f"{'Testing Array Module':-^100}")
	a=UArray(1,2,3,4).set('name','Custom List')
	print(a)