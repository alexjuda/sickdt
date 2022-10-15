======
sickdt
======

> Yo, these datetimes are sick!
> ~Anonymous

Wrapper over the Python stdlib's ``datetime`` package that avoids common gotchas with dates.


Driving Principles
==================

* A ``datetime`` object represents an *instant*, a particular point in time. A snapshot of the universe. It doesn't matter what was the timezone, DST mode, the user's calendar, nor their locale.
* A ``datetime`` on its own isn't human-readable. If you need to show it to the user, you need to provide the timezone or locale.
* All ``datetime`` objects **must** be *timezone-aware*.
* When in need of string timestamps, use `ISO8601 <https://en.wikipedia.org/wiki/ISO_8601>_` with milliseconds and Zulu time.
* When in need of numerical timestamps, use a float for UNIX epoch seconds in UTC.
* This **must** be easy to integrate with existing codebase. No custom data types over stdlib.
* Inspired by the design choices of `NSDate <https://developer.apple.com/documentation/foundation/nsdate>`_.


Similar Projects
================

* `Arrow <https://arrow.readthedocs.io/en/latest/>`_. Requires a total buy-in, you have to switch to using their datatypes.
