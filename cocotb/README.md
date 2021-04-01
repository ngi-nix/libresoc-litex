# Usage

Cocotb is Makefile based. In order to support different configuration and
simulators, run scripts are provided that call the Makefile:

* run_iverilator.sh: Run pre-layout testbench with Icarus Verilog.
* clean.sh: clean up all outputs.

# Dependency

* cocotb: `pip install cocotb`
* iverilog: `apt install iverilog`
* `../libresoc.v`, `../ls180.v`: run `make ls180_verilog` in soc directory,
  `make ls180` in parent directory.  
  Version with SRAMs is currently not supported.

