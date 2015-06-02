'use strict';

var angular = require("angular"); 
var mainModule = angular.module("app.pages.main");

var ctr = function($scope, sum, auth, rest_helloworld)
{
    $scope.sum = sum;

    $scope.result = undefined;

    $scope.sign_out = function()
    {
        auth.sign_out();
        $scope.state.go('login');
    };

    $scope.submit = function(x, y)
    {
        rest_helloworld.get(x, y).then(function(sum)
        {
            $scope.result = {x:x, y:y, sum: sum};
        },
        function()
        {
            $scope.result = undefined;
        });
    }
}

mainModule.controller
(
    "main.ctr", 
    [
        "$scope",
        "sum",
        "auth",
        "rest.helloworld",
        ctr
    ] 
);
