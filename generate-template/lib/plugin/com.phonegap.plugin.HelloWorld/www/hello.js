var hello = function(name, win, fail) {
   PhoneGap.exec(win, fail, "HelloWorld", "hello", [name]);
}

// this is only for Android..for now
PhoneGap.addConstructor(function() {
   navigator.app.addService('HelloWorld','com.phonegap.plugin.HelloWorld');
})