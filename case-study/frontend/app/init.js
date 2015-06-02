'use strict';

var angular = require('angular');
var app = require('./app.js');

require('./vendors/js/ready.min.js')
(
    function()
    {
        angular.bootstrap(document, [app.name]);
    }
);
