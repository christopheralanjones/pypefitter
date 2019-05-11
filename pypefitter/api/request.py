"""
Holds the request-related elements for interacting with the Pypefitter API.
"""


class PypefitterRequest(object):
    """
    A request provided to the Pypefitter API.
    """
    def __init__(self, action: str, provider: str, file: str, out: str, **kwargs):
        """
        Initializes the PypefitterRequest. The kwargs can contain arbitrary
        data, but it must be understood by the receiver of the request.

        Parameters
        ----------
        action : str
            The name of the action to be executed.
        provider :  str
            The name of the provider to be used.
        file : str
            The full path to the file to be used.
        out : str
            The directory where any output will be placed.
        """
        self.action = action
        self.file = file
        self.out = out
        self.provider = provider
        self.__dict__.update(kwargs)


class PypefitterResponse(object):
    """
    A response provided by the Pypefitter API resulting from a
    PypefitterRequest.
    """
    def __init__(self, return_code: int = 200, reason: str = 'OK', **kwargs):
        """
        Initializes the PypefitterResponse

        Parameters
        ----------
        return_code : str
            The code representing the response. As much as possible we try to
            adhere to HTTP response codes, but this isn't mandatory.
        reason : str
            Any text that can help shed light on why the `return_code` is what
            it is.
        """
        self.return_code = return_code
        self.reason = reason
        self.__dict__.update(kwargs)
