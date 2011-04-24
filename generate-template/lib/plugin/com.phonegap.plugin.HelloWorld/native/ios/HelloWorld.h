//
//  HelloWorld.h
//  PhoneGapVanilla
//
//  Created by Brian LeRoux on 11-04-21.
//  Copyright 2011 Nitobi Software. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "PhoneGapCommand.h"


@interface HelloWorld : PhoneGapCommand {
    NSString* win;
    NSString* fail;
}

- (void) hello:(NSMutableArray*)arguments withDict:(NSMutableDictionary*)options;


@end
