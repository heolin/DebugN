# DebugN
Simple wrapper for sending Unity logs to http server


## About
I was testing achievement system for our new game so I created console app in python to watch Unity logs in realtime.
You can run python server on your PC and communicate with your game on device.

## Server
Server requires Python 2.7+ to run.

## Server usage
	To start server use:
	python ./simple_http_server.py --port <PORT> --file <PATH_TO_OUTPUT_FILE>

## Unity usage
	Add DebugN.cs file to your project.
	Insert your IP to host variable.
	To send log into server send use:
	DebugN.Log("Message");