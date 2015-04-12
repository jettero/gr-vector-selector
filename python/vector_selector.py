
import numpy, math
from gnuradio import gr
from operator import itemgetter

INDEX_MODE  = 0
MINMAX_MODE = 1

class vector_selector(gr.sync_block):
    """
    Select index(es) of vector inputs and create a stream (or streams) of those indicies
    """

    def __init__(self, dtype, vec_len, indices, modality=INDEX_MODE, debug=False):
        """
        Create the block block

        Args:
            dtype:    the numpy dtype of the numeric values -- vector and stream(s)
            vec_len:  size of the input vectors
            indices:  a list of indicies out of which to create streams
            debug:    be spammy on the console
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

        self._outputs  = len(indices)
        self._indices  = indices
        self._debug    = debug
        self._modality = modality

        gr.sync_block.__init__(self, "vector_selector",
            [ ", ".join( [dtype] * vec_len ) ],
            [dtype] * self._outputs
        )

    def set_indices(self, indices):
        self._indices = indices

    def work(self, input_items, output_items):
        _in = input_items[0]

        if self._modality == INDEX_MODE:
            for (i_idx, i_vec) in enumerate(_in):
                for (o_stream_idx, i_vec_idx) in enumerate(self._indices):
                    c = i_vec[ i_vec_idx ]
                    output_items[ o_stream_idx ][ i_idx ] = c

                    if self._debug:
                        print "spam: <%s> %7.2fi + %7.2fj -> v-slice %d @[%d]" % (
                            numpy.dtype(c),
                            c.real, c.imag,
                            o_stream_idx,
                            i_idx,
                        )

        elif self._modality == MINMAX_MODE:
            for (i_idx, i_vec) in enumerate(_in):
                mlist = []
                for (i,c) in enumerate(i_vec):
                    mlist.append( (i, math.sqrt( c.real ** 2 + c.imag ** 2 )) )
                mlist = sorted(mlist, key=itemgetter(1))

                for (o_stream_idx, i_nth_max) in enumerate(self._indices):
                  ct = mlist[ i_vec_idx ]
                  output_items[ o_stream_idx ][ i_idx ] = ct

                  if self._debug:
                      print "spam: <%s> %7.2fi + %7.2fj @[%d] -> v-slice %d @[%d]" % (
                          numpy.dtype(ct[1]),
                          ct[1].real, ct[1].imag, ct[0],
                          o_stream_idx,
                          i_idx,
                      )
        else:
            raise AttributeError("modality not understood")

        if  self._debug:
            print "spam: len=%d\n" % len(_in)

        return len(_in)
