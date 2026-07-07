class ProboError(Exception):
    """
    Base exception class for all Probo UI specific errors.
    
    All custom exceptions in the probo package should inherit from this class
    to allow users to catch any probo-related error easily.
    """
    pass
