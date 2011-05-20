document.addEventListener('deviceready', function(){

    var q = function(id) { return document.getElementById(id) } 
    
    function win (a) {
        var x = q('x')
        ,   y = q('y')
        ,   z = q('z')

        x.innerHTML = 'x value is ' + ~~a.x
        y.innerHTML = 'y value is ' + ~~a.y
        z.innerHTML = 'z value is ' + ~~a.z
    
        var horizontal = a.x
        ,   vertical   = a.y
        ,   shadow     = horizontal + 'px ' + vertical + 'px 10px #888'

        x.style['-webkit-box-shadow'] = shadow
        y.style['-webkit-box-shadow'] = shadow
        z.style['-webkit-box-shadow'] = shadow
    }

    function fail () {
        console.log('acceleration fail callback fired!')
    }

    navigator.accelerometer.watchAcceleration(win, fail, {frequency:50})

}, true);
