# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

launch: venv shutdown
	. venv/bin/activate; export set FLASK_APP=app; Flask run --port 5000 &
	. venv/bin/activate; export set FLASK_APP=Services/eventManager; Flask run --port 5001;

shutdown:
	ps -ef | grep python  | grep -v grep | awk '{print $$2}' | xargs kill 
	
