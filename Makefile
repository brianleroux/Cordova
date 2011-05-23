# since I'm revamping I'm using a tool that I think is faster and more
# descriptive for tests - http://pyvows.org
vows:
	@env PYTHONPATH=$$PYTHONPATH:. pyvows tests/
# Not sure if that's a appropriate, but since nose is pretty much the standard
# in python I guessed it to be a good choice.
test:
	@nosetests -s -v tests/
