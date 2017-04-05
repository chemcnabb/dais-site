/**
 * Created by STO-SD003 on 2017-01-23.
 */

var WatchController = {
    init: function () {

    },
    initVideo: function(videoId){
        Utilities.videoClick(videoId);
    },
    initYoutube: function(embed){
        Utilities.youtubeClick(embed);
    }
};


module.exports = WatchController;