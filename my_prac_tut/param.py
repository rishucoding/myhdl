from myhdl import always, Signal, delay, instance, block

@block
def clkDriver(clk, period = 20):

	lowTime = int(period/2)
	highTime = period - lowTime

	@instance
	def drive_clk():
		while(True):
			yield delay(lowTime)
			clk.next = 1
			yield delay(highTime)
			clk.next = 0

	return drive_clk