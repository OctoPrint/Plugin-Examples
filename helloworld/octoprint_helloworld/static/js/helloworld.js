$(function() {
    function HelloWorldViewModel(parameters) {
        var self = this;

        // We want to only display some of the components when the user is logged in, so we need the login state view
        // view model from the application
        self.loginState = parameters[0];

        // This is just some custom value that we have bound to at a couple of spans in the template files which
        // normally read "inactive"
        self.someValue = ko.observable("active");
    }

    // This is how our plugin registers itself with the application, by adding some configuration information to
    // the global variable ADDITIONAL_VIEWMODELS
    ADDITIONAL_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        HelloWorldViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request here is the order
        // in which the dependencies will be injected into your view model upon instantiation via the parameters
        // argument
        ["loginStateViewModel"],

        // Finally, this is the list of all elements we want this view model to be bound to. We see all our components
        // here that we defined in get_template_configs of our TemplatePlugin implementation, using the default IDs
        // assigned to them by OctoPrint
        [
            document.getElementById("tab_plugin_helloworld"),
            document.getElementById("tab_plugin_helloworld_link"),
            document.getElementById("navbar_plugin_helloworld"),
            document.getElementById("sidebar_plugin_helloworld_wrapper"),
            document.getElementById("settings_plugin_helloworld"),
            document.getElementById("settings_plugin_helloworld_2")
        ]
    ]);
});
