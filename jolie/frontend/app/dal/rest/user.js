'use strict';

var angular = require("angular");
var restApiModule = angular.module("app.dal.rest");

restApiModule.factory
(
    "rest.users",
    [
        "rest.http",
        "$rootScope",
        function(http, $rootScope)
        {
            var users = {};

            users.get = function()
            {
                return http
                (
                    {
                        url: $rootScope.config.rest_url + "/users", 
                        method: 'GET'
                    }
                );
            };

            users.post = function(params)
            {
                return http
                (
                    {
                        url: $rootScope.config.rest_url + "/users", 
                        method: 'POST',
                        data: params
                    }
                );
            };
            
            return users;
        }
    ]
);
