import pytest
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import API_URL
from github_actions.helper_results import results_compare


# Zestawy testów
overflow_test = [
    {
        "name": "Possible overflow",
        "json": {
            "group_columns": ["Age"],
            "select": [
                {"column": "Salary", "function": "Average"}
            ],
            "table_name": "large_salary_overflow_dataset"
        }
    },
]

missing_values_test = [
    {
        "name": "Handle Missing Values",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Age", "function": "Average"}
            ],
            "table_name": "missing_values_dataset"
        }
    }
]

long_strings_test = [
    {
        "name": "Long String Handling",
        "json": {
            "group_columns": ["Name","Surname"],
            "select": [
                {"column": "Salary", "function": "Maximum"}
            ],
            "table_name": "long_strings_dataset"
        }
    }
]

zero_values_test = [
    {
        "name": "Handle Zero Values",
        "json": {
            "group_columns": ["Department"],
            "select": [
                {"column": "Budget", "function": "Sum"},
                {"column": "Budget", "function": "Average"}
            ],
            "table_name": "zero_values_dataset"
        }
    }
]
negative_values_test = [
    {
        "name": "Negative Values Handling",
        "json": {
            "group_columns": ["Category"],
            "select": [
                {"column": "Profit", "function": "Average"},
                {"column": "Profit", "function": "Minimum"}
            ],
            "table_name": "negative_values_dataset"
        }
    }
]

empty_dataset_test = [
    {
        "name": "Empty Dataset Handling",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Surname", "function": "Maximum"}
            ],
            "table_name": "empty_dataset"
        }
    }
]

zero_values_test = [
    {
        "name": "Handle Zero Values",
        "json": {
            "group_columns": ["Surname"],
            "select": [
                {"column": "Age", "function": "Maximum"},
                {"column": "Age", "function": "Average"}
            ],
            "table_name": "zero_values_dataset"
        }
    }
]

negative_values_test = [
    {
        "name": "Negative Values Handling",
        "json": {
            "group_columns": ["Age"],
            "select": [
                {"column": "Salary", "function": "Average"},
                {"column": "Salary", "function": "Minimum"}
            ],
            "table_name": "negative_values_dataset"
        }
    }
]

empty_dataset_test = [
    {
        "name": "Empty Dataset Handling",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Salary", "function": "Average"}
            ],
            "table_name": "empty_values_dataset"
        }
    }
]

nulls_dataset_tests = [
    {
        "name": "Empty Dataset Handling",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Age", "function": "Average"},
                {"column": "Age", "function": "Minimum"},
                {"column": "Age", "function": "Maximum"}
            ],
            "table_name": "edge_case_nulls_1"
        }
    },
       {
        "name": "Nulls Dataset",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Age", "function": "Average"},
                {"column": "Age", "function": "Minimum"},
                {"column": "Age", "function": "Maximum"}
            ],
            "table_name": "edge_case_nulls_2"
        }
    },
           {
        "name": "Empty Dataset Handling",
        "json": {
            "group_columns": ["Name"],
            "select": [
                {"column": "Age", "function": "Average"},
                {"column": "Age", "function": "Minimum"},
                {"column": "Age", "function": "Maximum"},
                {"column": "Age", "function": "Sum"},
                {"column": "Age", "function": "Count"},
            ],
            "table_name": "edge_case_nulls_3"
        }
    }
]


@pytest.mark.parametrize("test", overflow_test)
def test_overflow_queries(test):
    """Testuje przypadek overflow"""
    print(f"Running test: {test['name']}")
    try:
        response = requests.post(API_URL, json=test["json"])
        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
        response_json = response.json()
        
        assert "result" in response_json, "Key 'result' missing in response."
        assert "values" in response_json["result"], "Key 'values' missing in 'result'."
        for value in response_json["result"]["values"]:
            assert "grouping_value" in value, "'grouping_value' missing in one of the values."
            for result in value["results"]:
                assert "double_value" in result, "'double_value' missing in one of the results."
                if result["double_value"] < 0:
                    print(f"WARNING: Possible overflow detected! Grouping value: {value['grouping_value']}, Value: {result['double_value']}")
    except Exception as e:
        print(f"FAILED: {test['name']} - {e}")
        pytest.fail(f"Test failed for query {test['name']}")


@pytest.mark.edge
@pytest.mark.parametrize("test", missing_values_test)
def test_missing_values_queries(test):
    """Testuje przypadek brakujących wartości"""
    print(f"Running test: {test['name']}")
    
    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    
    # Walidacja wyników
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        for result in value["results"]:
            assert "double_value" in result, "'double_value' missing in one of the results."

    results_compare(
        query_payload=test["json"],
        response_json=response_json,
        files_path = ["/home/data/missing_values_dataset/missing_values_dataset.parquet"]
    )
    
@pytest.mark.edge
@pytest.mark.parametrize("test", long_strings_test)
def test_long_strings_queries(test):
    """Testuje przypadek długich ciągów znaków"""
    print(f"Running test: {test['name']}")

    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()

        # Walidacja wyników
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

@pytest.mark.edge
@pytest.mark.parametrize("test", negative_values_test)
def test_negative_value_queries(test):
    """Testuje przypadek negatywnych wartosci"""
    print(f"Running test: {test['name']}")

    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()

        # Walidacja wyników
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        for result in value["results"]:
             assert "value" in result or "double_value" in result, "'double_value' or 'value' missing in one of the results."

@pytest.mark.edge
@pytest.mark.parametrize("test", zero_values_test)
def test_zero_values_queries(test):
    """Testuje przypadek zerowych wartosci"""
    print(f"Running test: {test['name']}")

    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
        # Walidacja wyników
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        for result in value["results"]:
            assert "value" in result or "double_value" in result, "'double_value' or 'value' missing in one of the results."

@pytest.mark.edge
@pytest.mark.parametrize("test", empty_dataset_test)
def test_empty_dataset_queries(test):
    """Testuje przypadek pustego datasetu"""
    print(f"Running test: {test['name']}")

    response = requests.post(API_URL, json=test["json"])
    assert response.status_code == 500, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    # Walidacja wyników
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        for result in value["results"]:
           assert "double_value" in result, "'double_value' missing in one of the results."

# Bug jeszcze nie rozwiazany 
@pytest.mark.edge
@pytest.mark.parametrize("test", nulls_dataset_tests)
def test_empty_nulls_edge(test):
    """Testuje przypadek pustego datasetu"""
    print(f"Running test: {test['name']}")

    response = requests.post(API_URL, json=test["json"])
    print(test["json"])
    response_json = response.json()   
    print(response_json)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    # TODO dorob sprawdzanie wynikow 
    # results_compare(
    #     query_payload=test["json"],
    #     response_json=response_json,
    #     file_path = f"/home/data/{test['json']['table_name']}.parquet"
    # )