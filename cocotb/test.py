import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotb.utils import get_sim_steps
from cocotb.binary import BinaryValue

from c4m.cocotb.jtag.c4m_jtag import JTAG_Master
from c4m.cocotb.jtag.c4m_jtag_svfcocotb import SVF_Executor

#
# Helper functions
#

def setup_sim(dut, *, clk_period, run):
    """Initialize CPU and setup clock"""

    clk_steps = get_sim_steps(clk_period, "ns")
    cocotb.fork(Clock(dut.sys_clk, clk_steps).start())

    dut.sys_rst <= 1
    dut.sys_clk <= 0
    if run:
        yield Timer(int(10.5*clk_steps))
        dut.sys_rst <= 0
        yield Timer(int(5*clk_steps))

def setup_jtag(dut, *, tck_period):
    # Make this a generator
    if False:
        yield Timer(0)
    return JTAG_Master(dut.jtag_tck, dut.jtag_tms, dut.jtag_tdi, dut.jtag_tdo, clk_period=tck_period)

def execute_svf(dut, *, jtag, svf_filename):
    jtag_svf = SVF_Executor(jtag)
    with open(svf_filename, "r") as f:
        svf_deck = f.read()
    yield jtag_svf.run(svf_deck, p=dut._log.info)
    
#
# IDCODE using JTAG_master
#

def idcode(dut, *, jtag):
    jtag.IDCODE = [0, 0, 0, 1]
    yield jtag.idcode()
    result1 = jtag.result
    dut._log.info("IDCODE1: {}".format(result1))
    assert(result1 == BinaryValue("00000000000000000001100011111111"))

    yield jtag.idcode()
    result2 = jtag.result
    dut._log.info("IDCODE2: {}".format(result2))

    assert(result1 == result2)

@cocotb.test()
def idcode_reset(dut):
    dut._log.info("Running IDCODE test; cpu in reset...")

    clk_period = 100 # 10MHz
    tck_period = 300 # 3MHz

    yield from setup_sim(dut, clk_period=clk_period, run=False)
    jtag = yield from setup_jtag(dut, tck_period = tck_period)

    yield from idcode(dut, jtag=jtag)

    dut._log.info("IDCODE test completed")

@cocotb.test()
def idcode_run(dut):
    dut._log.info("Running IDCODE test; cpu running...")

    clk_period = 100 # 10MHz
    tck_period = 300 # 3MHz

    yield from setup_sim(dut, clk_period=clk_period, run=True)
    jtag = yield from setup_jtag(dut, tck_period = tck_period)

    yield from idcode(dut, jtag=jtag)

    dut._log.info("IDCODE test completed")

#
# Read IDCODE from SVF file
#

@cocotb.test()
def idcodesvf_reset(dut):
    dut._log.info("Running IDCODE through SVF test; cpu in reset...")

    clk_period = 100 # 10MHz
    tck_period = 300 # 3MHz

    yield from setup_sim(dut, clk_period=clk_period, run=False)
    jtag = yield from setup_jtag(dut, tck_period = tck_period)

    yield from execute_svf(dut, jtag=jtag, svf_filename="idcode.svf")

    dut._log.info("IDCODE test completed")

@cocotb.test()
def idcode_run(dut):
    dut._log.info("Running IDCODE through test; cpu running...")

    clk_period = 100 # 10MHz
    tck_period = 300 # 3MHz

    yield from setup_sim(dut, clk_period=clk_period, run=True)
    jtag = yield from setup_jtag(dut, tck_period = tck_period)

    yield from execute_svf(dut, jtag=jtag, svf_filename="idcode.svf")

    dut._log.info("IDCODE test completed")

