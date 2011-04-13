Cordova Automation Scripts
===

A toolchain is a set of automations for common, tedious and likely error
prone tasks for software development. In particular, Mobile software develoment 
is rather hostile environment for developers with a distinct lack of open tools. 
The PhoneGap project has helped ease the pain of building apps but building with 
PhoneGap itself can be tedious. Despite providing a common abstraction the PhoneGap 
source itself is exascerbated by a proliferation of proprietary mobile operating sytems and 
sdks. Cordova removes tooling ambigutiy, unifies the nomenclature by providing 
everything neccessary to itereatively installable web apps. 

You will notice a consistent, readable and easily communicable style in
the script naming/pathing. These conventions make it trivially easy for
new developers to work with a Cordova based project and, more
importantly, extend one. Cordova scripts live in the root of your
project under a folder named `./bin`. Have a look around in that folder
to get an idea of the tools available to you. A `Makefile` gets
generated to further simplify common tasks.

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

Logging
---

By now you can probably guess how this is going to work.

	./bin/log/ios
	./bin/log/android

These tools log to stdout.

Other Utilities
---

Cordova comes bundled with a suite of other useful utilities.

	./bin/util/validate-config ... validates `./www/config.xml`
	./bin/util/read-config ....... output a value from `./www/config.xml`
	./bin/util/version-index ..... adds version in `./www/config.xml` to `./www/index.html`
	./bin/util/weinre.jar ........ the amazing web inspector remote

TODO
---

- doc plugins
- doc release



