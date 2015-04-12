#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Vectorselectordemo
# Generated: Sun Apr 12 10:37:10 2015
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import grvectorselector
import sip
import sys

class VectorSelectorDemo(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Vectorselectordemo")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Vectorselectordemo")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "VectorSelectorDemo")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 256000
        self.fft_size = fft_size = 1024
        self.freq = freq = 8000
        self.Hz_per_slice = Hz_per_slice = (samp_rate/2.0) / fft_size
        self.tap = tap = int( (fft_size/2) + (freq/Hz_per_slice) )

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_tab_widget_0 = Qt.QTabWidget()
        self.qtgui_tab_widget_0_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_0)
        self.qtgui_tab_widget_0_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_0.addLayout(self.qtgui_tab_widget_0_grid_layout_0)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_0, "QT GUI")
        self.qtgui_tab_widget_0_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_1)
        self.qtgui_tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_1.addLayout(self.qtgui_tab_widget_0_grid_layout_1)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_1, "V-Slice 0")
        self.qtgui_tab_widget_0_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_2)
        self.qtgui_tab_widget_0_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_2.addLayout(self.qtgui_tab_widget_0_grid_layout_2)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_2, "V-Slice 1")
        self.qtgui_tab_widget_0_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_3)
        self.qtgui_tab_widget_0_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_3.addLayout(self.qtgui_tab_widget_0_grid_layout_3)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_3, "V-Slice 2")
        self.top_layout.addWidget(self.qtgui_tab_widget_0)
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel("freq"+": "))
        self._freq_line_edit = Qt.QLineEdit(str(self.freq))
        self._freq_tool_bar.addWidget(self._freq_line_edit)
        self._freq_line_edit.returnPressed.connect(
        	lambda: self.set_freq(eng_notation.str_to_num(self._freq_line_edit.text().toAscii())))
        self.top_layout.addWidget(self._freq_tool_bar)
        self.vector_selector_0 = grvectorselector.vector_selector(dtype="complex64",vec_len=fft_size,indices=(( tap -1, tap, tap+1 )))
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	64, #size
        	samp_rate / fft_size, #samp_rate
        	"V-slice 2", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_NEG, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_layout_3.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	64, #size
        	samp_rate / fft_size, #samp_rate
        	"V-slice 0", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_NEG, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	64, #size
        	samp_rate / fft_size, #samp_rate
        	"V-slice 1", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	fft_size, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_layout_0.addWidget(self._qtgui_sink_x_0_win)
        
        def qtgui_sink_x_0_callback(p, num):
        	if num == 1 or num == 2: self.set_freq(p.x())
        	
        Qt.QObject.connect(self._qtgui_sink_x_0_win, Qt.SIGNAL("plotPointSelected(QPointF, int)"), qtgui_sink_x_0_callback )
        
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (window.blackmanharris(fft_size)), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.vector_selector_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.vector_selector_0, 1), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.vector_selector_0, 2), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.fft_vxx_0, 0), (self.vector_selector_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "VectorSelectorDemo")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Hz_per_slice((self.samp_rate/2.0) / self.fft_size)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.fft_size)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.fft_size)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.fft_size)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.set_Hz_per_slice((self.samp_rate/2.0) / self.fft_size)
        self.set_tap(int( (self.fft_size/2) + (self.freq/self.Hz_per_slice) ))
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.fft_size)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.fft_size)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.fft_size)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_tap(int( (self.fft_size/2) + (self.freq/self.Hz_per_slice) ))
        self.analog_sig_source_x_0.set_frequency(self.freq)
        self._freq_line_edit.setText(eng_notation.num_to_str(self.freq))

    def get_Hz_per_slice(self):
        return self.Hz_per_slice

    def set_Hz_per_slice(self, Hz_per_slice):
        self.Hz_per_slice = Hz_per_slice
        self.set_tap(int( (self.fft_size/2) + (self.freq/self.Hz_per_slice) ))

    def get_tap(self):
        return self.tap

    def set_tap(self, tap):
        self.tap = tap

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = VectorSelectorDemo()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

