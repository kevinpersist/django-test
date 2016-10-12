#!/bin/bash
killall -9 uwsgi
uwsgi --ini mysite_uwsgi.ini --daemonize uwsgi.log --plugin python
