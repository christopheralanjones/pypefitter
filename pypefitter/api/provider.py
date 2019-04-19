"""
Defines the classes that are used to implement providers for the various
platforms.
"""


class Provider:
    """
    Defines the Provider API, which is used to declare concrete Provider
    implementations for platforms like Jenkins or AWS.
    """

    def generate(self):
        """
        Performs the actual code generation process.
        :return:
        """
        pass

    def validate(self):
        """
        Performs a validation step to ensure that there is enough information
        provided that a subsequent code generation request will succeed.
        :return:
        """
        pass
