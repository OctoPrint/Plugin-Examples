# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class DummyMobileUiPlugin(octoprint.plugin.UiPlugin,
                          octoprint.plugin.TemplatePlugin):

	def will_handle_ui(self, request):
		return request.user_agent and request.user_agent.platform in ("android", "ipad", "iphone")

	def on_ui_render(self, now, request, render_kwargs):
		from flask import make_response, render_template
		return make_response(render_template("dummy_mobile_ui_index.jinja2", **render_kwargs))

__plugin_name__ = "Dummy Mobile UI"
__plugin_implementation__ = DummyMobileUiPlugin()