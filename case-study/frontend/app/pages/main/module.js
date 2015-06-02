'use strict';

var angular = require("angular"); 

var mainModule = angular.module
(
    "app.pages.main", 
    [
        require('angularUIRouter'),
        require('../../dal/rest/module.js'),
        require("../../dal/auth/module.js")
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
                            "rest.helloworld",
                            function(rest_helloworld)
                            {
                                return rest_helloworld.get(2, 3);
                            }
                        ]
                    }
                }
            )
        }
    ]
);

module.exports = mainModule.name;
