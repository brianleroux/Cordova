document.addEventListener('deviceready', function(){

    var q = function(id) { return document.getElementById(id) } 
    
    function win (a) {
        q('x').innerHTML = ~~a.x
        q('y').innerHTML = ~~a.y
        q('z').innerHTML = ~~a.z
    }

    function fail () {
        console.log('acceleration fail callback fired!')
    }

    navigator.accelerometer.watchAcceleration(win, fail, {frequency:50})

}, true);
