x$(document).on('deviceready', function() {

    var w = window.screen.width + 'px'
    ,   h = window.screen.height + 'px'

    // lets make our cards fix to the width of the screen they are being displayed on 
    var freezeCardSize = (function() {
        x$('.card').each(function(e) {
            //x$(e).css({ width:w, height:h });
        });
    })();

    // link touch navigates to corosponding card
    var hijackLinks = (function() {
        x$('a').touchstart(function(a) {
            var activeCard = x$('#' + this.href.split('#')[1]);
            // move the card to the top right
            // make it visible
            // animate to that card
            x$('#deck').tween({'left':'-' + w, 'duration':3 });
            
        });
    })();

});
