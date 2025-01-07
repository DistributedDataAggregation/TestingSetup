import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import API_URL



non_existent_column_test = [
    {
        "name": "Non-existent Column",
        "json": {
            "group_columns": ["NonExistentColumn"],
            "select": [
                {"column": "Salary", "function": "Average"}
            ],
            "table_name": "large_salary_overflow_dataset"
        }
    }
]


@pytest.mark.parametrize("test", non_existent_column_test)
def test_non_existent_column_queries(test):
    """Testuje zapytanie z kolumną, która nie istnieje"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 500, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json["result"], "Expected 'error' key in response"
    print(f"Error received: {response_json["result"]['error']}")


unsupported_data_type_test = [
    {
        "name": "Unsupported Data Type",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Date", "function": "Maximum"}
            ],
            "table_name": "missing_values_dataset"
        }
    }
]

@pytest.mark.parametrize("test", unsupported_data_type_test)
def test_unsupported_data_type_queries(test):
    """Testuje zapytanie z nieobsługiwanym typem danych"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 200, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json["result"], "Expected 'error' key in response"
    print(f"Error received: {response_json['result']['error']}")


invalid_function_test = [
    {
        "name": "Invalid Function",
        "json": {
            "group_columns": ["Age"],
            "select": [
                {"column": "Salary", "function": "Maximalum"}
            ],
            "table_name": "large_salary_overflow_dataset"
        }
    }
]

@pytest.mark.parametrize("test", invalid_function_test)
def test_invalid_function_queries(test):
    """Testuje zapytanie z nieobsługiwaną funkcją agregującą"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 400, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json['result'], "Expected 'error' key in response"
    print(f"Error received: {response_json['result']['error']}")



empty_query_test = [
    {
        "name": "Empty Query",
        "json": {}
    }
]

@pytest.mark.parametrize("test", empty_query_test)
def test_empty_query(test):
    """Testuje zapytanie z pustym JSON"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 400, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json['result'], "Expected 'error' key in response"
    print(f"Error received: {response_json['result']['error']}")

duplicated_columns_test = [
    {
        "name": "Duplicate Column in Group and Select",
        "json": {
            "group_columns": ["Name","Salary","Age"],
            "select": [
                {"column": "Wiek", "function": "Count"},
                {"column": "Age", "function": "Count"}
            ],
            "table_name": "missing_values_dataset"
        }
    }
    ,{
        "name": "Duplicate Column in Group and Select",
        "json": {
            "group_columns": ["Age","Age"],
            "select": [
                {"column": "Salary", "function": "Count"}
            ],
            "table_name": "missing_values_dataset"
        }
    },
]

@pytest.mark.parametrize("test", duplicated_columns_test)
def test_duplicated_column_query(test):
    """Testuje zapytanie z duplikowanymi kolumnami w JSON"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 400, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json['result'], "Expected 'error' key in response"
    print(f"Error received: {response_json['result']['error']}")


non_existent_table_test = [
    {
        "name": "Non-existent Table",
        "json": {
            "group_columns": ["Age"],
            "select": [
                {"column": "Salary", "function": "Average"}
            ],
            "table_name": "karol_przystojny"
        }
    }
]

@pytest.mark.parametrize("test", non_existent_table_test)
def test_non_existent_table_queries(test):
    """Testuje zapytanie z nieistniejącą tabelą"""
    print(f"Running test: {test['name']}")
    response = requests.post(API_URL, json=test["json"])
 
    assert response.status_code == 500, f"Expected HTTP 400, got {response.status_code}"
    response_json = response.json()
    assert "error" in response_json["result"], "Expected 'error' key in response"
    print(f"Error received: {response_json["result"]['error']}")
