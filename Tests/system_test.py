import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import API_URL

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
            {"grouping_value": "1|3", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|0", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|2", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|4", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|3", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|2", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|0", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|5", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|4", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|2", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|3", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "99|0", "results":[{"int_value": 3, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "99|1", "results":[{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|2", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|6", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|3", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|4", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|5", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "6|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|3", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|4", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|6", "results": [{"int_value": 3, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|5", "results": [{"int_value": 3, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "99|2", "results":[{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|4", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|5", "results": [{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|6", "results": [{"int_value": 3, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "99|3", "results":[{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|5", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4|6", "results": [{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|9", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|0", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|6", "results": [{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|0", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|7", "results": [{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1|2", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "2|1", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5|8", "results": [{"int_value": 3, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3|0", "results": [{"int_value": 4, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]}
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
            {"grouping_value": "2", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "3", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "4", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "5", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "99", "results": [{"int_value": 1,  "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "6", "results": [{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]},
            {"grouping_value": "1", "results": [{"int_value": 1, "is_null": False,'result_type': 'INT', 'aggregation': 'Minimum' },{"int_value": 2, "is_null": False,'result_type': 'INT', 'aggregation': 'Maximum' }]}
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
                        "double_value": 3000,
                        "is_null": False,
                        'result_type': 'DOUBLE',
                        'aggregation': 'Average' 
                    }
                ]
            },
            {
                "grouping_value": "null",
                "results": [
                    {
                        "double_value": 30,
                        "is_null": False,
                        'result_type': 'DOUBLE',
                        'aggregation': 'Average' 
                    }
                ]
            },
            {
                "grouping_value": "Developer",
                "results": [
                    {
                        "double_value": 1000,
                        "is_null": False,
                        'result_type': 'DOUBLE',
                        'aggregation': 'Average' 
                    }
                ]
            },
            {
                "grouping_value": "CEO",
                "results": [
                    {
                        "double_value": 5500,
                        "is_null": False,
                        'result_type': 'DOUBLE',
                        'aggregation': 'Average' 
                    }
                ]
            },
            {
                "grouping_value": "Designer",
                "results": [
                    {
                        "double_value": 2222,
                        "is_null": False,
                        'result_type': 'DOUBLE',
                        'aggregation': 'Average' 
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
      "function": "Maximum"
    },
    {
      "column": "Age",
      "function": "Sum"
    },
    {
      "column": "Age",
      "function": "Count"
    }
  ],
  "table_name": "data_null"
}

NULL_SELECT_EXPECTED_RESULT = {
    "result": {
        "error": None,
        "values": [
            {
                "grouping_value": "null",
                "results": [
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Average"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Maximum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Sum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Count"
                    }
                ]
            },
            {
                "grouping_value": "Manager",
                "results": [
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Average"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Maximum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Sum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Count"
                    }
                ]
            },
            {
                "grouping_value": "Developer",
                "results": [
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Average"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Maximum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Sum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Count"
                    }
                ]
            },
            {
                "grouping_value": "CEO",
                "results": [
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Average"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Maximum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Sum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Count"
                    }
                ]
            },
            {
                "grouping_value": "Designer",
                "results": [
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Average"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Maximum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Sum"
                    },
                    {
                        "is_null": True,
                        "result_type": "INT",
                        "aggregation": "Count"
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