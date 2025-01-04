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
            {"grouping_value": "1|3", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|2", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "3|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|0", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "1|4", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|3", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "3|2", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|0", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "1|5", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|4", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|2", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "3|3", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "99|0", "results": [{"value": 3, "count": 0, "is_null": False}]},
            {"grouping_value": "99|1", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "5|2", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "1|6", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|3", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "3|4", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|5", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "6|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|3", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|4", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|6", "results": [{"value": 3, "count": 0, "is_null": False}]},
            {"grouping_value": "3|5", "results": [{"value": 3, "count": 0, "is_null": False}]},
            {"grouping_value": "99|2", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "5|4", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|5", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "3|6", "results": [{"value": 3, "count": 0, "is_null": False}]},
            {"grouping_value": "99|3", "results": [{"value": 1, "count": 0, "is_null": False}]},
            {"grouping_value": "5|5", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "4|6", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "1|9", "results": [{"value": 1, "count": 0, "is_null": False}]},
            {"grouping_value": "1|0", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|6", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "1|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|0", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|7", "results": [{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "1|2", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "2|1", "results": [{"value": 4, "count": 0, "is_null": False}]},
            {"grouping_value": "5|8", "results": [{"value": 3, "count": 0, "is_null": False}]},
            {"grouping_value": "3|0", "results": [{"value": 4, "count": 0, "is_null": False}]}
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
            {"grouping_value": "2", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "3", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "4", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "5", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "99", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "6", "results": [{"value": 2, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]},
            {"grouping_value": "1", "results": [{"value": 1, "count": 0, "is_null": False},{"value": 2, "count": 0, "is_null": False}]}
        ]
    }
}

NULL_GROUPING_PAYLOAD = {
    "group_columns": [
    "Position"
    ],
    "select": [
    {
      "column": "Salary",
      "function": "Average"
    }
  ],
  "table_name": "data_null"
}

# zakładam trzy pliki data_null
NULL_GROUPING_EXPECTED_RESULT = {
    "result": {
        "error": None,
        "values": [
            {
                "grouping_value": "Manager",
                "results": [
                    {
                        "value": 9000,
                        "count": 3,
                        "is_null": False
                    }
                ]
            },
            {
                "grouping_value": "null",
                "results": [
                    {
                        "value": 90,
                        "count": 3,
                        "is_null": False
                    }
                ]
            },
            {
                "grouping_value": "Developer",
                "results": [
                    {
                        "value": 3000,
                        "count": 3,
                        "is_null": False
                    }
                ]
            },
            {
                "grouping_value": "CEO",
                "results": [
                    {
                        "value": 33000,
                        "count": 6,
                        "is_null": False
                    }
                ]
            },
            {
                "grouping_value": "Designer",
                "results": [
                    {
                        "value": 6666,
                        "count": 3,
                        "is_null": False
                    }
                ]
            }
        ]
    },
}

NULL_SELECT_PAYLOAD = {
    "group_columns": [
    "Position"
  ],
  "select": [
  {
      "column": "Age",
      "function": "Average"
    },
   {
      "column": "Age",
      "function": "Minimum"
    },
   {
      "column": "Age",
      "function": "Maximum"
    }
  ],
  "table_name": "data_null"
}

NULL_SELECT_EXPECTED_RESULT = {
    "result": {
        "error": None,
        "values": [
            {
                "grouping_value": "Manager",
                "results": [
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    }
                ]
            },
            {
                "grouping_value": "null",
                "results": [
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    }
                ]
            },
            {
                "grouping_value": "Developer",
                "results": [
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    }
                ]
            },
            {
                "grouping_value": "CEO",
                "results": [
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    }
                ]
            },
            {
                "grouping_value": "Designer",
                "results": [
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    },
                    {
                        "value": 0,
                        "count": 0,
                        "is_null": True
                    }
                ]
            }
        ]
    },
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
def test_query_response_null_grouping():
    response = requests.post(API_URL, json=NULL_GROUPING_PAYLOAD)
    check_response(response, NULL_GROUPING_EXPECTED_RESULT)

@pytest.mark.system
def test_query_response_null_select():
    response = requests.post(API_URL, json=NULL_SELECT_PAYLOAD)
    check_response(response, NULL_SELECT_EXPECTED_RESULT)   


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