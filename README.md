OctoPrint Plugin Examples
=========================

This repository collects the sources of examples for writing plugins for [OctoPrint](http://octoprint.org).

Currently the following examplatory plugins can be found here:

  * **custom_action_command**: Single file plugin (place it in ``~/.octoprint/plugins``) that shows how to utilize the
    [octoprint.comm.protocol.action hook](http://docs.octoprint.org/en/devel/plugins/hooks.html#octoprint-comm-protocol-action)
    and how to register hook handlers that are part of a mixin implementation. The plugin will listen for 
    firmware messages of the form ``// action:custom`` and if received will log that it received the "custom" action
    from the firmware.
  * **helloworld**: A simple plugin that injects itself into various places in OctoPrint's web interface to display
    "Hello World". Shows the basic structure of a plugin, how plugins can execute code at startup, inject themselves into
    the interface and how they can control when their content is shown based on internal state of the UI such as login
    information.
  * **message_on_connect**: Single file plugin (place it in ``~/.octoprint/plugins``) that shows how to utilize the
    [octoprint.comm.protocol.scripts hook](http://docs.octoprint.org/en/devel/plugins/hooks.html#octoprint-comm-protocol-scripts)
    by adding an ``M117 OctoPrint connected`` to the GCODE script sent to the printer after OctoPrint connected to
    it.
  * **rewrite_m107**: Single file plugin (place it in ``~/.octoprint/plugins``) that shows how to utilize the
    [octoprint.comm.protocol.gcode hook](http://docs.octoprint.org/en/devel/plugins/hooks.html#octoprint-comm-protocol-gcode)
    by swapping the (deprecated) ``M107`` command with the equivalent ``M106 S0``.
  * **strip_all_comments**: Single file plugin (place it in ``~/.octoprint/plugins``) that shows how to utilize the
    [octoprint.filemanager.preprocessor hook](http://docs.octoprint.org/en/devel/plugins/hooks.html#octoprint-filemanager-preprocessor)
    by removing the comments (and empty lines) from all uploaded/generated GCODE files ending on the name postfix "_strip".

Further Links
-------------

  * [OctoPrint](http://octoprint.org)
  * [OctoPrint Source Repository](http://github.com/foosel/OctoPrint)
  * [OctoPrint Plugin Documentation](http://docs.octoprint.org/en/devel/plugins/index.html)