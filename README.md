# Petstore GRPC example
This is example project in python which utilizes GRPC framework. 

    Note: This project implements only category service for demo purposes.    

## Package structure
- `proto_files` - contains project's proto files
- `petstore` - contains python source code
- `tests`

### Prerequisites
- Python >= 3.6
- Poetry
- python venv


### Installation
```bash
poetry install
poetry shell
python -m grpc.tools.protoc --proto_path=proto_files --python_out=. --python_grpc_out=. --mypy_out=. proto_files/petstore/proto/petstore.proto proto_files/petstore/proto/services/*.proto
```

### Running tests
```bash
poetry shell
pytest .
```

### Running GRPC server
```bash
poetry shell
python petstore/server.py
```
