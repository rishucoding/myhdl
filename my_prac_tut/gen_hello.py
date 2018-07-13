from myhdl import instance, Signal, delay, block, always, now

#@block
#def clkDriver(clk, period = 20):
	# clk is a asignal parameter
	

@block
def hello(clk, to = "world", period = 20):
	
	lowTime = int(period/2)
	highTime = period - lowTime

	@instance
	def drive_clk(): # explicitily define the desired behaviour
		while(True): # for generator to run forever
			yield delay(lowTime)
			clk.next = 1
			yield delay(highTime)
			clk.next = 0

	#return drive_clk
	#clk = Signal(0)
	#ins = clkDriver(clk)
	#delay(3)
	#clk = Signal(1)

	#@always(delay(10))
	#def drive_clk():
	#	clk.next = not clk # toggle clk, new value of clk by next attribute

	#print ins.clk
	@always(clk.posedge)
	def say_hello():
		print ("%s Hello %s" % (now(), to))

	return drive_clk, say_hello

#clk = Signal(0)
#ins = hello(clk)
#ins.run_sim(50)
