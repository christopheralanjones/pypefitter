"""
This module contains the Pypefitter object model. These are the objects that
are produced during parsing and which are consumed and interrogated during
code generation.
"""
from typing import List


class Stage(object):
    """
    A stage represents some location within an overall Pypefitter pipeline.
    Conceptually a pipeline is nothing more than a series of stages and
    each stages can be further subdivided into smaller stages (normally
    called steps). Because there is a lovely recursive relationship between
    stages, we do not currently try to further subdivide them although we
    may in the future.

    A Pypefitter pipeline is considered a series of stages. This is easier to
    deal with than a tree and it really doesn't lose any capability that way.
    """
    def __init__(self, name: str):
        """
        Constructs the Stage.

        Parameters
        ----------
        name : str
            The name of the stage within the Pypefitter pipeline. Within a
            pipeline no two stages may have the same name.
        """
        self.name: str = name
        self.stages: List[Stage] = []


class Pypeline(Stage):
    """
    The Pypeline is the container for all stages and provides some high-level
    oversight for the pipeline as a whole.
    """
    def __init__(self, name: str):
        """
        Constructs the Stage.

        Parameters
        ----------
        name : str
            The name of the stage within the Pypefitter pipeline. Within a
            pipeline no two stages may have the same name.
        """
        Stage.__init__(self, name)
