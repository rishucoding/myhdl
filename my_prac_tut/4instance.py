from myhdl import block, Signal

from param import clkDriver
from gen_hello import hello

@block
def Greetings():

	clk1 = Signal(0)
	clk2 = Signal(0)

	clkdriver_1 = clkDriver(clk1) # clk1 is positional, period is default association
	clkdriver_2 = clkDriver(clk = clk2, period = 19) # named association
	hello_1 = hello(clk = clk1) # named and default association
	hello_2 = hello(to = "myhdl", clk = clk2) # named associ

	return clkdriver_1, clkdriver_2, hello_2, hello_1

inst = Greetings()
inst.run_sim(100)

