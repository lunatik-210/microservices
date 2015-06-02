'use strict';

var angular = require("angular");
var store = require("store");
var authModule = angular.module("app.dal.rest");


authModule.factory
(
    "rest.http",
    [
        "$http",
        "$base64",
        "$q",
        function($http, $base64, $q)
        {
            var on_success = function(response)
            {
                var deffered = $q.defer();
                if(response.data.error.code == 0)
                {
                    deffered.resolve(response.data.result);
                } 
                else
                {
                    deffered.reject(response.data.error);
                }
                return deffered.promise;
            };

            var http = function(config)
            {
                if(!('headers' in config))
                {
                    angular.extend(config, {headers: {}});
                }

                var token = store.get("auth_token");
                if(token!== null)
                {
                    config.headers['Authorization'] = 'Basic ' + $base64.encode(token + ':');
                }

                //config.headers['Content-Type'] = 'application/json; charset=utf-8';

                return $http(config).then(on_success);
            };
            return http;
        }
    ]
);
