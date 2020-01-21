# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import debate_pb2 as debate__pb2


class CandidateStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Answer = channel.unary_unary(
        '/routeguide.Candidate/Answer',
        request_serializer=debate__pb2.AnswerRequest.SerializeToString,
        response_deserializer=debate__pb2.AnswerReply.FromString,
        )
    self.Elaborate = channel.unary_unary(
        '/routeguide.Candidate/Elaborate',
        request_serializer=debate__pb2.ElaborateRequest.SerializeToString,
        response_deserializer=debate__pb2.ElaborateReply.FromString,
        )


class CandidateServicer(object):
  """The greeting service definition.
  """

  def Answer(self, request, context):
    """Sends a answer
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Elaborate(self, request, context):
    """Elaborate
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CandidateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Answer': grpc.unary_unary_rpc_method_handler(
          servicer.Answer,
          request_deserializer=debate__pb2.AnswerRequest.FromString,
          response_serializer=debate__pb2.AnswerReply.SerializeToString,
      ),
      'Elaborate': grpc.unary_unary_rpc_method_handler(
          servicer.Elaborate,
          request_deserializer=debate__pb2.ElaborateRequest.FromString,
          response_serializer=debate__pb2.ElaborateReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routeguide.Candidate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
