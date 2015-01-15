$(function() {
    function HelloWorldViewModel(parameters) {
        var self = this;

        self.loginState = parameters[0];

        self.someValue = ko.observable("active");
    }

    // view model class, parameters for constructor, container to bind to
    ADDITIONAL_VIEWMODELS.push([HelloWorldViewModel, ["loginStateViewModel"], [
        document.getElementById("tab_plugin_helloworld"),
        document.getElementById("tab_plugin_helloworld_link"),
        document.getElementById("navbar_plugin_helloworld"),
        document.getElementById("sidebar_plugin_helloworld_wrapper")
    ]]);
});
