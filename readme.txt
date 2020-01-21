# README.txt contains instructions how to build and run your code.

# TODO: document how to invoke protoc in order to generate the stubs in your
# language of choice.
# YOUR INSTRUCTIONS GO HERE

I chose python as my language of choice. 
First, activate the virtual env and run:
pip install grpcio-tools

To generate the stubs, make sure you are in the same directory where debate.proto is
and run the following command:

	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. debate.proto 


# TODO: document how to build your server and client code (if applicable)
# YOUR INSTRUCTIONS GO HERE

No need to build server and client 

# TODO: document how run your server (on localhost)
# YOUR INSTRUCTIONS GO HERE

To run the server, make sure you are in the correct directory and run:

	python server.py 

To run the client, make sure you are in the correct directory and run:

	python client.py [answer/elaborate] [question/topic] [blah_run]

Notes: For the question/topic, make sure you use quotes around them otherwise
the command line will take each word as a separate argument. blah_run is a list of integers
that are passed as individual parameters so be sure to pass each integer separately 

Elaborate examples: 
a. python client.py elaborate "foreign policy" 1 2 3
b. python client.py elaborate "foreign policy" 1
c. python client.py elaborate "foreign policy" 

Answer examples:
a. python client.py answer "who are you"
b. python client.py answer "testing"




