# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

launch: venv shutdown
	. venv/bin/activate; FLASK_APP=app; Flask run --port 5000&
	. venv/bin/activate; FLASK_APP=Services/eventManager; Flask run --port 5001;

shutdown:
	ps -ef | grep "app.py" | grep -v grep | awk '{print $$2}' | xargs kill  
	ps -ef | grep "Services/eventManager.py" | grep -v grep | awk '{print $$2}' | xargs kill 
