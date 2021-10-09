import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):

        request_value = {
            "status": request.status,
            "created_at": request.created_at,
            "created_by": request.created_by,
            "id": request.id,
            "equipment": request.equipment
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)

    def Get(self, request, context):
        first_order = order_pb2.OrderMessage(
            id="2222",
            created_by="USER123",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-12',
            equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
        )

        second_order = order_pb2.OrderMessage(
            id="3333",
            created_by="USER123",
            status=order_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-11',
            equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
        )
        #return order_pb2.OrderMessageList().extend([first_order, second_order])
        result = order_pb2.OrderMessageList()
        result.orders.extend([first_order, second_order])
        print("giving you back some mock data for illustration purpose...")
        print(result)
        return result

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5006...")
server.add_insecure_port("[::]:5006")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
