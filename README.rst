Artemis - Nozzle Calculator
===========

:Name: Artemis NOzzle Calculator
:Description: Rocket design calculations
:Website: https://www.artemislaunchsystems.com
:Author: AeroPython Team <aeropython@groups.io>
:Version: 0.3.dev0
Calulator package bassed on scikit-aero by by Juan Luis Cano in 2012.
Visit his GitHub: https://github.com/AeroPython/scikit-aero

**Notice**: Outputs are propritary towards the Artemis project. Do not use raw data without adjustment for your project.

Features
--------


* Pythonic interface.
* Use of SI units.
* Full support of NumPy arrays.
* Support for both Python 2 and 3.
* Fully tested and documented.
* Standard atmosphere properties up to 86 kilometers.
* Gas dynamics calculations.
* Metric units

Future
------

* Airspeed conversions.
* Coordinate systems.
* Most of the PDAS.

Usage
=====

Atmosphere properties::

  >>> from skaero.atmosphere import coesa
  >>> h, T, p, rho = coesa.table(1000)  # Altitude by default, 1 km

Inverse computations allowed with density and pressure, which are monotonic::

  >>> h, T, p, rho = coesa.table(p=101325)  # Pressure of 1 atm

Gas dynamics calculations::

  >>> from skaero.gasdynamics import isentropic, shocks
  >>> fl = isentropic.IsentropicFlow(gamma=1.4)
  >>> p = 101325 * fl.p_p0(M=0.8)  # Static pressure given total pressure of 1 atm
  >>> ns = shocks.Shock(M_1=2.5, gamma=1.4)
  >>> M_2 = ns.M_2  # Mach number behind a normal shock wave
  >>> os = shocks.Shock(M_1=3.0, theta=np.radians(25), weak=True)

Dependencies
============

This package depends on Python, NumPy and SciPy and is usually tested on
Linux with the following versions:

* Python 2.7, NumPy 1.6, SciPy 0.11
* Python 3.3, NumPy 1.7.0b2, SciPy 0.11.0

but there is no reason it shouldn't work on Windows or Mac OS X and other
Python versions newer or equal to 2.5. If you are
willing to provide testing on this platforms, please
`contact me <mailto:juanlu001@gmail.com>`_ and if you find any bugs file them
on the `issue tracker`_.

Optional
--------

For running the tests, `py.test`_ is recommended (see `Testing`_). The examples are
in `IPython`_ notebook format, so to run them locally you will need a recent
version of IPython and its dependencies.

.. _`py.test`: http://pytest.org
.. _`IPython`: http://ipython.org/

Testing
=======

scikit-aero recommends py.test for running the test suite. Running from the
top directory::

  $ py.test

To test code coverage, make sure you install `py.test-cov`_ extension and run::

  $ py.test --cov skaero/

.. _`py.test-cov`: https://pypi.python.org/pypi/pytest-cov

Examples
========

Some applied examples are in the folder `examples` in the IPython notebook
format. To see them without running locally, use `nbviewer`_; for example,
to see the `cd_nozzle.ipynb` notebook, browse to

http://nbviewer.ipython.org/url/raw.github.com/Pybonacci/scikit-aero/master/examples/Oblique%20shocks%20chart.ipynb

.. _`nbviewer`: http://nbviewer.ipython.org/


License
=======

scikit-aero is released under a 2-clause BSD license, hence allowing commercial use
of the library. Please refer to the COPYING file.

Reff.
========

* `AeroCalc`_, package written by Kevin Horton which inspired scikit-aero.
* `MATLAB Aerospace Toolbox`_,
* `PDAS`_, the Public Domain Aeronautical Software.

.. _Aerocalc: http://pypi.python.org/pypi/AeroCalc/0.11
.. _`MATLAB Aerospace Toolbox`: http://www.mathworks.com/help/aerotbx/index.html
.. _PDAS: http://www.pdas.com/index.html
