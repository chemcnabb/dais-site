/**
 * Created by STO-SD003 on 2017-01-23.
 */
function sendDaisMail(){
    let subject = escape("Contact Us");
    let name = escape(jQuery("#name").val());
    let email = jQuery("#email").val();
    let body = escape(jQuery("#comment").val());
    window.open('mailto:info@dais.ca?subject='+subject+'&body=NAME:' + name + '\nEmail:'+email+'\n' + body);
}
const HomeController = {
    init: function () {
        let collection = ["watch", "look", "listen"];

        let count = 0;
        jQuery(".post-list-display").children().each(function () {
            count++;
            if (count === 4) {
                count = 1;
            }
            if (count === 1) {
                jQuery(this).find(".viewport").addClass("full");
            } else if ((count === 2 || count === 3) && !jQuery(this).is(':last-child')) {
                jQuery(this).find(".viewport").removeClass("full");
                jQuery(this).find(".viewport").addClass("half");
            } else if ((count === 3) && jQuery(this).is(':last-child')) {
                jQuery(this).find(".viewport").removeClass("full");
                jQuery(this).find(".viewport").addClass("half");
            } else if ((count === 2) && jQuery(this).is(':last-child')) {
                jQuery(this).find(".viewport").addClass("full");
                jQuery(this).find(".viewport").removeClass("half");
            }
        });

        jQuery(".home a.filter-buttons").on("click", function (e) {
            let button = this;


            jQuery.each(collection, function (index, value) {
                jQuery(`.${value}`).hide(800);
            });

            jQuery.each(collection, function (index, value) {

                if (value === button.id) {
                    jQuery(`.${value}`).addClass("will-show");
                }

            });
            let count = 0;
            jQuery(".post-list-display ").children("li.will-show").each(function () {

                count++;

                if (count === 4) {
                    count = 1;
                }
                if (count === 1) {
                    jQuery(this).find(".viewport").addClass("full");
                    jQuery(this).find(".viewport").removeClass("half");
                } else if ((count === 2 || count === 3) && (jQuery(".post-list-display ").children("li.will-show").length > 1)) {
                    jQuery(this).find(".viewport").addClass("half");
                    jQuery(this).find(".viewport").removeClass("full");
                } else if ((count === 2 || count === 3) && (jQuery(".post-list-display ").children("li.will-show").length === 1)) {
                    jQuery(this).find(".viewport").addClass("full");
                    jQuery(this).find(".viewport").removeClass("half");
                }
                jQuery(this).removeClass("will-show");

            });


            jQuery.each(collection, function (index, value) {
                if (value === button.id) {

                    jQuery(`.${value}`).show(800);
                }

            });

        });

        jQuery(".home .content").hover(function () {
            let re = /(?:\.([^.]+))?$/;
            let $img = jQuery(this).find(".watch-logo-container img");
            let fileArr = $img.attr("src").split(".");
            let fname = fileArr[0];
            let ext = fileArr[1];
            $img.attr("src", fname + "-white." + ext);

        }, function () {
            let re = /(?:\.([^.]+))?$/;
            let $img = jQuery(this).find(".watch-logo-container img");
            let fileArr = $img.attr("src").split("-white.");
            let fname = fileArr[0];
            let ext = fileArr[1];
            $img.attr("src", fname + "." + ext);

        });


        jQuery(".home .viewport, .home .viewport-half").hover(function () {
            jQuery(this).animate({boxShadow: "inset 0 0 0 1000px rgba(255, 255, 255, 0)"}, 1000);
        }, function () {
            jQuery(this).animate({boxShadow: "inset 0 0 0 1000px rgba(255, 255, 255, .5)"}, 1000);
        });

    },
};

module.exports = HomeController.init();