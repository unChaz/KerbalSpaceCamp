var httpProxy = require('http-proxy');
var config = require('./config');

httpProxy.createProxyServer({target: config.server.host + ':' + config.server.port}).listen(config.port);
