var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');


module.exports = {
  context: __dirname,
  name:'js',
  entry: ['./assets/js/index', './assets/sass/file.scss'], // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
  devtool: 'source-map',
  output: {
      path: path.resolve('./static/assets/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
      new ExtractTextPlugin("./main.css")
  ],

  module: {
    loaders: [

      { test: /\.js?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
      { test: /\.scss$/, loader: ExtractTextPlugin.extract("style", "css!sass")},
        { test: /\.(png|woff|woff2|eot|ttf|svg)$/, loader: 'url-loader?limit=100000' }
    ],
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}