# How to run tests

## 1. Prerequisites

Install required packages:
```bash
pip install -r requirements.txt
```

Add `testa1`, `testab` and `yellow_tripdata_2024-01.parquet` files to your ***/home/data*** directory.

Have testing setup running.

## 2. Run all tests
```bash
pytest -v
```

## 3. Run tests from specific module
```bash
pytest -m [module-name] -v
```

example: 
```bash
pytest -m integration -v
```

