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
    def __init__(self, entry_point):
        """
        Initializes the plugin.

        entry_point
            The entry point metadata that was used to instantiate this
            plugin. This allows the plugin to use its own metadata to mek
            decisions regarding its behavior.
        """
        super().__init__(entry_point)

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
