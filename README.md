Cordova
===

A PhoneGap project toolchain that automates common tasks for building cross platform mobile projects with OS X. This is mobile project automation for common development workflow tasks such as: compiling, debugging, testing, releasing and other things in between. As an added benefit projects generated with Cordova create a consistent, predictable, easy to understand and therefor extend software project. A number of conventions are introduced removing the need for mobile developers to relearn their tools or, worse, rebuild them for every project. 

Currently Supported Platforms
---

- iOS
- Android
- webOS

Justification
---

Mobile development requires proprietary SDKs. The SDKs supported by this tool currently work well with OS X. If you are doing PhoneGap development on a Windows based machine for BlackBerry, Bada or Windows Phone 7 then a different tool chain is required (or, perhaps with contribution, this one will grow to accommodate other operating systems). 

Requirements
---

    ios sdk ........ http://developer.apple.com 
    android sdk .... http://developer.android.com
    palm sdk ....... http://developer.palm.com
	ios-sim ........ https://github.com/Fingertips/ios-sim
	phonegap/ios ... http://phonegap.com/download <-----------( run phonegap/ios/PhoneGapLibInstaller.pkg 

Installation
---

1. Make sure you have an Android AVD named `default`.
2. Add the following line to `~/.bashrc` or `~/.bash_profile`:
	
	export PATH=PATH:/path/to/cordova

Usage
---

Generate a new PhoneGap project by running:
	
	phonegap PROJECTNAME --www [www recipe] --test [test recipe]
    

For further usage info try:

	phonegap -h

Generated Project Structure
---

Your generated project will look like this:

	/AppName ...... Project name; not programatically meaningful.
	|-bin/ ........ Cordova scripts (DO NOT MODIFY).
	|-doc/ ........ Project documentation.
	|-lib/ ........ Place for *your* scripts/utils.
	|-test/ ....... Place for *your* app tests.
	|-tmp/ ........ Native app src. (GENERATED! Leave out of src control.)
	|-www/ ........ Place for *your* app files.
	`-Makefile	... Useful examples of commands. Yours to modify too.
	
From here try running `make` to see what sort of useful commands you have available to you. Each of these `Makefile` commands are packaged for each platform in the `./bin` folder so, when needed, you can call scripts directly such as `./bin/debug/ios`. 

Other important notes about the generated project:

- The `./lib` folder is your place for custom automations. _Protip: make everything relative to the root of your project._
- The generated `Makefile` is intended as an example only. 
- Place unit tests in `./test` and copy in applicable js from `./www`. This is the point of build automation!
- Put your app code, logic and assets in `./www`.
- The `./tmp` directory is full of *toxic proprietary build sludge*. Interaction with it should limited as possible.
- Do read `./bin` scripts but only modify at risk of not getting future updates! Instead add your own to `./lib`.

A future release of Cordova will allow easy upgrading by simply overwriting `./bin` and leave an example `Makefile` if none is present. Happily modify `./lib`, `./www` and `./test` to develop your app. 

Recipes
---

Recipes are little packages of web code that initialize from an `index.html` file. By default `phonegap` will create a project with a bare bones (vanilla) `www/index.html` and qunit starter project in the `test/index.html` directory. In the future recipes will be added for all the major mobile dom frameworks like XUI, Sencha Touch and jQuery Mobile. If you'd like to see them sooner, have a look at `ROADMAP.md` and consider contributing!

Generated MakeFile Commands
---

	create .... writes out native code to ./tmp directory based on config.xml
	debug ..... copies www, compiles native src, installs and launches
	web ....... serve www at http://localhost:8000
	weinre .... launch weinre at http://localhost:8080
	test ...... compiles ./test into native
	log ....... launches logger
	release ... this is for you to implement!
	emulate ... launch platform emulators
