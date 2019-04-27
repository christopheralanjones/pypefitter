"""
Defines the JenkinsProvider provider.
"""
from pypefitter.api import Provider
from pypefitter.api.provider import BaseProvider


class JenkinsProvider(BaseProvider):
    """
    Provides services related to the Jenkins platform.
    """
    __instance: Provider = None

    def __new__(cls):
        """
        We want to treat this class as a singleton since there's no good
        reason to have multiple instances of it.
        :return: The single instance of the JenkinsProvider.
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    @classmethod
    def get_provider_id(cls) -> str:
        return 'jenkins'
