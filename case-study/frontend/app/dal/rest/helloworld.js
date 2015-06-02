'use strict';

var angular = require("angular");
var restApiModule = angular.module("app.dal.rest");

restApiModule.factory
(
    "rest.helloworld",
    [
        "rest.http",
        "$rootScope",
        function(http, $rootScope)
        {
            var users = {};

            users.get = function(x, y)
            {
                return http
                (
                    {
                        url: $rootScope.config.rest_url + "/helloworld", 
                        method: 'GET',
                        params: {x:x, y:y}
                    }
                );
            };
            
            return users;
        }
    ]
);
