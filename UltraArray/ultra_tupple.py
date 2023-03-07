print('Note: Tupple Class not working Correctly')
class Tupple(tuple):
	_name='Tuple'

	def __new__(self,*args):
		print(args)
		b=[]
		for a in args:
			b.append(a)
		#self=(b)
		self.__init__(self,b)

	def __init__(self,build):
		print('Initializing')

		if len(build)>0:
		 	print('To Build:',build)
		 	self=(build)


	

if __name__=='__main__':
	t=Tupple(1,2,3,4)
	#t=UTupple()
	#t=(360,180,475)
	print('Tupple:',t)
