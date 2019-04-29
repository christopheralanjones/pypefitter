"""
Defines the classes that are used to implement providers for the various
platforms.
"""
from pypefitter.api.builder import PypefitterPluginCLIRequestBuilder, PypefitterProviderCLIRequestBuilder
from pypefitter.api.emitter import Emitter
from pypefitter.api.plugin import PluginManager, PypefitterPlugin, PypefitterPluginNotFoundError
from pypefitter.api.request import PypefitterRequest, PypefitterResponse
from typing import List


class Provider(PypefitterPlugin):
    """
    Defines the Provider API, which is used to declare concrete Provider
    implementations for platforms like Jenkins or AWS.
    """
    @classmethod
    def get_cli_builder(cls) -> PypefitterPluginCLIRequestBuilder:
        """
        The request builder that will be used to augment the CLI.

        Returns
        -------
        PypefitterRequestBuilder
            The request builder for the plugin.
        """
        return PypefitterProviderCLIRequestBuilder()

    @classmethod
    def get_actions(cls) -> List:
        """
        Gets the Actions that have been registered for this Provider. We do
        this by assembling the common actions from the pypefitter actions
        entry point and then adding in any provider-specific actions from
        the provider actions entry point.

        Returns
        -------
        List[Action]
            The Actions associated with the provider's action entry point.
        """
        # get all of the actions
        all_actions: List[PypefitterPlugin] = []
        common_actions: List[PypefitterPlugin] = \
            PluginManager.get_plugins(f"{cls.get_entry_point()}.actions")
        provider_actions: List[PypefitterPlugin] = \
            PluginManager.get_plugins(f"{cls.get_entry_point()}.{cls.get_plugin_id()}.actions")

        # assemble the final list
        if common_actions:
            all_actions.extend(common_actions)
        if provider_actions:
            all_actions.extend(provider_actions)
        return all_actions

    @classmethod
    def get_action(cls, plugin_id: str):
        """
        Gets the action with the specified plugin ID. We first look for
        provider-specific actions and then look for common actions after
        that.

        Returns
        -------
        Action
            The Action with the specified plugin_id. The precedence is that
            the provider's entry point is considered first and then the
            common actions.
        """
        try:
            action = PluginManager.get_plugin(f"{cls.get_entry_point()}.{cls.get_plugin_id()}.actions", plugin_id)
        except PypefitterPluginNotFoundError:
            action = PluginManager.get_plugin(f"{cls.get_entry_point()}.actions", plugin_id)
        return action

    def do_action(self, request: PypefitterRequest) -> PypefitterResponse:
        """
        Performs an action.

        Parameters
        ----------
        request : PypefitterRequest
            The request that encapsulates all of the information acquired
            when pypefitter was invoked.

        Returns
        -------
        PypefitterResponse
            The result of the request being performed.
        """
        try:
            action = self.get_action(request.action)
            response: PypefitterResponse = action.do_action(self, request)
        except PypefitterPluginNotFoundError as ppnfe:
            response = PypefitterResponse(400, ppnfe.message)
        return response

    @classmethod
    def get_entry_point(cls) -> str:
        """
        Each class of plugin corresponds to an entry point. the plugin class
        can define its own entry_point, but it has to have one.

        Returns
        -------
        str
            The name of the entry point associated with the plugin.
        """
        return 'pypefitter.providers'

    @classmethod
    def get_emitters(cls) -> List[Emitter]:
        """
        Gets the Emitters that have been registered for this Provider.

        Returns
        -------
        List[Emitter]
            The Emitters associated with the provider's emitter entry point.
        """
        emitters: List[PypefitterPlugin] = \
            PluginManager.get_plugins(f"{cls.get_entry_point()}.{cls.get_plugin_id()}.emitters")
        return emitters

    @classmethod
    def get_providers(cls) -> List:
        """
        Gets the Providers that have been installed to Pypefitter's providers
        entry point.

        Returns
        -------
        List[Provider]
            The Providers associated with Pypefitter's provider entry point.
        """
        providers: List[PypefitterPlugin] = \
            PluginManager.get_plugins(cls.get_entry_point())
        return providers

    @classmethod
    def get_provider(cls, plugin_id: str):
        """
        Gets the Emitters that have been registered for this Provider.

        Parameters
        ----------
        plugin_id : str
            The ID of the Provider that we want.

        Returns
        -------
        Provider
            The Provider with the specified plugin_id.

        Raises
        ------
        PypefitterPluginNotFoundError
            If no provider with the specified ID exists.
        """
        return PluginManager.get_plugin(cls.get_entry_point(), plugin_id)
