import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
	def get_template_vars(self):
		return dict(
			_settings=dict(name="Hello World", custom_bindings=True),
			_tab=dict(name="Hello World", styles=["display: none"], custom_bindings=True, data_bind="allowBindings: true, visible: loginState.isUser()"),
			_sidebar=dict(name="Hello World", styles_wrapper=["display: none"], custom_bindings=True, data_bind="allowBindings: true, visible: loginState.isUser()", icon="gear"),
			_navbar=dict(styles=["display: none"], custom_bindings=True, data_bind="allowBindings: true, visible: loginState.isUser()")
		)

	def get_assets(self):
		return dict(
			js=["js/helloworld.js"]
		)

__plugin_name__ = "Hello World"
__plugin_version__ = "1.0"
__plugin_implementations__ = [HelloWorldPlugin()]