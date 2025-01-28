tests_aws = [
    {
        "testname": "Yellow trip data",
        "queries": [
        {
          "name": "Simple query 1",
          "json": {
            "group_columns": ["VendorID"],
            "select": [
              {"column": "fare_amount", "function": "Maximum"},
            ],
            "table_name": "yellow_trip_2023"
          }
        },
        {
          "name": "Simple query 2",
          "json": {
            "group_columns": ["payment_type"],
            "select": [
              {"column": "total_amount", "function": "Average"},
              {"column": "trip_distance", "function": "Sum"}
            ],
            "table_name": "yellow_trip_2023"
          }
        },
        {
          "name": "Simple query 3",
          "json": {
            "group_columns": ["RatecodeID"],
            "select": [
              {"column": "trip_distance", "function": "Sum"},
              {"column": "passenger_count", "function": "Average"},
              {"column": "total_amount", "function": "Maximum"}
            ],
            "table_name": "yellow_trip_2023"
          }
        },
        {
          "name": "Medium query 1",
          "json": {
            "group_columns": ["passenger_count","payment_type"],
            "select": [
              {"column": "fare_amount", "function": "Average"},
              {"column": "tip_amount", "function": "Average"},
              {"column": "tip_amount", "function": "Minimum"}
            ],
            "table_name": "yellow_trip_2023"
          }
        },
        {
          "name": "Medium query 2",
          "json": {
            "group_columns": ["VendorID", "payment_type"],
            "select": [
              {"column": "tip_amount", "function": "Maximum"},
              {"column": "tip_amount", "function": "Minimum"},
              {"column": "tip_amount", "function": "Sum"},
              {"column": "tip_amount", "function": "Average"},
             {"column": "trip_distance", "function": "Maximum"},
              {"column": "trip_distance", "function": "Sum"},
            ],
            "table_name": "yellow_trip_2023"
          },
        },
          {
          "name": "Complex query 1",
          "json": {
            "group_columns": ["VendorID", "payment_type","passenger_count","RatecodeID"],
            "select": [
              {"column": "tip_amount", "function": "Maximum"},
              {"column": "tip_amount", "function": "Minimum"},
              {"column": "tip_amount", "function": "Sum"},
              {"column": "tip_amount", "function": "Average"},
             {"column": "trip_distance", "function": "Maximum"},
              {"column": "trip_distance", "function": "Sum"},
            ],
            "table_name": "yellow_trip_2023"
          }
        }
      ]
    },
     {
      "testname": "Simple_Menu_Test1",
      "queries": [
        {
          "name": "Simple query 1",
          "json": {
            "group_columns": ["menus_appeared"],
            "select": [
              { "column": "lowest_price", "function": "Maximum" },
              { "column": "lowest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Maximum" }
            ],
            "table_name": "przepisy"
          }
        },
        {
          "name": "Simple query 2",
          "json": {
            "group_columns": ["description"],
            "select": [
              { "column": "highest_price", "function": "Average" },
              { "column": "highest_price", "function": "Sum" }
            ],
            "table_name": "przepisy"
          }
        },
        {
          "name": "Simple query 3",
          "json": {
            "group_columns": ["menus_appeared"],
            "select": [
              { "column": "times_appeared", "function": "Maximum" },
              { "column": "times_appeared", "function": "Count" }
            ],
            "table_name": "przepisy"
          }
        },
        {
          "name": "Medium query 1",
          "json": {
            "group_columns": ["times_appeared", "menus_appeared"],
            "select": [
              { "column": "lowest_price", "function": "Average" },
              { "column": "highest_price", "function": "Average" },
              { "column": "lowest_price", "function": "Maximum" },
              { "column": "lowest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Maximum" },
              { "column": "description", "function": "Count" },
              { "column": "first_appeared", "function": "Minimum" },
              { "column": "first_appeared", "function": "Maximum" }
            ],
            "table_name": "przepisy"
          }
        },
        {
          "name": "Medium query 2",
          "json": {
            "group_columns": ["id"],
            "select": [
              { "column": "lowest_price", "function": "Minimum" },
              { "column": "first_appeared", "function": "Minimum" }
            ],
            "table_name": "przepisy"
          }
        },
        {
          "name": "Complex query 1",
          "json": {
            "group_columns": ["id", "description"],
            "select": [
              { "column": "lowest_price", "function": "Average" },
              { "column": "highest_price", "function": "Average" },
              { "column": "lowest_price", "function": "Maximum" },
              { "column": "lowest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Minimum" },
              { "column": "highest_price", "function": "Maximum" }
            ],
            "table_name": "przepisy"
          }
        },
      ]
    },
   {
      "testname": "benchmark",
      "queries": [
        {
          "name": "Simple query 1",
          "json": {
            "group_columns": ["machine_name"],
            "select": [
              { "column": "cpu_idle", "function": "Maximum" },
              { "column": "cpu_user", "function": "Average" },
              {"column":"disk_free","function":"Minimum"},
            ],
            "table_name": "benchmark"
          }
        },
        {
          "name": "Simple query 2",
          "json": {
            "group_columns": ["machine_group"],
            "select": [
              { "column": "disk_free", "function": "Sum" },
              { "column": "disk_total", "function": "Average" },
              {"column":"disk_free","function":"Maximum"},
              {"column":"disk_free","function":"Minimum"}
            ],
            "table_name": "benchmark"
          }
        },
        {
          "name": "Simple query 3",
          "json": {
            "group_columns": ["log_time"],
            "select": [
              { "column": "load_one", "function": "Average" },
              { "column": "load_five", "function": "Minimum" },
              { "column": "bytes_in", "function": "Average" },
              { "column": "bytes_out", "function": "Minimum" }
            ],
            "table_name": "benchmark"
          }
        },
        {
          "name": "Medium query 1",
          "json": {
            "group_columns": ["machine_name", "machine_group"],
            "select": [
              { "column": "bytes_in", "function": "Sum" },
              { "column": "bytes_out", "function": "Sum" },
              { "column": "mem_free", "function": "Average" },
              {"column":"disk_total","function":"Count"},
              {"column":"disk_total","function":"Sum"},
              {"column":"disk_total","function":"Average"},
              {"column":"disk_total","function":"Minimum"},
              {"column":"disk_total","function":"Maximum"},
     
            ],
            "table_name": "benchmark"
          }
        },
        {
          "name": "Medium query 2",
          "json": {
            "group_columns": ["machine_name", "machine_group"],
            "select": [
              { "column": "swap_free", "function": "Maximum" },
              { "column": "part_max_used", "function": "Minimum" },
              {"column":"disk_free","function":"Count"},
              {"column":"disk_free","function":"Sum"},
              {"column":"disk_free","function":"Average"},
              {"column":"disk_free","function":"Minimum"},
              {"column":"disk_free","function":"Maximum"},
              {"column":"mem_cached","function":"Count"},
              {"column":"mem_cached","function":"Sum"},
              {"column":"mem_cached","function":"Average"},
              {"column":"mem_cached","function":"Minimum"},
              {"column":"mem_cached","function":"Maximum"},
            ],
            "table_name": "benchmark"
          }
        },
        {
          "name": "Complex query 1",
          "json": {
            "group_columns": ["machine_name", "machine_group",'disk_total'],
            "select": [
              { "column": "cpu_idle", "function": "Average" },
              { "column": "cpu_system", "function": "Sum" },
              { "column": "cpu_user", "function": "Average" },
              { "column": "disk_free", "function": "Sum" },
              { "column": "load_one", "function": "Maximum" },
              { "column": "load_fifteen", "function": "Minimum" },
              { "column": "disk_free", "function": "Average" },
              { "column": "swap_free", "function": "Average" },
              { "column": "mem_free", "function": "Average" },
              { "column": "mem_cached", "function": "Average" },
              {"column":"cpu_nice","function":"Count"},
              {"column":"cpu_nice","function":"Sum"},
              {"column":"cpu_nice","function":"Average"},
              {"column":"cpu_nice","function":"Minimum"},
              {"column":"cpu_nice","function":"Maximum"},
              {"column":"mem_cached","function":"Count"},
              {"column":"mem_cached","function":"Sum"},
              {"column":"mem_cached","function":"Average"},
              {"column":"mem_cached","function":"Minimum"},
              {"column":"mem_cached","function":"Maximum"},
            ],
            "table_name": "benchmark"
          }
        }
      ]
    }
]
