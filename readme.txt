I chose python as my language of choice. 
First, activate the virtual env and run:
pip install grpcio-tools

To generate the stubs, make sure you are in the same directory where debate.proto is
and run the following command:

	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. debate.proto 

No need to build server and client 

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




