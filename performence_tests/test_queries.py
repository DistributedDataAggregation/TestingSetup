tests= [
    {
        "testname": "Small_MediumKeys_Test1",
        "queries": [
         {
                "name": "Simple query 1",
                "json": {
                    "group_columns": ["Surname"],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Age", "function": "Minimum"},
                        {"column": "Age", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Simple query 2",
                "json": {
                    "group_columns": ["Units of Time", "Surname"],
                    "select": [
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Age", "function": "Minimum"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Medium query 1",
                "json": {
                    "group_columns": ["Tree Names", "Company Departments"],
                    "select": [
                        {"column": "Prime Numbers", "function": "Minimum"},
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Fibonacci Numbers", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Medium query 2",
                "json": {
                    "group_columns": ["Tree Names", "Company Departments"],
                    "select": [
                        {"column": "Prime Numbers", "function": "Minimum"},
                        {"column": "Cube Numbers", "function": "Maximum"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Complex query 1",
                "json": {
                    "group_columns": ["Colors", "Eye Colors", "Sports","Car Brands", "Zodiac Signs"],
                    "select": [
                        {"column": "Age", "function": "Average"},
                        {"column": "Fibonacci Numbers", "function": "Maximum"},
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Kraje", "function": "Maximum"},
                        {"column": "Days of the Month", "function": "Minimum"},
                        {"column": "Negative Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
          
            {
                "name": "Complex query 2",
                "json": {
                    "group_columns": ["Colors", "Eye Colors", "Sports", "Tree Names", "Company Departments", "Car Brands", "Zodiac Signs", "Web Browsers", "Senses", "Letters"],
                    "select": [
                        {"column": "Age", "function": "Average"},
                        {"column": "Fibonacci Numbers", "function": "Maximum"},
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Odd Numbers", "function": "Average"},
                        {"column": "Shoe Sizes", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Maximum"},
                        {"column": "Days of the Month", "function": "Minimum"},
                        {"column": "Negative Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Complex query 3",
                "json": {
                    "group_columns": [
                        "Surname", "Age", "Colors", "Sports", "Eye Colors", "Tree Names", "Company Departments", "Car Brands", "Rainbow Colors", "Days of the Month", 
                        "Shoe Sizes", "Flowers", "Zodiac Signs", "Types of Fruits", "Web Browsers", "Cat Breeds", "Computer Brands", "Senses", "Letters", "Animals"
                    ],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Fibonacci Numbers", "function": "Average"},
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Odd Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Minimum"},
                        {"column": "Shoe Sizes", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Average"},
                        {"column": "Negative Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            },
            {
                "name": "Extreme complex query 1",
                "json": {
                    "group_columns": [
                        "Surname", "Age", "Colors", "Sports", "Eye Colors", "Tree Names", "Company Departments", "Car Brands", "Rainbow Colors", "Days of the Month", 
                        "Shoe Sizes", "Flowers", "Zodiac Signs", "Types of Fruits", "Web Browsers", "Cat Breeds", "Computer Brands", "Senses", "Letters", "Animals",
                        "Body Parts", "Mountains", "Grades", "Roles", "Logical Operators", "Payment Methods", "Vegetables", "Animals", "Prime Numbers", "Cube Numbers"
                    ],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Fibonacci Numbers", "function": "Average"},
                        {"column": "Cube Numbers", "function": "Maximum"},
                        {"column": "Odd Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Minimum"},
                        {"column": "Shoe Sizes", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Average"},
                        {"column": "Negative Numbers", "function": "Average"},
                        {"column": "Prime Numbers", "function": "Average"}
                    ],
                    "table_name": "small_size_some_keys_github_actions"
                }
            }
        ]
    },
    {
        "testname": "Medium_SmallKeys_Test1",
        "queries": [
            {
                "name": "Simple query 1",
                "json": {
                    "group_columns": ["Position"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Simple query 2",
                "json": {
                    "group_columns": ["Position"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"},
                        {"column": "Age", "function": "Minimum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Simple query 3",
                "json": {
                    "group_columns": ["Position"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Medium",
                "json": {
                    "group_columns": ["Position"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"},
                        {"column": "Age", "function": "Minimum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Parallel query 5",
                "json": {
                    "group_columns": ["Position"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Medium query 1",
                "json": {
                    "group_columns": ["Position", "Surname", "Age"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"},
                        {"column": "Age", "function": "Minimum"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            },
            {
                "name": "Complex query 2",
                "json": {
                    "group_columns": ["Position", "Age", "Surname"],
                    "select": [
                        {"column": "Salary", "function": "Maximum"},
                        {"column": "Salary", "function": "Minimum"},
                        {"column": "Salary", "function": "Average"}
                    ],
                    "table_name": "medium_size_few_keys_karol"
                }
            }
        ]
    },
    {
        "testname": "Medium_Size_Many_Keys_Queries_1",
        "queries": [
            {
                "name": "Simple query 1",
                "json": {
                    "group_columns": ["Surname"],
                    "select": [
                        {"column": "Age", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Simple query 2",
                "json": {
                    "group_columns": ["Countries"],
                    "select": [
                        {"column": "Digits", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Simple query 3",
                "json": {
                    "group_columns": ["Random"],
                    "select": [
                        {"column": "Age", "function": "Average"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Medium query 1",
                "json": {
                    "group_columns": ["Surname", "Countries"],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Age", "function": "Average"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Medium query 2",
                "json": {
                    "group_columns": ["RandomGIGA", "RandomMedium"],
                    "select": [
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Medium query 3",
                "json": {
                    "group_columns": ["Kraje", "Surname"],
                    "select": [
                        {"column": "Age", "function": "Average"},
                        {"column": "Digits", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Complex query 1",
                "json": {
                    "group_columns": ["Countries", "Surname", "Random"],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Maximum"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Complex query 2",
                "json": {
                    "group_columns": ["RandomGIGA", "RandomMedium"],
                    "select": [
                        {"column": "Digits", "function": "Maximum"},
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Kraje", "function": "Average"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            },
            {
                "name": "Complex query 3",
                "json": {
                    "group_columns": ["Surname", "Random"],
                    "select": [
                        {"column": "Age", "function": "Maximum"},
                        {"column": "Digits", "function": "Average"},
                        {"column": "Kraje", "function": "Average"}
                    ],
                    "table_name": "medium_size_many_keys"
                }
            }
        ]
    }
]
