#!/bin/bash 
echo "Starting application"
APP_HOSTNAME=${APP_HOSTNAME:-0.0.0.0}
APP_PORT=${APP_PORT:-5000}
APP_DEBUG=${APP_DEBUG:-""}
flask run -h $APP_HOSTNAME -p $APP_PORT $APP_DEBUG
