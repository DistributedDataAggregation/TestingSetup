import pytest
import requests

# Adres endpointu API
API_URL = "http://localhost:80/api/v1/query"

# Dane wejściowe dla testu
QUERY_PAYLOAD = {
    "group_columns": [
        "RatecodeID", "passenger_count"
    ],
    "select": [
        {
            "column": "payment_type",
            "function": "Maximum"
        }
    ],
    "table_name": "yellow_tripdata_2024-01"
}

# Oczekiwany wynik testu
EXPECTED_RESULT = {
    "result": {
        "values": [
            {"grouping_value": "13", "results": [{"value": 4}]},
            {"grouping_value": "22", "results": [{"value": 4}]},
            {"grouping_value": "31", "results": [{"value": 4}]},
            {"grouping_value": "40", "results": [{"value": 4}]},
            {"grouping_value": "14", "results": [{"value": 4}]},
            {"grouping_value": "41", "results": [{"value": 4}]},
            {"grouping_value": "23", "results": [{"value": 4}]},
            {"grouping_value": "32", "results": [{"value": 4}]},
            {"grouping_value": "50", "results": [{"value": 4}]},
            {"grouping_value": "51", "results": [{"value": 4}]},
            {"grouping_value": "15", "results": [{"value": 4}]},
            {"grouping_value": "24", "results": [{"value": 4}]},
            {"grouping_value": "42", "results": [{"value": 4}]},
            {"grouping_value": "33", "results": [{"value": 4}]},
            {"grouping_value": "990", "results": [{"value": 3}]},
            {"grouping_value": "991", "results": [{"value": 2}]},
            {"grouping_value": "52", "results": [{"value": 4}]},
            {"grouping_value": "16", "results": [{"value": 4}]},
            {"grouping_value": "43", "results": [{"value": 4}]},
            {"grouping_value": "34", "results": [{"value": 4}]},
            {"grouping_value": "25", "results": [{"value": 4}]},
            {"grouping_value": "61", "results": [{"value": 4}]},
            {"grouping_value": "53", "results": [{"value": 4}]},
            {"grouping_value": "44", "results": [{"value": 4}]},
            {"grouping_value": "26", "results": [{"value": 3}]},
            {"grouping_value": "35", "results": [{"value": 3}]},
            {"grouping_value": "992", "results": [{"value": 2}]},
            {"grouping_value": "54", "results": [{"value": 4}]},
            {"grouping_value": "45", "results": [{"value": 2}]},
            {"grouping_value": "36", "results": [{"value": 3}]},
            {"grouping_value": "993", "results": [{"value": 1}]},
            {"grouping_value": "55", "results": [{"value": 4}]},
            {"grouping_value": "46", "results": [{"value": 2}]},
            {"grouping_value": "19", "results": [{"value": 1}]},
            {"grouping_value": "10", "results": [{"value": 4}]},
            {"grouping_value": "56", "results": [{"value": 2}]},
            {"grouping_value": "11", "results": [{"value": 4}]},
            {"grouping_value": "20", "results": [{"value": 4}]},
            {"grouping_value": "57", "results": [{"value": 2}]},
            {"grouping_value": "12", "results": [{"value": 4}]},
            {"grouping_value": "21", "results": [{"value": 4}]},
            {"grouping_value": "58", "results": [{"value": 3}]},
            {"grouping_value": "30", "results": [{"value": 4}]}
        ]
    }
}

MULTIPLE_SELECTS_PAYLOAD = {
    "group_columns": [
        "RatecodeID"
    ],
    "select": [
        {
            "column": "payment_type",
            "function": "Minimum"
        },
        {
            "column": "VendorID",
            "function": "Maximum"
        }
    ],
    "table_name": "yellow_tripdata_2024-01"
}

MULTIPLE_SELECTS_EXPECTED_RESULT = {
    "result": {
        "values": [
            {"grouping_value": "2", "results": [{"value": 1}, {"value": 2}]},
            {"grouping_value": "3", "results": [{"value": 1}, {"value": 2}]},
            {"grouping_value": "4", "results": [{"value": 1}, {"value": 2}]},
            {"grouping_value": "5", "results": [{"value": 1}, {"value": 2}]},
            {"grouping_value": "99", "results": [{"value": 1}, {"value": 2}]},
            {"grouping_value": "6", "results": [{"value": 2}, {"value": 2}]},
            {"grouping_value": "1", "results": [{"value": 1}, {"value": 2}]}
        ]
    }
}


@pytest.mark.system
def test_query_response_multiple_group_columns():
    response = requests.post(API_URL, json=QUERY_PAYLOAD)
    check_response(response, EXPECTED_RESULT)

@pytest.mark.system
def test_query_response_multiple_selects():
    response = requests.post(API_URL, json=MULTIPLE_SELECTS_PAYLOAD)
    check_response(response, MULTIPLE_SELECTS_EXPECTED_RESULT)


@pytest.mark.system
def test_query_response_parallel():
    response = requests.post(API_URL, json=QUERY_PAYLOAD)
    response2 = requests.post(API_URL, json=QUERY_PAYLOAD)
    
    check_response(response, EXPECTED_RESULT)
    check_response(response2, EXPECTED_RESULT)

def check_response(response, expected_result):
    """Wspólna funkcja do sprawdzania odpowiedzi."""
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()

    for expected_group in expected_result["result"]["values"]:
        grouping_value = expected_group["grouping_value"]
        expected_results = expected_group["results"]

        # Znajdź odpowiedni wpis w odpowiedzi
        actual_group = next((group for group in response_json["result"]["values"] if group["grouping_value"] == grouping_value), None)
        assert actual_group is not None, f"Grouping value {grouping_value} not found in response."
        assert actual_group["results"] == expected_results, (
            f"Results for grouping value {grouping_value} do not match.\n"
            f"Actual: {actual_group['results']}\nExpected: {expected_results}"
        )