PhoneGap Plugins
===

In this guide we're going to work through the creation of a basic plugin
for PhoneGap.

Plugin Packaging
---

Plugins require consistent packaging. By adhering to these conventions
your plugins will be easily discoverable and installable in any PhoneGap
based project.

As you can see below, plugins consist of two distinct portions of code:
native code and the JavaScript interface you wish to expose to the
PhoneGap webview. The native code is different for each platform your
plugin will support and it is perfectly acceptable to have a plugin that
only supports a single platform. The JavaScript interface wraps the
native bridge calls that can be specific for each platform. The end user
of your plugin does not need to know these ugly details.

    /
    |-native ............. native implemetation code goes here
    | |-ios 
    | |-android
    | |-webos
    | `-blackberry
    |
    |-www
    | `-helloworld.js ... JavaScript interface code goes here
    |
    `-package.json ...... descriptor as per CommonJS package


JavaScript Interface
===

PhoneGap Plugins utilize the consistent bridging interface defined by PhoneGap. All
calls should be made with an async style signature like so:

	methodName(successCallback, failureCallback, nativeClassName, nativeClassMethodName, argumentsArray);

With this in mind, we want to construct our HelloWorld plugin with a signature like so:

    hello('brian', function(s) {
        console.log(s)
    });

Of course, since a good PhoneGap Plugin implements error callbacks this
could be rewritten as:

    hello('brian', console.log, console.log);

So, lets implement it:

	navigator.hello = function(name, win, fail) {
    	PhoneGap.exec(win, fail, "HelloWorld", "hello", [name]);
	}
  
Not so bad. Now lets write the native binding code.

iOS Native Implementation
---

We're going to start out with implementing the iOS native code. Its
pretty straightforward. If you are unfamiliar with Objective C, this is 
not the tutorial you're looking for. 

First we implement the interface. Our class will have a single method appropriately 
named `hello`:

	// HelloWorld.h
	#import <Foundation/Foundation.h>
	#import "PhoneGapCommand.h"


	@interface HelloWorld : PhoneGapCommand {
	}

	- (void) hello:(NSMutableArray*)arguments withDict:(NSMutableDictionary*)options;
	@end
	
And then the actual implementation:
	
	// HelloWorld.m
	#import "HelloWorld.h"

	@implementation HelloWorld

	- (void)hello:(NSMutableArray*)arguments withDict:(NSMutableDictionary*)options
	{
	    NSString* callbackid = [arguments objectAtIndex:0];
	    NSString* jsString = NULL;
	    PluginResult* result = nil;

	    @try {
	        NSString* name = [arguments objectAtIndex:1];

	        result = [PluginResult resultWithStatus:PGCommandStatus_OK messageAsString:[NSString stringWithFormat:@"%@%@", @"Hello, ", name]];
	        jsString = [result toSuccessCallbackString:callbackid];
	    }
	    @catch (NSException *exception) {
	        result = [PluginResult resultWithStatus:PGCommandStatus_ERROR messageAsString:@"hello missing name!"];
	        jsString = [result toErrorCallbackString:callbackid];
	    }
	    @finally {
	       [[self webView] stringByEvaluatingJavaScriptFromString:jsString];
	    }
	}
	@end

Despite the archaic visual detritus of the Objective C language this is rather straightforward implementation. 

Android Native Implementation
---

The Android native code is found under `/native/android/com/phonegap/plugin/HelloWorld.java`.

	
	package com.phonegap.plugin;
	
	import org.json.*;
	import com.phonegap.api.Plugin;
	import com.phonegap.api.PluginResult;

	public class HelloWorld extends Plugin {
	    public PluginResult execute(String action, JSONArray args, String callinglbackId) {
	        try {
	            String name = args.getString(0);
            
	            if (name.equals("null")) {
	                throw new Exception();
	            }
	            return new PluginResult(PluginResult.Status.OK, "Hello, " + name);
	        } catch(Exception e) {
	            return new PluginResult(PluginResult.Status.INVALID_ACTION, "hello missing parameter!");
	        }
	    }
	}
	
	
When installing: place this in the root of your `src/com/phonegap/plugin/HelloWorld.java`.

Unfortunately, we currently require Android specific JavaScript that helps reflect in the Java class we want to call:

	// add this to helloworld.js
	PhoneGap.addConstructor(function() {
		navigator.app.addService('HelloWorld','com.phonegap.plugin.HelloWorld');
	})
	
	
Its interesting to note this code is not necessary in iOS because Objective C doesn't have a concept for namespaces. 
A definite candidate for some refactoring. Perhaps create a magical global area for Android like com.phonegap.plugin? 

Plugin Installation
---

Plugin native code ultimately gets copied into PhoneGap native projects; and each native platform is a special snowflake:

- iOS native code gets dropped into `plugins` group.
- Android native code goes under `src`.
- TODO blackberry, webos, etc

There is an example usage file in the root called `example.html`. Drop that code into your `www/index.html` to test.