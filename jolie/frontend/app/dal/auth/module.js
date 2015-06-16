'use strict';

var angular = require("angular");

var authModule = angular.module
(
    "app.dal.auth", 
    [
        require('../rest/module')
    ]
);

require('./service');
require('./interceptor');

authModule.config
(
    [
        "$httpProvider",
        function($httpProvider)
        {
            $httpProvider.interceptors.push("auth.interceptor");
        }
    ]
);

module.exports = authModule.name;
