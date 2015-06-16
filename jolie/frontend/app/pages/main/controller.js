'use strict';

var angular = require("angular"); 
var mainModule = angular.module("app.pages.main");

var ctr = function($scope, sum)
{
    $scope.sum = sum;
}

mainModule.controller
(
    "main.ctr", 
    [
        "$scope",
        "sum",
        ctr
    ] 
);
