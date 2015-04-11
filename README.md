gr-vector-selector
===========

I was experimenting with the gr-fft module, which outputs long vectors.  I
became particularly curious what a constilation plot of a single tap would look
like — it seems pretty obvious if you've looked at the map, but I wanted to see
it.

I couldn't find a vector operator that would select an arbitrary position (e.g.,
the 13th index of every FFT vector) and create a stream of it.  There are built
in operators to go from streams to vectors, and vectors to streams, but none
that decimate in this particular way (afaik).

===========

Requirements

GNU Radio 3.7
python 

*Installing GNU Radio*

maybe just run:
sudo apt-get install gnuradio

or maybe see this page:
http://gnuradio.org/redmine/projects/gnuradio/wiki/InstallingGR


*Installing gr-pyserial*

buildname=gr-vector-selector
buildloc=/tmp/$buildname

git clone http://github.com/jettero/$buildname.git
cd $buildname
src="$(pwd)"
mkdir $buildloc
cd $buildloc
# skip the -DMAKE_INSTALL_PREFIX if you want /usr/local
cmake -DCMAKE_INSTALL_PREFIX=/usr "$src"
sudo make install

# *or* just use my build script
bash build.sh /my/install/prefix/here
