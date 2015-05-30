gr-vector-selector
==================

You can do some really cool things with single FFT output BINs.  Why is there no
way (that I can find) to extract one or more bins from the FFT output in a
useful/arbitrary way?

*Requirements*

* GNU Radio 3.7
* python

Installing GNU Radio
====================

maybe just run:
sudo apt-get install gnuradio

or maybe see this page:
http://gnuradio.org/redmine/projects/gnuradio/wiki/InstallingGR


Installing the Alternate Moving Averages
========================================

*using my build script*

    PREFIX=/usr ./build.sh

*building by hand*

    buildname=gr-alt-moving-average
    buildloc=/tmp/$buildname

    git clone http://github.com/jettero/$buildname.git
    cd $buildname
    src="$(pwd)"
    mkdir $buildloc
    cd $buildloc

    # skip the -DMAKE_INSTALL_PREFIX if you want /usr/local
    cmake -DCMAKE_INSTALL_PREFIX=/usr "$src"
    sudo make install
