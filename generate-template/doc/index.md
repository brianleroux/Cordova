Cordova Automation Scripts
===

A toolchain is a set of automations for common, tedious and likely error prone tasks for software development. The PhoneGap project has helped ease the pain of building apps but building with PhoneGap itself can be tedious. Despite providing a common abstraction the PhoneGap source itself is exacerbated by a proliferation of proprietary mobile operating systems and sdks.

__Cordova is a PhoneGap toolchain for OS X.__

- unified nomenclature for common tasks
- removes tooling ambiguity 
- everything you need to iteratively develop installable web apps 

Scripts are presented in consistent, readable and easily communicable style with everything provided by Cordova in the `./bin` directory. Have a browse around in there to get a sense of what you can do. 

These conventions make it trivially easy for new developers to work with a Cordova based project and, more importantly, to _extend with your own automations_. A `Makefile` also gets generated to further simplify common tasks. 

Launch Emulators
---

Most platforms have an emulation capability which is useful for testing.
You can launch the emulators using these commands.

	./bin/emulate/ios
	./bin/emulate/android

Native Project Generation
---

These scripts will generate a new native project in `./tmp` using
`./www/config.xml` for project name (and other metadata).

	./bin/create/ios
	./bin/create/android

Debugging 
---

These scripts will copy `./www` into the appropriate native projects,
compile and then launch in the appropriate emulator or device.

	./bin/debug/ios
	./bin/debug/android

Testing
---

Professional software projects have tests. These scripts will copy the
contents of `./test` into the appropriate native project folders in
`./tmp`.

	./bin/test/ios
	./bin/test/android

You will need to further augment the built in Cordova scripts with your
own logic to appropriately copy in any custom JavaScript from your `./www`
folder to the `./test` directory. Put your custom scripts in `./lib`.
For example you could imagine creating a custom script like this in `./lib/test/all`:

	#! /bin/sh

	# clobber old file
	rm ./test/app.js

	# copy in new app.js	
	cp ./www/app.js ./test/app.js

	# call out to the Cordova test scripts
	./bin/test/ios
	./bin/test/android

From here you could update your `Makefile` with a new target something like this:

	test:
		./lib/test/all

Mobile is hard enough -- you won't regret automated unit tests.
		
Logging
---

By now you can probably guess how this is going to work.

	./bin/log/ios
	./bin/log/android

These tools log to stdout.

Plugins
---

Rudimentary PhoneGap Plugin support is being prototyped in Cordova. Plugins are installed under `./lib/plugin` and automatically 
built from a `./bin/debug/*`. Currently available plugin commands are:

	./bin/plugin/find ....... currently only outputs the online plugin registry
	./bin/plugin/install .... installs specified plugin locally
	./bin/plugin/list ....... lists locally installed plugins
	./bin/plugin/register ... registers a plugin with the online plugin registry
	./bin/plugin/remove ..... removes locally installed plugin
	./bin/plugin/validate ... validates specified (local) plugin package

Plugins are copied into `./tmp/*` during a debug build with the following commands:

	./bin/plugin/shotgun/ios ....... copies native/www code into correct places
	./bin/plugin/shotgun/android ... copies native/www code into correct places

Consider the `shotgun` scripts private for the moment. I'm fairly certain that logic will change.

Other Utilities
---

Cordova comes bundled with a suite of other useful utilities for mobile dev.

	./bin/util/validate-config ... validates `./www/config.xml`
	./bin/util/read-config ....... output a value from `./www/config.xml`
	./bin/util/version-index ..... adds version in `./www/config.xml` to `./www/index.html`
	./bin/util/weinre.jar ........ the amazing web inspector remote

TODO
---

- doc release