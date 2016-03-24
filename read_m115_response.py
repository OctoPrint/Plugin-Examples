# coding=utf-8

import logging

def detect_machine_type(comm, line, *args, **kwargs):
	if "MACHINE_TYPE" not in line:
		return line

	# Create a dict with all the keys/values returned by the M115 request
	printer_data = dict(d.split(':') for d in line.split(' '))
	
	logging.getLogger("octoprint.plugin." + __name__).info("Machine type detected: {machine}.".format(machine=printer_data["MACHINE_TYPE"]))

	return line

__plugin_name__ = "Detect Machine Data"
__plugin_hooks__ = {
	"octoprint.comm.protocol.gcode.received": detect_machine_type
}
