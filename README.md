tipb-exercise
=============

The Informal Python Bootcamp - Exercise Repository

Participants
------------

* emolch (Sebastian)
* karamzad (Nasim)
* Zaccarelli (Riccardo)
* Al-Halbouni (Djamil)
* FelixMSchneider (Felix und  Jana) 
* nnima (Nima)
* Zakharova (Olya)

Task 1: get started
-------------------

* get a github account
* fork this repos (emolch/tipb-exercise) on your github account
* clone the fork on your machine
* add your name to the participants list above
* commit and push the change to your fork on github
* send me a pull request
* wait for your name to appear in emolch/tipb-exercise
* install Pyrocko if you have not done so yet

Task 2: create and save a Pyrocko trace
---------------------------------------

* the code in `randomtrace.py` creates and displays a Pyrocko trace with random samples
* try it out
* find documentation of `time.time`, `pyrocko.trace.Trace`, and `numpy.random.random`
* read just enough to understand the code
* try to save this trace in Mini-SEED format with `pyrocko.io.save`
* why is this not possible? how solve?
* save the trace in text format (using the `format='text'` option of `pyrocko.io.save`)
* what are the problems with this text format?
* discuss what would make up a good trace file format
* things to consider: simplicity, platform independence, speed, size, meta information, data corruption,
  maximum sampling rate, possible time range / span, jump to given time, streamability, meta data, data types, precision

Task 3: implement a better table-style text file format to store traces
-----------------------------------------------------------------------

* read documentation on `numpy.loadtxt` and `numpy.savetxt`
* commit often while you implement
* start with an empty Python module e.g. `yourname_text_trace_io.py`
* implement a write function `write(trace, filename)`
* implement a read function `read(filename)`
* enhance the read function to allow to only read metadata `read(filename, getdata=False)`
* write a test function which checks if your read and write functions work properly
* upload your work to github, send a pull request
