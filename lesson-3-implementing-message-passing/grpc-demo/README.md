## Generating gRPC files
`pip install grpcio-tools grpcio`

`python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto`
https://stackoverflow.com/questions/18351516/comparison-between-http-and-rpc
https://developers.google.com/protocol-buffers/docs/proto3
## How to run
### First set up a virtual environment:
conda --version 
conda env remove -n ENV_NAME
conda create --name snakes python=3.8
conda info --envs
conda activate snakes
### inside the virtual environment:
pip3 install grpcio-tools
conda list
python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto
python3 main.py

## References
https://blog.dreamfactory.com/grpc-vs-rest-how-does-grpc-compare-with-traditional-rest-apis/