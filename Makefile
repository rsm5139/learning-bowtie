SHELL = /bin/sh
src_folder = build/src/

all: cleanall devel prod

prod:
	python step_2.py prod

devel:
	python step_2.py build
	# Replace 'socketio.run(app, host=host, port=port)'
	#   with 'socketio.run(app, host=host, port=port, use_reloader=False)'
	# **This avoids a bug that may be fixed in the future
	sed -i  '' -e 's/socketio.run(app, host=host, port=port)/socketio.run(app, host=host, port=port, use_reloader=False)/g' $(src_folder)server.py
	
cleanall:
	rm -rf build || true

.PHONY: cleanall devel prod