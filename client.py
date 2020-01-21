from __future__ import print_function
import logging

import grpc

import debate_pb2
import debate_pb2_grpc
import sys 


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = debate_pb2_grpc.CandidateStub(channel)

        mode = sys.argv[1] # get the mode, either answer or elaborate 
        mode = mode.lower() # convert to lower case
        if mode == "answer":
        	question = sys.argv[2]
        	response = stub.Answer(debate_pb2.AnswerRequest(question=question))

        else:
        	topic = sys.argv[2]
        	blah_run = sys.argv[3:]
        	blah_run = list(map(int, blah_run))
        	response = stub.Elaborate(debate_pb2.ElaborateRequest(topic=topic,blah_run=blah_run))

       # response = stub.SendAnswer(debate_pb2_grpc.AnswerRequest(name='you'))

    print(response.answer)


if __name__ == '__main__':
    logging.basicConfig()
    run()
