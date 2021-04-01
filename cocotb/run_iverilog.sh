#!/bin/sh

touch mem.init mem_1.init mem_2.init mem_3.init mem_4.init
# Only run test in reset state as running CPU takes too much time to simulate
make \
  SIM=icarus \
  COCOTB_RESULTS_FILE=results_iverilog.xml \
  COCOTB_HDL_TIMEUNIT=100ps \
  TESTCASE="idcode_reset,idcodesvf_reset" \
  SIM_BUILD=sim_build_iverilog


