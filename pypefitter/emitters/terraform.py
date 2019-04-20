"""
The Terraform emitter.
"""
from pypefitter.emitters import AwsEmitter


class TerraformEmitter(AwsEmitter):
    """
    Represents an Emitter that produces a Terraform representation for AWS
    CodePipeline, CodeBuild, CodeCommit, and CodeDeploy and its associated
    files.
    """
    @classmethod
    def get_emitter_id(cls) -> str:
        return 'terraform'
