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
      jQuery(".title, .subtitle").animate({ color: "#fff" }, 1000);
    },function() {
      jQuery(".title, .subtitle").animate({ color: "#000" }, 1000);
    });

    },
};

module.exports = HomeController.init();