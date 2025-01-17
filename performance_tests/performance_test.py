import pytest
import requests
import math
from test_queries import tests
from tabulate import tabulate
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import API_URL


NUMBER_OF_REPETITIONS = 10
ENABLE_AVERAGE_TEST = False

results = []

@pytest.mark.parametrize("test", tests)
def test_performance_one(test):
    """Testuje czas odpowiedzi dla różnych zapytań (pojedyncze wykonanie)."""

    print(f"Table name: {test['testname']}")

    for query in test["queries"]:
        try:
            print(f"Test name: {query['name']}")
            response = requests.post(API_URL, json=query["json"])
            response_json = response.json()
            assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
            
            
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
                    if result['result_type'] == 'DOUBLE':
                        assert "double_value" in result, "double_value missing in one of the results. "
                    elif result['result_type'] == 'FLOAT':
                        assert "float_value" in result, "float_value missing in one of the results."
                    elif result['result_type'] == 'INT':
                        assert "int_value" in result, "int_value missing in one of the results."


            print("PASSED")
        except Exception as e:
            print(f"FAILED: {query['name']} - {e}")
            print(response_json)
            continue

    print("\n")
    print(tabulate(results, headers=["Nazwa zapytania", "Czas odpowiedzi (s)", "Czas przetwarzania z odpowiedzi (s)"]))
    print("\n")
    results.clear()

def calculate_standard_deviation(times, mean):
    """Oblicza odchylenie standardowe."""
    variance = sum((time - mean) ** 2 for time in times) / len(times)
    return math.sqrt(variance)

@pytest.mark.parametrize("test", tests)
def test_performance_average(test):
    """Testuje czas odpowiedzi dla różnych zapytań (wielokrotne wykonanie)."""
    if not ENABLE_AVERAGE_TEST:
        pytest.skip("Test średnich czasów wylaczony!")

    print(f"Table name: {test['testname']}")

    for query in test["queries"]:
        print(f"Test name: {query['name']}")
        response_times = []
        processing_times = []

        for _ in range(NUMBER_OF_REPETITIONS):
            try:
                response = requests.post(API_URL, json=query["json"])
                response_json = response.json()
                assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
             

                response_times.append(response.elapsed.total_seconds())
                processing_times.append(float(response_json["processing_time"]) / 1000)

                # Sprawdzenie struktury odpowiedzi
                assert "result" in response_json, "Key 'result' missing in response."
                assert "values" in response_json["result"], "Key 'values' missing in 'result'."
                for value in response_json["result"]["values"]:
                    assert "grouping_value" in value, "'grouping_value' missing in one of the values."
                    assert "results" in value, "'results' missing in one of the values."

                    for result in value["results"]:
                            if result['result_type'] == 'DOUBLE':
                                assert "double_value" in result, "double_value missing in one of the results. "
                            elif result['result_type'] == 'FLOAT':
                                assert "float_value" in result, "float_value missing in one of the results."
                            elif result['result_type'] == 'INT':
                                assert "int_value" in result, "int_value missing in one of the results."
            except Exception as e:
             print(f"FAILED: {query['name']} - {e}")
             print(response_json['result']['error'])
            continue

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
    results.clear()
