'use strict';

var angular = require("angular"); 
var store = require("store");
var authModule = angular.module("app.dal.auth");

authModule.factory
(
    "auth",
    [
        "rest.token",
        "rest.users",
        "$q",
        function(token, users, $q)
        {
            var service = {};

            service.isAuthorized = function()
            {
                return (service.token() !== null);
            };

            service.sign_in = function(email, password)
            {
                var token_success = function(response)
                {
                    var deffered = $q.defer();

                    if(response.status == 201 && response.data.error.code == 0)
                    {
                        store.set('auth_token', response.data.result.token);
                        store.set('user', response.data.result.user);
                        deffered.resolve(response.data.result);
                    } 
                    else
                    {
                        deffered.reject(response.data.error);
                    }
                    return deffered.promise;
                };

                return token.get(email, password).then(token_success);
            };

            service.sign_out = function()
            {
                store.remove('auth_token');
                store.remove('user');
            };

            service.sign_up = function(email, password)
            {
                return users.post({email:email, password:password});
            };

            function safe_store_get(key)
            {
                if(store.has(key))
                    return store.get(key);
                return null;                
            };

            service.token = function()
            {
                return safe_store_get('auth_token');
            };

            service.current_user = function()
            {
                return safe_store_get('user');
            };

            return service;
        }
    ]
);
