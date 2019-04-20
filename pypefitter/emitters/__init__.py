"""
Contains the base-class Emitters.
"""
from pypefitter.api.provider import Emitter


class JenkinsEmitter(Emitter):
    """
    A base class for all Jenkins-related emitters.
    """
    @classmethod
    def get_provider_id(cls) -> str:
        """
        Returns the ID of the Provider that this Emitter supports.
        :return: The ID of the Provider that this Emitter supports.
        """
        return 'jenkins'


class AwsEmitter(Emitter):
    """
    A base class for all AWS-related emitters.
    """
    @classmethod
    def get_provider_id(cls) -> str:
        """
        Returns the ID of the Provider that this Emitter supports.
        :return: The ID of the Provider that this Emitter supports.
        """
        return 'aws'
