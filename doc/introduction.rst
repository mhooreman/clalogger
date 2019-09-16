============
Introduction
============

This package provides a `ClaLogger` class which is providing a `logger`
property, which is a `logging.Logger` who's name is the class name.

This `logger` is created by a factory which is provided as an `abstract` class,
in order to allow configuration.

In addition to that, some configured items (handlers, formatters) are provided.

The intended approach is to define a common base class for your project which
inherits of `ClaLogger` and provides a concrete implementation of the factory.
The other classes of your projects must then inherit of that base class, so
that they use `self.logger`, or `cls.logger` in a static way, the same way as
`logging.Logger` objects are used.
