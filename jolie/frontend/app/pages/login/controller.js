'use strict';

var angular = require("angular");
var loginModule = angular.module("app.pages.login");

loginModule.controller
(
    "login.ctr",
    [
        "$scope",
        "auth",
        function($scope, auth)
        {
            function is_valid_form(form)
            {
                if(form === undefined || !('email' in form) || !('password' in form) || form.email === undefined || form.password === undefined)
                {
                    return false;
                } 
                return true;
            }

            $scope.sign_in = function(form)
            {
                if(!is_valid_form(form))
                {
                    return;
                }       

                function success(data)
                {
                    $scope.state.go('main.receipts');
                };

                function error(data)
                {
                };
                auth.sign_in(form.email, form.password).then(success, error);
            };

            $scope.sign_up = function(form)
            {
                if(!is_valid_form(form))
                {
                    return;
                }

                function success(data)
                {
                    $scope.sign_in(form);
                };

                function error(data)
                {
                };
                auth.sign_up(form.email, form.password).then(success, error);
            };
        }
    ]
);
