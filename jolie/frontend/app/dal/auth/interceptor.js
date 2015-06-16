'use strict';

var angular = require("angular");
var authModule = angular.module("app.dal.auth");

authModule.factory
(
    "auth.interceptor",
    [
        "$q",
        "$rootScope",
        "$base64",
        function($q, $rootScope, $base64)
        {
            function onResponseError(response)
            {
                if(response.status === 401)
                {
                    console.log('404 ERROR LOG OUT');
                    $rootScope.$broadcast("auth.UnauthorizedRequest");
                    $rootScope.state.go("login");
                }
                return $q.reject(response);
            }
            
            return {
                'responseError': onResponseError
            };
        }
    ]
);
