.. |pypi-badge| image:: https://img.shields.io/pypi/v/rigolwfm-dho800?color=68CA66
   :target: https://pypi.org/project/rigolwfm-dho800/
   :alt: pypi

.. |github-badge| image:: https://img.shields.io/github/v/tag/aimoda/rigolwfm-dho800?label=github&color=68CA66
   :target: https://github.com/aimoda/rigolwfm-dho800
   :alt: github

.. |kaitaistruct| image:: https://img.shields.io/badge/kaitai-struct-68CA66
   :target: https://ide.kaitai.io
   :alt: kaitai-struct

.. |zenodo-badge| image:: https://zenodo.org/badge/244228290.svg
   :target: https://zenodo.org/badge/latestdoi/244228290
   :alt: doi

.. |license-badge| image:: https://img.shields.io/github/license/aimoda/rigolwfm-dho800?color=68CA66
   :target: https://github.com/aimoda/rigolwfm-dho800/blob/main/LICENSE.txt
   :alt: License

.. |downloads-badge| image:: https://img.shields.io/pypi/dm/rigolwfm-dho800?color=68CA66
   :target: https://pypi.org/project/rigolwfm-dho800/
   :alt: Downloads

rigolwfm-dho800
===============

by ai.moda (Fork of RigolWFM by Scott Prahl)

A utility to process Rigol DHO800 series oscilloscope ``.wfm`` files
--------------------------------------------------------------------

|pypi-badge| |github-badge| |kaitaistruct|

|license-badge| |downloads-badge|

**Note**: This is a fork of scottprahl/RigolWFM focused on DHO800 series support (DHO804, DHO814, DHO824, DHO914, DHO924). For the original project supporting other Rigol oscilloscope series, visit `RigolWFM <https://github.com/scottprahl/RigolWFM>`_.

This project provides tools to interpret waveform ``.wfm`` files created by Rigol DHO800 series oscilloscopes. It leverages kaitai struct, a domain specific language to represent binary files.  Once a binary file has been described in this text format, parsers can be generated for a wide range of languages (C++/STL, C#, Go, Java, JavaScript, Lua, Perl, PHP, Python, and Ruby).

Original documentation: <https://RigolWFM.readthedocs.io>

Installation
---------------

You can install locally using pip::

    pip install --user rigolwfm-dho800

or `analyze your files using the kaitai struct IDE <https://ide.kaitai.io>`_ (you will need to manually upload the appropriate `.ksy` file and your `.wfm` to the IDE).  This allows one to interactively reverse engineer binary file formats directly in your browser.  This is super helpful for those Rigol ``.wfm`` formats that are undocumented or not parsing correctly.


Usage
-----

Once ``RigolWFM`` is installed, you can plot the signals from binary Rigol ``.wfm`` files by::

   import matplotlib.pyplot as plt
   import RigolWFM.wfm as rigol

   filename = 'example.wfm'
   scope = 'DS1000E'

   w = rigol.Wfm.from_file(filename, scope)
   w.plot()
   plt.show()


Alternatively, ``wfmconvert`` can be used from the command line.  For example, the following should convert all the DS1000E files in the current directory to the ``.csv`` format::

   prompt> wfmconvert E csv *.wfm

If you just wanted to convert channel 1 from a single file to ``.csv`` then::

   prompt> wfmconvert --channel 1 E csv DS1102E.wfm

If you wanted to a signal `.wav` file using the second channel waveform (for use with LTspice) then:: 

   prompt> wfmconvert --channel 2 E wav *.wfm

If you want to create a ``.wav`` file with channels one and four as signals (and autoscale for use with Audacity or Sigrok Pulseview)::

   prompt> wfmconvert --autoscale --channel 14 E wav *.wfm

Status
------

There is a bit of work remaining (testing, validation, repackaging) but there are binary file descriptions for ``.wfm`` files created by the following scopes:

* DS1000B tested 
* DS1000C tested (two files only)
* DS1000D tested (one file only)
* DS1000E tested
* DS1000Z tested, but with wonky voltage offsets
* DS2000 tested
* DS4000 tested
* DS6000 untested

Resources
---------

This has been a bit of an adventure.  In the process of nailing down the basic formats, I have gleaned information from a wide range of projects started by others.


* Shein's Pascal program <https://sourceforge.net/projects/wfmreader>
* Wagenaars's Matlab script <https://www.mathworks.com/matlabcentral/fileexchange/18999-read-binary-rigol-waveforms>
* Steele's C program <http://nsweb.tn.tudelft.nl/~gsteele/rigol2dat>
* Blaicher's python code <https://github.com/mabl/pyRigolWFM>
* Szkutnik's python code <https://github.com/michal-szkutnik/pyRigolWfm1000Z>
* Cat-Ion's python code <https://github.com/Cat-Ion/rigol-ds4000-wfm>
* Šolc's python code <https://www.tablix.org/~avian/blog/archives/2019/08/quick_and_ugly_wfm_data_export_for_rigol_ds2072a/>
* Contributions from <http://www.hakasoft.com.au/wfm_viewer>
* A LabView program I got from Rigol support
* Rigol's documentation of the 1000E, 1000Z, 2000, and 6000 file formats.


Source code repository
-------------------------------------------

    <https://github.com/aimoda/rigolwfm-dho800>

Original upstream project
-------------------------------------------

    <https://github.com/scottprahl/RigolWFM>

License
-------
    BSD 3-clause -- see the file ``LICENSE`` for details.
