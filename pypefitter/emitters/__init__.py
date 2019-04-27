"""
Contains the base-class Emitters.
"""
from pypefitter.api.emitter import BaseEmitter


class JenkinsEmitter(BaseEmitter):
    """
    A base class for all Jenkins-related emitters.
    """
    @classmethod
    def get_provider_id(cls) -> str:
        """
        Returns the ID of the Provider to which this Emitter is associated.

        Returns
        -------
        str
            The unique ID of the Provider for which this Emitter will emit.
        """
        return 'jenkins'


class AwsEmitter(BaseEmitter):
    """
    A base class for all AWS-related emitters.
    """
    @classmethod
    def get_provider_id(cls) -> str:
        """
        Returns the ID of the Provider to which this Emitter is associated.

        Returns
        -------
        str
            The unique ID of the Provider for which this Emitter will emit.
        """
        return 'aws'
