0.3.0
---

- easy upgrade process (replace ./bin and write out Makefile-Example)
- package phonegap/iphone framework

0.4.0

- supress the insane amount of stdout noise in the common scripts
- phonegap-webos
- make android:screenOrientation = "portrait" by default. same for ios
- dojo mobile recipe

0.5.0

- ./bin/release

Future
---

- platform specific static files in ./www (eg app.android.css vs app.ios.css)
- include ./README.md ./generate-template/README.md and help in makefile from docs
- automatically insturmenting weinre, etc

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

