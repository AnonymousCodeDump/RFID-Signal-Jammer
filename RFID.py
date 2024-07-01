#!/usr/bin/env python
from gnuradio import gr
from gnuradio import analog
from gnuradio import blocks
import sys


class RFIDJammer(gr.top_block):
    def __init__(self, freq):
        gr.top_block.__init__(self)

        samp_rate = 1e6  # Sample rate of 1 MHz
        amplitude = 0.1  # Amplitude of the jamming signal

        # Source of the jamming signal - a simple sine wave
        self.src = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, amplitude)

        # Null sink - we're not actually processing the signal, just generating it
        self.sink = blocks.null_sink(gr.sizeof_gr_complex)

        # Connect the source to the sink
        self.connect(self.src, self.sink)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: rfid_jammer.py [frequency]")
        sys.exit(1)

    freq = float(sys.argv[1])
    jammer = RFIDJammer(freq)
    jammer.run()
