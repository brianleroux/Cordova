Early May
---

- `./test` working for each platform
- logging for each platform automated
- app www versioning


End of May
---

- plugins (its a copy/paste problem)
- icons for each platform from config.xml
- easy upgrade process (replace ./bin and write out Makefile-Example)
- docs folder for documentation
- include ./README.md ./generate-template/README.md and help in makefile from docs
- platform specific static files in ./www (eg app.android.css vs app.ios.css)
- automatically insturmenting weinre, etc
- package phonegap/iphone framework
- repackage phonegap-webos

Recipes TODO
---

These recipes are forthcoming...but I don't know when I will get to them. You can help! ;)

- boilerplate
- dojo
- jasmine
- jo
- jqtouch
- jquery
- sencha
- xui
- zepto	

(Pls do fork this project and add your own!!)

Cleanup Drudgery 
--

The leavings of fast hacking. Could happen that I (or you) get bored and want to refactor something simple.

- mv ./bin/create/w3c_config_reader ./bin/util/config-reader
- move logic in w3c_config_reader feature2intent to stand alone script
- mv ./bin/create/BeautifulSoup.py ./bin/util/BeatifulSoup.py
- mv ./bin/create/xcode-debug ./bin/util/xcode-debug
- rename scripts with prefixing if they are applicable to a single platform eg. ios-xcode-debug


Plugins Package Format
---

    ./
	 |-package.json ............ ala commonjs
	 |-test .................... not required but a good idea
	 |-native .................. native platform code
	 |   |-webos
	 |   |-ios
	 |   |  |-README.md ........ instructions for those whom copy/paste
	 |   |  |-Battery.h
	 |   |  `-Battery.m
	 |   |
	 |   `-android
	 |-wwww .................... plugin js src
	  `-plugin
	    `-battery
	      `-battery-0.0.1.js
	
To validate a plugin 
	

