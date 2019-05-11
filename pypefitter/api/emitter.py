"""
Contains API-related elements related to emitters.
"""
from pathlib import Path
from pypefitter.api.builder import PypefitterPluginCLIRequestBuilder
from pypefitter.api.plugin import PypefitterPlugin
from pypefitter.api.request import PypefitterRequest


class Emitter(PypefitterPlugin):
    """
    The abstract base class for all emitters. New Emitters should extend the
    BaseEmitter class instead.
    """
    @classmethod
    def get_cli_builder(cls) -> PypefitterPluginCLIRequestBuilder:
        """
        The request builder that will be used to augment the CLI.

        Returns
        -------
        PypefitterRequestBuilder
            The request builder for the plugin.
        """
        return None

    @classmethod
    def get_entry_point(cls) -> str:
        """
        Each class of plugin corresponds to an entry point. the plugin class
        can define its own entry_point, but it has to have one.

        Returns
        -------
        str
            The name of the entry point associated with the plugin.
        """
        return f"{super().get_entry_point()}.emitters"

    @classmethod
    def get_output_file(cls, request: PypefitterRequest, file_name: str) -> str:
        """
        Produces a Path that refers to the location of the specified file_name
        within the target output directory of the request.

        Parameters
        ----------
        request : PypefitterRequest
            The request for which we want to produce the output file path.
        file_name : str
            The name of the file to which we need to produce the path

        Returns
        -------
        str
            A path to the specified file. The path to the file will exist,
            but the file may not.
        """
        output_dir = Path(request.out) / request.provider / request.emitter
        output_dir.mkdir(parents=True, exist_ok=True)
        return str(output_dir / file_name)

    @classmethod
    def emit(cls, request: PypefitterRequest) -> None:
        """
        Performs the  actual emission of the generated code.

        Parameters
        ----------
        request : PypefitterRequest
            The request that triggered this emission.
        """
        pass
