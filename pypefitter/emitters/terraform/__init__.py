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
        return 'terraform'
