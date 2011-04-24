//
//  HelloWorld.m
//  PhoneGapVanilla
//
//  Created by Brian LeRoux on 11-04-21.
//  Copyright 2011 Nitobi Software. All rights reserved.
//

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
