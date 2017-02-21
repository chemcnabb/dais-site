/**
 * Created by STO-SD003 on 2017-01-23.
 */

const HomeController = {
    init: function () {
        let collection = ["watch", "look", "listen"];
        jQuery(".filter-buttons").on("click", function(e){
            let button = e.target;
            jQuery.each(collection, function(index, value){

                if(value != button.id){
                    jQuery("." + value).hide(1000);
                }else{
                    jQuery("." + value).show(1000);
                }
            });

        });
        jQuery(".viewport, .viewport-half").hover(function() {
      jQuery(this).animate({ boxShadow: "inset 0 0 0 1000px rgba(255, 255, 255, 0)" }, 1000);
    },function() {
      jQuery(this).animate({ boxShadow: "inset 0 0 0 1000px rgba(255, 255, 255, .5)" }, 1000);
    });

    },
};

module.exports = HomeController.init();