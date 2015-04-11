
import blocks_swig as blocks
from gnuradio import gr

class vector_selector(gr.basic_block):
    """
    Select index(es) of vector inputs and create a stream (or streams) of those indicies
    """

    def __init__(self, item_size, vec_len, indices):
        """
        Create the block chain.
        
        Args:
            item_size: the size of the samples in the vectors and output streams
            vec_len:   number of elements in the input vectors
            indices:   a list of indicies out of which to create streams
        """

        self._item_size = item_size
        self._vec_len   = vec_len
        self._indicies  = indices
        self._outputs   = len(indices)

        gr.hier_block2.__init__(self, "stream_to_vector_decimator",
                                gr.io_signature(1, 1, item_size*vec_len),
                                gr.io_signature(self._outputs, self._outputs, item_size))

    def general_work(self,input_items, output_items):
        # out = output_items[0]

        return 0;
