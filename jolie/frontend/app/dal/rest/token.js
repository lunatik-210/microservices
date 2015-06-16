'use strict';

var angular = require("angular");
var restApiModule = angular.module("app.dal.rest");

restApiModule.factory
(
    "rest.token",
    [
        "$http",
        "$rootScope",
        "$base64",
        function($http, $rootScope, $base64)
        {
            //////////////////////////////////////////////////////////////
            ////////////////////// THIS
            var api = {};

            // get token for user
            api.get = function(email, password)
            {
                return $http({
                    method: 'GET',
                    url: $rootScope.config.rest_url + "/token",
                    headers: 
                    {
                        'Authorization': 'Basic ' + $base64.encode(email + ':' + password)
                    }
                });
            };

            return api;
        }
    ]
);
