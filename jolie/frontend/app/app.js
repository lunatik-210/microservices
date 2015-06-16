'use strict';

var angular = require('angular');

var app = angular.module
(
    'AppModule', 
    [
        require('angularUIRouter'),
        require('./pages/login/module'),
        require('./pages/main/module')
    ]
)

require('./config');

app.config
(
    [
        "$urlRouterProvider",
        function($urlRouterProvider)
        {
            $urlRouterProvider.otherwise("/login");
        }
    ]
);

app.controller
(
    "AppCtr",
    [
        "$rootScope",
        "$state",
        "env",
        "endpoints",
        function($rootScope, $state, env, endpoints)
        {
            function form_rest_url(env, endpoints)
            {
                var rest_url = env.host;
                if(env.port != undefined && env.port != "")
                {
                    rest_url += ':' + env.port;
                }
                rest_url += '/' + endpoints.rest;
                return rest_url;
            }

            $rootScope.state = $state;

            $rootScope.config = 
            { 
                rest_url: form_rest_url(env, endpoints)
            };
        }
    ]
);

module.exports = app;
