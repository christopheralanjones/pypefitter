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
        return 'jenkinsfile'
