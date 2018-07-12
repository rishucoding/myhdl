from myhdl import block, delay, always, now

@block # modelling of hardware module 
def helloworld(): # parameter list defines the interface 

	@always(delay(10)) # the function say_hello executes whenever 
	# the delay interval gets expired
	def say_hello():
		print("%s Hello Rishabh! " %now())

	return say_hello

ins = helloworld()
ins.run_sim(50) # run-sim is a method to simulate the desired number of 
# timesteps
	