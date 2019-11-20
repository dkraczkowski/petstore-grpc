# Petstore GRPC example

### Prerequisites
- Python >= 3.6
- Poetry
- python venv


### Installation
```bash
poetry install
poetry shell
python -m grpc.tools.protoc --proto_path=. --python_out=. --python_grpc_out=. --mypy_out=. petstore/proto/petstore.proto petstore/proto/services/*.proto
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
