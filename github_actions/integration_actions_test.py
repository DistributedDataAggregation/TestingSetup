import pytest
import requests
from helper_results import results_compare

# Adres endpointu API

#API_URL = "http://localhost:3000/api/v1/query" 
API_URL = "http://localhost:80/api/v1/query"

@pytest.mark.integration
def test_response_format_actions():
    """Testuje, czy odpowiedź ma poprawny format."""
    query_payload = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Age", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
            {"column": "Age", "function": "Average"}
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

    response_json = response.json()

    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert (
            "grouping_value" in value
        ), "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

    # Sprawdzenie wynikow 
    results_compare(query_payload=query_payload,response_json=response_json)

    for group in response_json["result"]["values"]:
        grouping_value = group["grouping_value"]
        results = group["results"]

        if grouping_value == "Kulik":
            assert results[0]["value"] == 77
            assert results[1]["value"] == -1
        elif grouping_value == "Kabatka":
            assert results[0]["value"] == 84
            assert results[1]["value"] == -4
        elif grouping_value == "Krol":
            assert results[0]["value"] == 86
            assert results[1]["value"] == -2

    
@pytest.mark.integration
def test_response_multiple_selects_actions():
    """Testuje, czy odpowiedź jest poprawna dla zapytania z wieloma funkcjami agregacji."""
    query_payload = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()

    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert (
            "grouping_value" in value
        ), "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

    results_compare(query_payload=query_payload,response_json=response_json)

