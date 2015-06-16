'use strict';

var angular = require("angular"); 
require("base64");

var restApiModule = angular.module
(
    "app.dal.rest", 
    [
        "base64"
    ]
);

require("./http");
require("./token");
require("./user");

module.exports = restApiModule.name;