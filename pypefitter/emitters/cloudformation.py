"""
The CloudFormation emitter.
"""
from pypefitter.emitters import AwsEmitter


class CloudFormationEmitter(AwsEmitter):
    """
    Represents an Emitter that produces a CloudFormation representation for AWS
    CodePipeline, CodeBuild, CodeCommit, and CodeDeploy and its associated
    files.
    """
    @classmethod
    def get_emitter_id(cls) -> str:
        return 'cloudformation'
