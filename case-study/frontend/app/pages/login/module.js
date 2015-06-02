'use strict';

var angular = require("angular"); 

var loginModule = angular.module
(
    "app.pages.login", 
    [
        require('angularUIRouter'),
        require("../../dal/auth/module.js")
    ]
);

require("./controller");

loginModule.config
(
    [
        "$stateProvider",
        function($stateProvider)
        {
            $stateProvider
            .state
            (
                "login",
                {
                    url: "/login",
                    templateUrl: "pages/login/index.html",
                    controller: "login.ctr"
                }
            );
        }
    ]
);

module.exports = loginModule.name;
