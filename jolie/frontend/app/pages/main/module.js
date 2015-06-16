'use strict';

var angular = require("angular"); 

var mainModule = angular.module
(
    "app.pages.main", 
    [
        require('angularUIRouter'),
        require('../../dal/rest/module.js')
    ]
);

require('./controller');

mainModule.config
(
    [
        "$stateProvider",
        "$urlRouterProvider",
        function($stateProvider, $urlRouterProvider)
        {
            $stateProvider
            .state
            (
                "main",
                {
                    url: "/main",
                    templateUrl: "pages/main/index.html",
                    controller: "main.ctr",
                    resolve:
                    {
                        sum:
                        [
                            "$http",
                            function($http)
                            {
                                return $http.get('http://127.0.0.1:5000/sum?x=2&y=3');
                            }
                        ]
                    }
                }
            )
        }
    ]
);

module.exports = mainModule.name;
