"""
Contains the base-class Emitters.
"""
from pypefitter.api.emitter import Emitter


class JenkinsEmitter(Emitter):
    """
    A base class for all Jenkins-related emitters.
    """
    pass


class AwsEmitter(Emitter):
    """
    A base class for all AWS-related emitters.
    """
    pass
