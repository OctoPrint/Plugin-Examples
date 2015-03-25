OctoPrint Plugin Examples
=========================

This repository collects the sources of examples for writing plugins for [OctoPrint](http://octoprint.org).

Currently the following examplatory plugins can be found here:

  * **helloworld**: A simple plugin that injects itself into various places in OctoPrint's web interface to display
    "Hello World". Shows the basic structure of a plugin, how plugins can execute code at startup, inject themselves into
    the interface and how they can control when their content is shown based on internal state of the UI such as login
    information.
  * **rewrite_m107**: Single file plugin (place it in ``~/.octoprint/plugins``) that shows how to utilize the
    [octoprint.comm.protocol.gcode hook](http://docs.octoprint.org/en/devel/plugins/hooks.html#octoprint-comm-protocol-gcode)
    by swapping the (deprecated) ``M107`` command with the equivalent ``M106 S0``.

Further Links
-------------

  * [OctoPrint](http://octoprint.org)
  * [OctoPrint Source Repository](http://github.com/foosel/OctoPrint)
  * [OctoPrint Plugin Documentation](http://docs.octoprint.org/en/devel/plugins/index.html)