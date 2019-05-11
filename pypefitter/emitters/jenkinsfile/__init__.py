"""
The Jenkinsfile emitter.
"""
from jinja2 import Environment, PackageLoader
from pypefitter.emitters import JenkinsEmitter
from pypefitter.api.request import PypefitterRequest


class JenkinsfileEmitter(JenkinsEmitter):
    """
    Represents an Emitter that produces a Jenkinsfile and its associated
    files.
    """
    @classmethod
    def get_plugin_id(cls) -> str:
        """
        Each class of plugin needs to have its own to help uniquely identify it
        within its entry point.

        Returns
        -------
        str
            The ID of the plugin that uniquely identifies it within its entry
            point.
        """
        return 'jenkinsfile'

    @classmethod
    def emit(cls, request: PypefitterRequest) -> None:
        """
        Performs the  actual emission of the generated code.

        Parameters
        ----------
        request : PypefitterRequest
            The request that triggered this emission.
        """
        env = Environment(
            loader=PackageLoader(f"{cls.get_entry_point()}.{request.emitter}", 'templates'),
        )
        template = env.get_template('main')
        file_content: str = template.render()

        output_file: str = cls.get_output_file(request, 'Jenkinsfile')
        with open(output_file, 'w') as pf_file:
            pf_file.write(file_content)
