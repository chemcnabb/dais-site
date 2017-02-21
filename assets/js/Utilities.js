/**
 * Created by STO-SD003 on 2017-01-23.
 */
var $ = global.jQuery;
var Utilities = {
    init: function () {
        $(document).ready(function() {

            });


    },

    videoClick: function(videoId){
        $('.vimeo-img').click(function (event) {

          var $this = $(this),
              $parent = $this.parent();
console.log($parent);
          $this.remove();

          $parent.append('<iframe class="col-md-12 viewport" src="https://player.vimeo.com/video/' + videoId + '?color=ffffff&title=0&byline=0&portrait=0&autoplay=1" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>');
        });
    }
};


module.exports = Utilities;