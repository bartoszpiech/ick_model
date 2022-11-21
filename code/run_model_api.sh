#!/bin/sh

IP="192.168.1.62"

export FLASK_APP="model_api"
export FLASK_ENV="development"
flask run --host=$IP 2>model_api_logs.txt
