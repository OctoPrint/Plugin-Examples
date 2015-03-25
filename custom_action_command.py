# coding=utf-8

import octoprint.plugin

class CustomActionCommandPlugin(octoprint.plugin.OctoPrintPlugin):

	def custom_action_handler(self, comm, line, action):
		if not action == "custom":
			return

		self._logger.info("Received \"custom\" action from printer")

__plugin_name__ = "Custom action command"
__plugin_implementations__ = []
__plugin_hooks__ = dict()

def __plugin_init__():
	plugin = CustomActionCommandPlugin()

	global __plugin_implementations__
	__plugin_implementations__ = [plugin]

	global __plugin_hooks__
	__plugin_hooks__ = {"octoprint.comm.protocol.action": plugin.custom_action_handler}