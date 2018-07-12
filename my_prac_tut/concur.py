from myhdl import block, Signal, now, delay, always

@block 
def helloworld():

	clk = Signal(0)
	#delay(3)
	#clk = Signal(1)

	@always(delay(10))
	def drive_clk():
		clk.next = not clk # toggle clk, new value of clk by next attribute

	@always(clk.posedge)
	def say_hello(): # function sensitive to rising edge of clk
		print ("%s Hello Risabh" % now())

	return drive_clk, say_hello

inst = helloworld()# two generators drive_clk and printing hello
# are running in concurrently
inst.run_sim(55)