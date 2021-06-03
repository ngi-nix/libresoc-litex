module pll(input [0:0] ref_v,
           output [0:0] div_out_test,
           input [0:0] a0, 
           input [0:0] a1,
           output [0:0] vco_test_ana, 
           output [0:0] out_v);
  /* fake PLL */
  assign out_v = ref_v;
endmodule

