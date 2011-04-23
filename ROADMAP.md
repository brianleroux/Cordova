0.1.0
===

- plugins (its a copy/paste problem)
- icons for each platform from config.xml

0.2.0
---

- platform specific static files in ./www (eg app.android.css vs app.ios.css)
- automatically insturmenting weinre, etc
- package phonegap/iphone framework
- phonegap-webos

0.3.0
---

- easy upgrade process (replace ./bin and write out Makefile-Example)
- include ./README.md ./generate-template/README.md and help in makefile from docs
- supress the insane amount of stdout noise in the common scripts

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

Contributer Notes
---

- each script should be a standalone executable
- make each script single purpose and use unix stdin, stdout, stderr
- rename scripts with prefixing if they are applicable to a single platform eg. ios-xcode-debug

