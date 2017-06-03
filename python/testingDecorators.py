def new_decorator(func):
	def temp():
		print("Starting decoration")
		func()
		print("Ending decoration")
	return temp

@new_decorator
def my_func():
	print("I am function to be decorated")

#my_func = new_decorator(my_func)

my_func()	