@pytest.mark.integration
def test_response_multiple_groups_actions():
    """Testuje, czy odpowiedź jest poprawna dla zapytania z wieloma kolumnamy grupującymi."""
    query_payload = {
        "group_columns": ["Units of Time", "Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    response = requests.post(API_URL, json=query_payload)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()

    # Sprawdzenie struktury odpowiedzi
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."
    for value in response_json["result"]["values"]:
        assert (
            "grouping_value" in value
        ), "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

    results_compare(query_payload=query_payload,response_json=response_json)


@pytest.mark.integration
def test_parallel_requests_actions():
    """Testuje, czy równoległe zapytania zwracają poprawne odpowiedzi."""
    query_payload_1 = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    query_payload_2 = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    # Wysłanie zapytań równolegle
    response_1 = requests.post(API_URL, json=query_payload_1)
    response_2 = requests.post(API_URL, json=query_payload_2)

    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert (
        response_1.status_code == 200
    ), f"Expected HTTP 200 for query 1, got {response_1.status_code}"
    response_json_1 = response_1.json()
    assert "result" in response_json_1, "Key 'result' missing in response for query 1."

    # Sprawdzenie odpowiedzi dla drugiego zapytania
    assert (
        response_2.status_code == 200
    ), f"Expected HTTP 200 for query 2, got {response_2.status_code}"
    response_json_2 = response_2.json()
    assert "result" in response_json_2, "Key 'result' missing in response for query 2."

    results_compare(query_payload=query_payload_2,response_json=response_json_2)
    results_compare(query_payload=query_payload_1,response_json=response_json_1)


@pytest.mark.integration
def test_more_parallel_requests_actions():
    """Testuje, czy rwiele równoległych zapytań zwraca poprawne odpowiedzi."""
    query_payload = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name" :"small_size_some_keys_github_actions",
    }

    # Wysłanie zapytań równolegle
    response_1 = requests.post(API_URL, json=query_payload)
    response_2 = requests.post(API_URL, json=query_payload)
    response_3 = requests.post(API_URL, json=query_payload)
    response_4 = requests.post(API_URL, json=query_payload)

    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert (
        response_1.status_code == 200
    ), f"Expected HTTP 200 for query 1, got {response_1.status_code}"
    response_json_1 = response_1.json()
    assert "result" in response_json_1, "Key 'result' missing in response for query 1."

    results_compare(query_payload=query_payload,response_json=response_json_1)
    # Sprawdzenie odpowiedzi dla drugiego zapytania
    assert (
        response_2.status_code == 200
    ), f"Expected HTTP 200 for query 2, got {response_2.status_code}"
    response_json_2 = response_2.json()
    assert "result" in response_json_2, "Key 'result' missing in response for query 2."

    # Sprawdzenie odpowiedzi dla trzeciego zapytania
    assert (
        response_3.status_code == 200
    ), f"Expected HTTP 200 for query 3, got {response_3.status_code}"
    response_json_3 = response_3.json()
    assert "result" in response_json_3, "Key 'result' missing in response for query 3."

    # Sprawdzenie odpowiedzi dla czwartego zapytania
    assert (
        response_4.status_code == 200
    ), f"Expected HTTP 200 for query 4, got {response_4.status_code}"
    response_json_4 = response_4.json()
    assert "result" in response_json_4, "Key 'result' missing in response for query 4."
    results_compare(query_payload=query_payload,response_json=response_json_4)


@pytest.mark.integration
def test_splitting_files_to_nodes():
    """Testuje, czy nody dobrze obsluguja podzial plikow."""
    query_payload = {
        "group_columns": ["Name"],
        "select": [
            {"column": "Salary", "function": "Average"},
            {"column": "Salary", "function": "Minimum"},
            {"column": "Salary", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
            {"column": "Age", "function": "Sum"},
            {"column": "Age", "function": "Count"},
        ],
        "table_name" :"float_3_files_test",
    }

    response = requests.post(API_URL, json=query_payload)
    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert (
        response.status_code == 200
    ), f"Expected HTTP 200 for query 1, got {response.status_code}"
    response_json = response.json()
    assert "result" in response_json, "Key 'result' missing in response for query."


    results_compare(query_payload=query_payload,response_json=response_json,files_path=[
        "./data/float_3_files_test/float_3_files_test1.parquet",
        "./data/float_3_files_test/float_3_files_test2.parquet",
        "./data/float_3_files_test/float_3_files_test3.parquet"
    ])

@pytest.mark.integration
def test_sum_and_count():
    """
    Testuje, czy funkcje count i sum działają poprawnie
    """
    query_payload = {
        "group_columns": [
            "Colors", "Eye Colors", "Sports", "Car Brands", "Zodiac Signs"
        ],
        "select": [
            {"column": "Age", "function": "Count"},
            {"column": "Fibonacci Numbers", "function": "Maximum"},
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Kraje", "function": "Count"},
            {"column": "Days of the Month", "function": "Sum"},
            {"column": "Negative Numbers", "function": "Average"},
            {"column": "Prime Numbers", "function": "Average"}
        ],
        "table_name": "small_size_some_keys_github_actions"
    }

    response = requests.post(API_URL, json=query_payload)

    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert response.status_code == 200, (
        f"Expected HTTP 200 for query 1, got {response.status_code}"
    )
    
    response_json = response.json()
    assert "result" in response_json, "Key 'result' missing in response for query."
    
    results_compare(query_payload=query_payload, response_json=response_json)

@pytest.mark.integration
def test_sum_and_count_part2():
    """
    Testuje, czy funkcje count i sum działają poprawnie
    """
    query_payload =  {
                    "group_columns": ["Colors", "Eye Colors", "Sports", "Zodiac Signs"],
                    "select": [
                        {"column": "Age", "function": "Average"},
                        {"column": "Fibonacci Numbers", "function": "Maximum"},
                        {"column": "Cube Numbers", "function": "Count"},
                        {"column": "Odd Numbers", "function": "Average"},
                        {"column": "Shoe Sizes", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Sum"},
                        {"column": "Days of the Month", "function": "Sum"},
                        {"column": "Negative Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Count"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }

    response = requests.post(API_URL, json=query_payload)

    # Sprawdzenie odpowiedzi dla pierwszego zapytania
    assert response.status_code == 200, (
        f"Expected HTTP 200 for query 1, got {response.status_code}"
    )
    
    response_json = response.json()
    assert "result" in response_json, "Key 'result' missing in response for query."
    
    results_compare(query_payload=query_payload, response_json=response_json)

@pytest.mark.integration
def test_group_by_mixed_types():
    """
    Testuje, czy odpowiedź jest poprawna dla grupowania po kolumnach stringowych i integerowych.
    """
    query_payload = {
        "group_columns": ["Colors", "Shoe Sizes"],
        "select": [
            {"column": "Age", "function": "Maximum"},
            {"column": "Digits", "function": "Average"},
            {"column": "Cube Numbers", "function": "Sum"}
        ],
        "table_name": "small_size_some_keys_github_actions",
    }

    response = requests.post(API_URL, json=query_payload)

    # Sprawdzenie odpowiedzi
    assert response.status_code == 200, (
        f"Expected HTTP 200 for query, got {response.status_code}"
    )

    response_json = response.json()
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."

    for value in response_json["result"]["values"]:
        assert (
            "grouping_value" in value
        ), "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

    results_compare(query_payload=query_payload, response_json=response_json)

@pytest.mark.integration
def test_group_by_integers():
    """
    Testuje, czy odpowiedź jest poprawna dla grupowania po kolumnach typu integer.
    """
    query_payload = {
        "group_columns": ["Shoe Sizes", "Cube Numbers"],
        "select": [
            {"column": "Age", "function": "Count"},
            {"column": "Digits", "function": "Sum"},
            {"column": "Fibonacci Numbers", "function": "Average"}
        ],
        "table_name": "small_size_some_keys_github_actions",
    }   
    
    response = requests.post(API_URL, json=query_payload)

    # Sprawdzenie odpowiedzi
    assert response.status_code == 200, (
        f"Expected HTTP 200 for query, got {response.status_code}"
    )

    response_json = response.json()
    assert "result" in response_json, "Key 'result' missing in response."
    assert "values" in response_json["result"], "Key 'values' missing in 'result'."

    for value in response_json["result"]["values"]:
        assert (
            "grouping_value" in value
        ), "'grouping_value' missing in one of the values."
        assert "results" in value, "'results' missing in one of the values."
        for result in value["results"]:
            assert "value" in result, "'value' missing in one of the results."

    results_compare(query_payload=query_payload, response_json=response_json)
