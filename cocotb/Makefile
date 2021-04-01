ifeq ($(SIM),)
  $(error Use one of the run_*.sh scripts to run cocotb test bench)
endif

TOPLEVEL_LANG := verilog

VERILOG_SOURCES := \
  ../libresoc.v \
  ../ls180.v \
# END VERILOG_SOURCES

TOPLEVEL := ls180
MODULE := test

include $(shell cocotb-config --makefiles)/Makefile.sim

