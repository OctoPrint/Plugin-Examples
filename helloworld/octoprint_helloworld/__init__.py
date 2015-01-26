import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.StartupPlugin):

	def on_after_startup(self):
		# "_logger" gets injected into every plugin implementation and can be used to directly log to OctoPrint's log
		# file
		self._logger.info("Hello World!")

	def get_template_configs(self):
		return [
		    # Since our plugin contains two settings components, we have to make sure to also add an entry here for the
		    # default one. Otherwise OctoPrint will assume that the definition of the second component overrides the
		    # default one and won't include that at all. A simple entry only containing the "type" attribute is enough
		    # to achieve this, since the rest of our first settings component will just stick to the default configuration:
		    # template will be helloworld_settings.jinja2, name will be taken from the plugin's __plugin_name__, custom
		    # bindings will be active, etc
		    dict(type="settings"),

		    # This adds a second settings pane from helloworld_settings2.jinja2 with a different name than the plugin's
		    dict(type="settings", template="helloworld_settings2.jinja2", name="Hello World the second"),

		    # We want to display our tab, sidebar and navbar component only when the user is logged in, and we want to
		    # make sure they are not even visible when the page first loads, until the login state has been determined.
		    #
		    # To make the components depend on the login state, we have that injected in our custom view model[1] and
		    # define our components' data binding to set the "visible" property based on "loginState.isUser".
		    #
		    # To make sure the components are invisible at first, we add a custom css declaration to them setting
		    # "display: none". Notice how for the tab and the navbar component, the "styles" attribute is used for this,
		    # whereas for the sidebar component the "styles_wrapper" attribute is used. The reason is that for the tab
		    # we also want the link in the tab bar to be invisible ("styles" gets applied to both the link and the
		    # actual content pane), navbar only defines "styles" (since it only consists of one element, the content
		    # itself) and for the sidebar component our data binding only gets applied to the whole wrapper, so we
		    # want our custom style only there too so that the data-binding will remove it again when necessary.
		    #
		    # [1] see helloworld.js in ../static/js
			dict(type="tab", styles=["display: none"], data_bind="visible: loginState.isUser()"),
			dict(type="sidebar", icon="gear", styles_wrapper=["display: none"], data_bind="visible: loginState.isUser()"),
			dict(type="navbar", styles=["display: none"], data_bind="visible: loginState.isUser()")
		]

	def get_assets(self):
		return dict(
			# We only have one custom js file to include into the page, which is our custom view model
			js=["js/helloworld.js"]
		)

__plugin_name__ = "Hello World"
__plugin_implementations__ = [HelloWorldPlugin()]