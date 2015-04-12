
import numpy
from gnuradio import gr

class vector_selector(gr.sync_block):
    """
    Select index(es) of vector inputs and create a stream (or streams) of those indicies
    """

    def __init__(self, dtype, vec_len, indices):
        """
        Create the block block

        Args:
            dtype:    the numpy dtype of the numeric values -- vector and stream(s)
            vec_len:  size of the input vectors
            indices:  a list of indicies out of which to create streams
        """

        # APOLOGETIC NOTE:
        #
        # Apparently gnuradio 3.7 hides io sigs behind numpy now.  This is fine
        # and convenient and easy for simple numeric types, but kinda blows for
        # vectors.
        #
        # numpy.dtype( numpy.complex64 ) gives: dtype("complex64")
        # numpy.dtype(numpy.dtype(numpy.dtype("complex64"))) also
        # gives: dtype("complex64").
        #
        # to get a vector(2) structured array type, use this:
        #
        # numpy.dtype("complex64, complex64") which gives:
        #
        # dtype([('f0', '<c8'), ('f1', '<c8')]).
        #
        # When you take the numpy.dtype(<of that>)) you get
        # dtype([('f0', '<c8'), ('f1', '<c8')])
        # right back.
        #
        # Therfore, to get a structured array of dtype complex64 -- the only
        # way I can find to pull this off -- use a huge string join like the
        # below.  When you take the dtype of it, you get a very long tragedy
        # like in the structured dtype shown for the above complex vector.
        #
        # This was all a bunch easier in 3.6 imo:
        #
        #  gr.basic_block.__init__(self, "stream_to_vector_decimator",
        #      gr.io_signature(1, 1, item_size*vec_len),
        #      gr.io_signature(self._outputs, self._outputs, item_size))
        #
        #  Oh well, we live an adapt I guess.

        self._outputs = len(indices)
        self._indices = indices

        gr.sync_block.__init__(self, "vector_selector",
            [ ", ".join( [dtype] * vec_len ) ],
            [dtype] * self._outputs
        )

    def work(self, input_items, output_items):
        _in = input_items[0]

        for e1 in enumerate(_in):
            for e2 in enumerate(self._indices):
                _debug = output_items[ e2[0] ][ e1[0] ] = e1[1][ e2[1] ]
                print "spam: %s \t -> v-slice %d" % (_debug, e2[0])

        print "spam: len=%d\n" % len(_in)
        return len(_in)
