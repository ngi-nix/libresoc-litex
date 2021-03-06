ls1804k:
	./ls180soc.py --build --platform=ls180sram4k --num-srams=2 --srams4k
	cp build/ls180sram4k/gateware/ls180sram4k.v ./ls180.v
	cp build/ls180sram4k/gateware/mem.init .
	cp build/ls180sram4k/gateware/mem_1.init .
	cp libresoc/libresoc.v .
	cp libresoc/SPBlock_512W64B8W.v .
	yosys -p 'read_verilog libresoc.v' \
          -p 'write_ilang libresoc_cvt.il'
	yosys -p 'read_verilog ls180.v' \
	      -p 'read_verilog SPBlock_512W64B8W.v' \
          -p 'write_ilang ls180_cvt.il'
	yosys -p 'read_ilang ls180_cvt.il' \
          -p 'read_ilang libresoc_cvt.il' \
          -p 'write_ilang ls180.il'

ls180:
	./ls180soc.py --build --platform=ls180 --num-srams=2
	cp build/ls180/gateware/ls180.v .
	cp build/ls180/gateware/mem.init .
	cp build/ls180/gateware/mem_1.init .
	cp libresoc/libresoc.v .
	cp libresoc/SPBlock_512W64B8W.v .
	yosys -p 'read_verilog libresoc.v' \
	      -p 'read_verilog ls180.v' \
	      -p 'proc' \
          -p 'write_verilog ls180_cvt.v'
	yosys -p 'read_verilog ls180.v' \
	      -p 'read_verilog SPBlock_512W64B8W.v' \
          -p 'write_ilang ls180_cvt.il'
	yosys -p 'read_verilog libresoc.v' \
          -p 'write_ilang libresoc_cvt.il'
	yosys -p 'read_verilog ls180.v' \
	      -p 'read_verilog SPBlock_512W64B8W.v' \
          -p 'write_ilang ls180_cvt.il'
	yosys -p 'read_ilang ls180_cvt.il' \
          -p 'read_ilang libresoc_cvt.il' \
          -p 'write_ilang ls180.il'

versaecp5:
	 ./versa_ecp5.py --sys-clk-freq=55e6 --build

versaecp5load:
	./versa_ecp5.py --sys-clk-freq=55e6 --load
