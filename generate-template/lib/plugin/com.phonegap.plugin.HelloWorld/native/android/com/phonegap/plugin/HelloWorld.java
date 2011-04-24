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
