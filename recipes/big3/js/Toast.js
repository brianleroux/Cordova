/**
 * @author Anthony Lukasavage
 */
var toastTimeout;
	        
function showToast(o) {
	o = typeof o == 'string' ? {message:o} : o;     
    	var duration = o.duration || 3000;
    	var fadein = o.fadein || 500;
    	var fadeout = o.fadeout || fadein/2;
    	var message = o.message || '';
    	var top = o.top;
    
    clearToast();
    	
    // create new toast
    x$('body').top('<div id="toast">' + message + '</div>');
    var toast = x$('#toast');
    if (top) {
	    toast.setStyle('top', top);
    }
    toast.on('touchstart', clearToast);
    toast.tween({opacity:'1', duration:fadein});
    
    // set timeout for it to disappear
    toastTimeout = setTimeout(
	    	function() {
	        	toast.tween({opacity:'0', duration:fadeout}, clearToast);
	    }, 
	    duration + fadein
	);
}

function clearToast() {
	clearTimeout(toastTimeout);
    x$('#toast').html('remove');
}
