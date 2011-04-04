all: help

help:
	@echo try one of these commands:
	@echo "  create .... writes ou native code to ./tmp directory based on config.xml"
	@echo "  debug ..... copies www, compiles native src, installs and launches"
	@echo "  web ....... serve www at http://localhost:8000"
	@echo "  weinre .... launch weinre at http://localhost:8080"
	@echo "  test ...... compiles ./test into native"
	@echo "  log ....... launches logger"
	@echo "  release ... this is for you to implement!"
	@echo "  emulate ... launch platform emulators"

create:
	# write out the source for each native platform
	# careful, this is destructive!!!
	./bin/create/android
	./bin/create/ios
	./bin/create/webos

debug: 
	./bin/debug/android
	./bin/debug/ios
	./bin/debug/webos

web:
	cd ./www && python -m SimpleHTTPServer

weinre:
	java -jar ./bin/debug/weinre.jar

test:
	./bin/test/android
	./bin/test/ios
	./bin/test/webos	

log:
	echo TODO each platform has logging capability...

release:
	echo TODO this would be a good place for verioning, shortlog for changelog, minificaiton, key signing, etc

emulate:
	./bin/emulate/android
	./bin/emulate/ios
	./bin/emulate/webos

.PHONY: all