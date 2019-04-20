"""
The Jenkinsfile emitter.
"""
from pypefitter.emitters import JenkinsEmitter


class JenkinsfileEmitter(JenkinsEmitter):
    """
    Represents an Emitter that produces a Jenkinsfile and its associated
    files.
    """
    @classmethod
    def get_emitter_id(cls) -> str:
        """
        Returns the ID of the Emitter.

        Returns
        -------
        str
            The ID of the Emitter. This value will be unique across all
            emitters loaded by the emitter entry point.
        """
        return 'jenkinsfile'
