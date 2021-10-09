## Generating gRPC files
`pip install grpcio-tools grpcio`

`python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto`
https://stackoverflow.com/questions/18351516/comparison-between-http-and-rpc
https://developers.google.com/protocol-buffers/docs/proto3

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

An error occurred while installing package 'defaults::pycodestyle-2.7.0-pyhd3eb1b0_0'.
Rolling back transaction: done

[Errno 13] Permission denied: '/Users/mommy/opt/anaconda3/lib/python3.8/site-packages/pycodestyle-2.7.0.dist-info/INSTALLER'
grpc._channel._InactiveRpcError: <_InactiveRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "Exception calling application: equipement"
    -added []: "details = "failed to connect to all addresses""

    $ unset http_proxy; unset https_proxy; python main.py &
    unset http_proxy; unset https_proxy; python writer.py
/Users/mommy/codebase/pythonProjects/nd064-c2-message-passing-exercises/lesson-3-implementing-message-passing/grpc-demo