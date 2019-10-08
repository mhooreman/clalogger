=====
Usage
=====

This section shows example usage code.

Importing dependencies::

    import pathlib
    from clalogger import (ClaLogger, AbstractLoggerFactory, formatters,
                           handlers, Level)

Concrete implementation of the logger factory, using provided formatters and
handlers. We only have to define the `level` property and the `setupHandlers`
method. That last method takes the logger as argument and typically
instanciates provided handlers and formatters.::

    class MyLoggerFactory(AbstractLoggerFactory):
        @property
        def level(self):
            return Level.debug

        def setupHandlers(self, logger):
            handlers.StandardFileHandler(
                logger, pathlib.Path('spam.log'),
                formatters.DetailedFlatFormatter()
            )
            handlers.StderrHandler(
                logger, formatters.DetailedFlatFormatter(), Level.info
            )


.. note::
    The provided handlers are configuring the logger to use them
    from within their constructor, so that you don't have to worry about that
    association.

.. note::
    The provided handlers constructors can be called without `severity` or
    `severity = None`. In that case, the `logger`'s severity is used.

Definition of a base class for our project. It inherits of the abstract
`ClaLogger` class and implements the `loggerFactoryClass` property, which is
the class we have just defined::

    class Base(ClaLogger):
        @property
        def loggerFactoryClass(self):
            return MyLoggerFactory

And now, our application::

    class Demo(Base):
        def hello(self):
            self.logger.info("Hello, World")


    class Demo2(Base):
        def hello(self):
            self.logger.debug("Hello, World\nDfsmfk\n\tmsqùl")

    def main():
        d = Demo()
        d2 = Demo2()
        for i in range(60):
            d.hello()
            d2.hello()

    if __name__ == '__main__':
        main()


As results, we:

#. Receive the logs on stderr
#. Store the logs in the file `spam.log`
#. Have detailed information in the logs: timestamp, level name, PID,
   class.function and file\@line, separated by a tabulation. The message is
   shown on the next line, every line of the message is prefixed by a
   tablulation.
