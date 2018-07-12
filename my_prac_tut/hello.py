from myhdl import block, delay, always, now

@block
def helloworld():

	@always(delay(10))
	def say_hello():
		print("%s Hello Rishabh! " %now())

	return say_hello

ins = helloworld()
ins.run_sim(50)