# Queries plik Kacpra 8mb, średnio zróznicowane klucze wiele kolumn
queries_1 = [
    {
        "name": "Simple test 1",
        "json": {
            "group_columns": ["Surname"],
            "select": [
                {"column": "Age", "function": "Maximum"},
                {"column": "Age", "function": "Minimal"},
                {"column": "Age", "function": "Average"},
            ],
            "table_name": "test",
        },
    },
    {
        "name": "Simple test 2",
        "json": {
            "group_columns": ["Units of Time", "Surname"],
            "select": [
                {"column": "Cube Numbers", "function": "Maximum"},
                {"column": "Age", "function": "Maximum"},
            ],
            "table_name": "test",
        },
    },
    {
        "name": "Medium query 2",
        "json": {
            "group_columns": ["Tree Names", "Company Departments"],
            "select": [
                {"column": "Prime Numbers", "function": "Count"},
                {"column": "Cube Numbers", "function": "Maximum"},
            ],
            "table_name": "test",
        },
    },
    {
        "name": "Complex query 1",
        "json": {
            "group_columns": ["Colors", "Eye Colors", "Sports"],
            "select": [
                {"column": "Age", "function": "Average"},
                {"column": "Fibonacci Numbers", "function": "Maximum"},
                {"column": "Cube Numbers", "function": "Maximum"},
            ],
            "table_name": "test",
        },
    },
]

# Quries plik karola 1gb, wiele danych, mało zróznicowane wartości
queries_2 = [
    {
        "name": "Simple query 1",
        "json": {
            "group_columns": ["Position"],
            "select": [{"column": "Salary", "function": "Maximum"}],
            "table_name": "ala",
        },
    },
    {
        "name": "Multiple selects query",
        "json": {
            "group_columns": ["Position"],
            "select": [
                {"column": "Salary", "function": "Maximum"},
                {"column": "Age", "function": "Minimum"},
            ],
            "table_name": "ala",
        },
    },
    {
        "name": "Multiple groups query",
        "json": {
            "group_columns": ["Position", "Surname"],
            "select": [
                {"column": "Salary", "function": "Maximum"},
                {"column": "Age", "function": "Minimum"},
            ],
            "table_name": "ala",
        },
    },
    {
        "name": "Parallel query 1",
        "json": {
            "group_columns": ["Position"],
            "select": [{"column": "Salary", "function": "Maximum"}],
            "table_name": "ala",
        },
    },
    {
        "name": "Parallel query 2",
        "json": {
            "group_columns": ["Position"],
            "select": [
                {"column": "Salary", "function": "Maximum"},
                {"column": "Age", "function": "Minimum"},
            ],
            "table_name": "ala",
        },
    },
    {
        "name": "More parallel query 1",
        "json": {
            "group_columns": ["Position"],
            "select": [{"column": "Salary", "function": "Maximum"}],
            "table_name": "ala",
        },
    },
]
