# coding=utf-8

import octoprint.plugin
import octoprint.filemanager
import octoprint.filemanager.util

from octoprint.util.comm import strip_comment

class CommentStripper(octoprint.filemanager.util.LineProcessorStream):
	def process_line(self, line):
		line = strip_comment(line).strip()
		if not len(line):
			return None
		return line + "\r\n"

def strip_all_comments(path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
	if not octoprint.filemanager.valid_file_type(path, type="gcode"):
		return file_object

	import os
	name, _ = os.path.splitext(file_object.filename)
	if not name.endswith("_strip"):
		return file_object

	return octoprint.filemanager.util.StreamWrapper(file_object.filename, CommentStripper(file_object.stream()))

__plugin_name__ = "Strip comments from GCODE"
__plugin_description__ = "Strips all comments and empty lines from uploaded/generated GCODE files ending on the name " \
                         "postfix \"_strip\", e.g. \"some_file_strip.gcode\"."
__plugin_hooks__ = {
	"octoprint.filemanager.preprocessor": strip_all_comments
}
