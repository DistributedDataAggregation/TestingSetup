import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import API_URL

@pytest.mark.integration
def test_response_format():
    """Testuje, czy odpowiedź ma poprawny format."""
    query_payload = {
        "group_columns": [
            "Position"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    
    response_json = response.json()
    
    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "int_value" in result, "'int_value' missing in one of the results."

@pytest.mark.integration
def test_response_multiple_selects():
    """Testuje, czy odpowiedź jest poprawna dla zapytania z wieloma funkcjami agregacji."""
    query_payload = {
        "group_columns": [
            "Position"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            },
            {
                "column": "Age",
                "function": "Minimum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    
    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "int_value" in result, "'int_value' missing in one of the results."

@pytest.mark.integration
def test_response_multiple_groups():
    """Testuje, czy odpowiedź jest poprawna dla zapytania z wieloma kolumnamy grupującymi."""
    query_payload = {
        "group_columns": [
            "Position", "Surname"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            },
            {
                "column": "Age",
                "function": "Minimum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    
    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert "grouping_value" in value, "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "int_value" in result, "'int_value' missing in one of the results."

@pytest.mark.integration
def test_parallel_requests():
    """Testuje, czy równoległe zapytania zwracają poprawne odpowiedzi."""
    query_payload_1 = {
        "group_columns": [
            "Position"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    query_payload_2 = {
        "group_columns": [
            "Position"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            },
            {
                "column": "Age",
                "function": "Minimum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    # Wysłanie zapytań równolegle
    response_1 = requests.post(API_URL, json=query_payload_1)
    response_2 = requests.post(API_URL, json=query_payload_2)
    
    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert response_1.status_code == 200, f"Expected HTTP 200 for query 1, got {response_1.status_code}"
    response_json_1 = response_1.json()
    assert "result" in response_json_1, "Key 'result' missing in response for query 1."
    
    # Sprawdzenie odpowiedzi dla drugiego zapytania
    assert response_2.status_code == 200, f"Expected HTTP 200 for query 2, got {response_2.status_code}"
    response_json_2 = response_2.json()
    assert "result" in response_json_2, "Key 'result' missing in response for query 2."

@pytest.mark.integration
def test_more_parallel_requests():
    """Testuje, czy rwiele równoległych zapytań zwraca poprawne odpowiedzi."""
    query_payload = {
        "group_columns": [
            "Position"
        ],
        "select": [
            {
                "column": "Salary",
                "function": "Maximum"
            }
        ],
        "table_name": "medium_size_few_keys_karol"
    }
    
    # Wysłanie zapytań równolegle
    response_1 = requests.post(API_URL, json=query_payload)
    response_2 = requests.post(API_URL, json=query_payload)
    response_3 = requests.post(API_URL, json=query_payload)
    response_4 = requests.post(API_URL, json=query_payload)
    
    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert response_1.status_code == 200, f"Expected HTTP 200 for query 1, got {response_1.status_code}"
    response_json_1 = response_1.json()
    assert "result" in response_json_1, "Key 'result' missing in response for query 1."
    
    # Sprawdzenie odpowiedzi dla drugiego zapytania
    assert response_2.status_code == 200, f"Expected HTTP 200 for query 2, got {response_2.status_code}"
    response_json_2 = response_2.json()
    assert "result" in response_json_2, "Key 'result' missing in response for query 2."

    # Sprawdzenie odpowiedzi dla trzeciego zapytania
    assert response_3.status_code == 200, f"Expected HTTP 200 for query 3, got {response_3.status_code}"
    response_json_3 = response_3.json()
    assert "result" in response_json_3, "Key 'result' missing in response for query 3."

    # Sprawdzenie odpowiedzi dla czwartego zapytania
    assert response_4.status_code == 200, f"Expected HTTP 200 for query 4, got {response_4.status_code}"
    response_json_4 = response_4.json()
    assert "result" in response_json_4, "Key 'result' missing in response for query 4."
