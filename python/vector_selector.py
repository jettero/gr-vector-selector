
import numpy, math
from gnuradio import gr
from operator import itemgetter

INDEX_MODE  = 1234
MINMAX_MODE = 5678

class vector_selector(gr.sync_block):
    """
    Select index(es) of vector inputs and create a stream (or streams) of those indices
    """

    def __init__(self, dtype, vec_len, indices, modality=INDEX_MODE, debug=False):
        """
        Create the block block

        Args:
            dtype:    the numpy dtype of the numeric values -- vector and stream(s)
            vec_len:  size of the input vectors
            indices:  a list of indices out of which to create streams
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
        self._modality = modality
        self._dtype    = dtype
        self._indices  = indices + ()  # A:A+I→A so the error is right here on bad arg
        self._debug    = not not debug # same idea as above

        gr.sync_block.__init__(self, "vector_selector",
            [ ", ".join( [dtype] * vec_len ) ],
            [ "%s,%s" % (dtype,dtype) ] * self._outputs if modality == MINMAX_MODE else [ dtype ] * self._outputs
        )

    def change_settings(self, indices, debug):
        if len(indices) != len(self._indices):
            print "attempt to change lenght of indices list ignored"
        else:
            self._indices = indices + ()
        self._debug = not not debug

        print "change_settings(indices=%s, debug=%s)" % (indices,debug)

    def work(self, input_items, output_items):
        _in = input_items[0]

        if self._modality == INDEX_MODE:
            for (i_idx, i_vec) in enumerate(_in):
                for (o_stream_idx, i_vec_idx) in enumerate(self._indices):
                    c = i_vec[ i_vec_idx ]
                    output_items[ o_stream_idx ][ i_idx ] = c

                    if self._debug:
                        if self._dtype == "complex64":
                            print "spam[idx]: %7.2fi + %7.2fj @[%d] -> @[%d][%d]" % (
                                c.real, c.imag, i_vec_idx,
                                o_stream_idx, i_idx,
                            )

                        else:
                            print "spam[idx]: %s @[%d] -> @[%d][%d]" % ( c, o_stream_idx, i_idx )

        elif self._modality == MINMAX_MODE:
            for (i_idx, i_vec) in enumerate(_in):
                mlist = []
                for (i,c) in enumerate(i_vec):
                    m = math.sqrt( c.real ** 2 + c.imag ** 2 ) if self._dtype == "complex64" else c
                    mlist.append( (i, c, m) )
                mlist = sorted(mlist, key=itemgetter(2), reverse=True)

                for (o_stream_idx, i_nth_max) in enumerate(self._indices):
                  ct = mlist[ i_nth_max ]
                  ct = (ct[0], ct[1])
                  output_items[ o_stream_idx ][ i_idx ] = ct

                  if self._debug:
                    if self._dtype == "complex64":
                      print "spam[max]: (@[%4d], %7.2fi + %7.2fj) @[%d] -> @[%d][%d]" % (
                          ct[0], ct[1].real, ct[1].imag, i_nth_max,
                          o_stream_idx, i_idx,
                      )
                    else:
                        print "spam[max]: (@[%4d],%s) -> @[%d][%d]" % ( ct, o_stream_idx, i_idx )
        else:
            raise AttributeError("modality not understood")

        return len(_in)
