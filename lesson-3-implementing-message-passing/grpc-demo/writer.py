import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("127.0.0.1:5006", options=(('grpc.enable_http_proxy', 0),))
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    created_by="algune hombre",
    status=order_pb2.OrderMessage.Status.QUEUED,
    id="4",
    created_at="2018-08-20'T'13:20:10*633+0000",
    equipment = [order_pb2.OrderMessage.Equipment.WEBCAM]
)


response = stub.Create(order)
