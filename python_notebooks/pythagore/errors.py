class Error(Exception):
    """Base class for other exceptions"""

    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""

    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""

    pass


class NegativeValue(Error):
    """Raised when the input value negative (<0)"""

    pass


class ValueStrError(Error):
    """Raised when the input value is a string"""

    pass


class ValueComplexError(Error):
    """Raised when the input value is a complex number"""

    pass
