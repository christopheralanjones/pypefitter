"""
Contains the various default builders
"""
from abc import ABC, abstractmethod


class PypefitterRequestBuilder(ABC):
    """
    The builder is used to construct Pypefitter requests from other sources.

    The most common use of this pattern is build Pypefitter requests from
    the CLI.
    """
    @classmethod
    @abstractmethod
    def assemble(cls, **kwargs) -> None:
        """
        Assemble the materials needed to perform the build. This allows the
        build to perform pre-processing or preparation before being asked to
        produce the finished request.
        """
        pass


class PypefitterPluginCLIRequestBuilder(PypefitterRequestBuilder):
    """
    Build a request from the CLI using the argparse package.
    """
    pass
