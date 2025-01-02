import pytest
import requests
import math
from test_quries import Medium_SmallKeys_Test1, Small_MediumKeys_Test1
from tabulate import tabulate


# Adres endpointu API
# API_URL = "http://localhost:80/api/v1/query"
API_URL = "http://localhost:3000/api/v1/query"

NUMBER_OF_REPETITIONS = 5

results=[]



@pytest.mark.parametrize("query", Medium_SmallKeys_Test1)
def test_performence_once(query):
    """Testuje, czas odpowiedzi dla róznych zapytań"""

    response = requests.post(API_URL, json=query["json"])
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
    response_json = response.json()
    response_time = response.elapsed.total_seconds()
    response_time_from_response = float(response_json["processing_time"]) / 1000
    results.append((query["name"], response_time, response_time_from_response))

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



def test_display_results():
    print("\n")
    print(tabulate(results, headers=["Nazwa zapytania", "Czas odpowiedzi (s)"]))
    print("\n")

def calculate_standard_deviation(times, mean):
    variance = sum((time - mean) ** 2 for time in times) / len(times)
    return math.sqrt(variance)


@pytest.mark.parametrize("query", Medium_SmallKeys_Test1)
def test_performance_average(query):
    """Testuje czas odpowiedzi dla różnych zapytań, wykonując je wielokrotnie, obliczając średni czas i odchylenie standardowe."""
    response_times = []
    processing_times = []
    results=[]

    for _ in range(NUMBER_OF_REPETITIONS):
        response = requests.post(API_URL, json=query["json"])
        assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
        response_json = response.json()

        response_times.append(response.elapsed.total_seconds())
        processing_times.append(float(response_json["processing_time"]) / 1000)

        # Sprawdzenie struktury odpowiedzi
        assert "result" in response_json, "Key 'result' missing in response."
        assert "values" in response_json["result"], "Key 'values' missing in 'result'."
        for value in response_json["result"]["values"]:
            assert "grouping_value" in value, "'grouping_value' missing in one of the values."
            assert "results" in value, "'results' missing in one of the values."
            for result in value["results"]:
                assert "value" in result, "'value' missing in one of the results."

    avg_response_time = sum(response_times) / NUMBER_OF_REPETITIONS
    avg_processing_time = sum(processing_times) / NUMBER_OF_REPETITIONS
    stddev_response_time = calculate_standard_deviation(response_times, avg_response_time)
    stddev_processing_time = calculate_standard_deviation(processing_times, avg_processing_time)

    results.append((
        query["name"],
        avg_response_time,
        stddev_response_time,
        avg_processing_time,
        stddev_processing_time,
    ))

def test_display_results():
    """Wyświetla wyniki testów w tabeli."""
    print("\n")
    print(tabulate(
        results,
        headers=[
            "Nazwa zapytania", 
            "Średni czas odpowiedzi (s)", 
            "Odchylenie standardowe odpowiedzi (s)", 
            "Średni czas przetwarzania (s)", 
            "Odchylenie standardowe przetwarzania (s)"
        ]
    ))
    print("\n")





@pytest.mark.integration
def test_more_parallel_requests():
    """Testuje, czy rwiele równoległych zapytań zwraca poprawne odpowiedzi."""
    query_payload = {
        "group_columns": ["Surname"],
        "select": [
            {"column": "Cube Numbers", "function": "Maximum"},
            {"column": "Age", "function": "Minimum"},
        ],
        "table_name": "test",
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
