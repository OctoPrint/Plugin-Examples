# coding=utf-8

def rewrite_m107(comm, cmd, cmd_type=None, send_checksum=None):
	gcode = comm.gcode_command_for_cmd(cmd)
	if not gcode or not gcode == "M107":
		return cmd

	return "M106 S0"

__plugin_name__ = "Rewrite M107"
__plugin_hooks__ = {"octoprint.comm.protocol.gcode": rewrite_m107}
