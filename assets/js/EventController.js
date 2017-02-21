/**
 * Created by STO-SD003 on 2017-01-23.
 */

const WatchController = {
    init: function () {
        const $ = jQuery;
        $("#toggleCalendar").on("click", function(){
            $("#event-calendar").slideToggle( "slow", function() {
    // Animation complete.
                if($("#event-calendar").is(":hidden"))
{
    $("#toggleCalendar").text("Show Calendar");
}else{
                    $("#toggleCalendar").text("Hide Calendar")
                }
  });
        })
    },

};


module.exports = WatchController;