# sim openocd test

in the soc directory, create the verilog file
    "python issuer_verilog.py libresoc.v"

copy to libresoc/ directory
terminal 1: ./sim.py
terminal 2: openocd -f openocd.cfg -c init -c 'svf idcode_test2.svf'

# ecp5 build

same thing: first build libresoc.v and copy it to the libresoc/ directory

./versa_ecp5.py --sys-clk-freq=55e6 --build
./versa_ecp5.py --sys-clk-freq=55e6 --load
