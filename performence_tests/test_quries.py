# Queries plik Kacpra 8mb, średnio zróznicowane klucze wiele kolumn
Small_MediumKeys_Test1 = [
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
Medium_SmallKeys_Test1 = [
    {
        "name": "Simple query 1",
        "json": {
            "group_columns": ["Position"],
            "select": [{"column": "Salary", "function": "Maximum"}],
            "table_name": "MS",
        },
    },
    {
        "name": "Simple query 2",
        "json": {
            "group_columns": ["Position"],
            "select": [
                {"column": "Salary", "function": "Maximum"},
                {"column": "Age", "function": "Minimum"},
            ],
            "table_name": "MS",
        },
    },
    #    {
    #     "name": "Simple query 3",
    #     "json": {
    #         "group_columns": ["Position"],
    #         "select": [{"column": "Salary", "function": "Maximum"}],
    #         "table_name": "MS",
    #     },
    # },
    # {
    #     "name": "Simple query 4",
    #     "json": {
    #         "group_columns": ["Position"],
    #         "select": [
    #             {"column": "Salary", "function": "Maximum"},
    #             {"column": "Age", "function": "Minimum"},
    #         ],
    #         "table_name": "MS",
    #     },
    # },
    # {
    #     "name": "Parallel query 5",
    #     "json": {
    #         "group_columns": ["Position"],
    #         "select": [{"column": "Salary", "function": "Maximum"}],
    #         "table_name": "MS",
    #     },
    # },
    # {
    #     "name": "Medium query 1",
    #     "json": {
    #         "group_columns": ["Position", "Surname", "Age"],
    #         "select": [
    #             {"column": "Salary", "function": "Maximum"},
    #             {"column": "Age", "function": "Minimum"},
    #         ],
    #         "table_name": "MS",
    #     },
    # },
    # {
    #     "name": "Complex query 1",
    #     "json": {
    #         "group_columns": ["Name", "Surname", "Position"],
    #         "select": [
    #             {"column": "Salary", "function": "Maximum"},
    #             {"column": "Salary", "function": "Minimum"},
    #             {"column": "Salary", "function": "Average"},
    #             {"column": "Age", "function": "Maximum"},
    #             {"column": "Age", "function": "Minimum"},
    #             {"column": "Age", "function": "Average"}
    #         ],
    #         "table_name": "MS"
    #     },
    # },
    # {
    #     "name": "Complex query 2",
    #     "json": {
    #         "group_columns": ["Position", "Age", "Surname"],
    #         "select": [
    #             {"column": "Salary", "function": "Maximum"},
    #             {"column": "Salary", "function": "Minimum"},
    #             {"column": "Salary", "function": "Average"}
    #         ],
    #         "table_name": "MS"
    #     },
    # },
    {
        "name": "Complex query 3",
        "json": {
            "group_columns": ["Name", "Surname", "Position"],
            "select": [
                {"column": "Age", "function": "Maximum"},
                {"column": "Age", "function": "Minimum"},
                {"column": "Age", "function": "Average"},
                {"column": "Salary", "function": "Maximum"},
                {"column": "Salary", "function": "Minimum"},
                {"column": "Salary", "function": "Average"},
                {"column": "Salary", "function": "Average"},
                {"column": "Salary", "function": "Average"}
            ],
            "table_name": "MS"
        },
    }
]