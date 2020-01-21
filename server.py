from concurrent import futures
import logging

import grpc

import debate_pb2
import debate_pb2_grpc
import consultation_pb2
import consultation_pb2_grpc
import random


class Candidate(debate_pb2_grpc.CandidateServicer):

    def Answer(self, request, context):

        question = request.question
        question = question.lower() # convert to lower case

        if question.split()[0] in ['why', 'what', 'how', 'who', 'when']:

            # call Retort with question
            with grpc.insecure_channel('23.236.49.28:50051') as channel:
                stub = consultation_pb2_grpc.CampaignManagerStub(channel)
                retort_response = stub.Retort(consultation_pb2.RetortRequest(original_question=request.question))

            # replace all "you" with "i" and all "your" with "my"
            question_stub = question.replace('your', 'my')
            question_stub = question_stub.replace('you', 'I')

            return debate_pb2.AnswerReply(answer="You asked me " + question_stub + " but I want to say that " + retort_response.retort)

        else:
            # randomly select 0 or 1 and return a response 
            num = random.randint(0,1)
            if num == 0:
                return debate_pb2.AnswerReply(answer="your 3 cent titanium tax goes too far")
            else:
                return debate_pb2.AnswerReply(answer="your 3 cent titanium tax doesn't go too far enough​")

    def Elaborate(self, request, context):
        topic = request.topic
        blah_run = request.blah_run

        output = ""
        if len(blah_run) == 0:
            output = topic
        else:
            for i in blah_run:
                output += "blah " * i + topic + " "

        return debate_pb2.ElaborateReply(answer=output)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    debate_pb2_grpc.add_CandidateServicer_to_server(Candidate(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
