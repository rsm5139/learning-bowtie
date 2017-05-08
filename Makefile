SHELL = /bin/sh
src_folder = build/src/

all: cleanall devel prod bugs

prod:
	python step_2.py prod

devel:
	python step_2.py build

bugs:
	# Replace 'socketio.run(app, host=host, port=port)'
	#   with 'socketio.run(app, host=host, port=port, use_reloader=False)'
	sed -i  '' -e 's/socketio.run(app, host=host, port=port)/socketio.run(app, host=host, port=port, use_reloader=False)/g' $(src_folder)server.py

cleanall:
	rm -rf build || true

.PHONY: cleanall bugs prod devel