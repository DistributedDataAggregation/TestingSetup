import pandas as pd
import os



def results_compare(query_payload, response_json, file_path=None):

    if not file_path:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        file_path = os.path.join(data_dir, "small_size_some_keys_github_actions.parquet")
    
    df_test_parquet= pd.read_parquet(file_path)
    pandas_result = run_query_pandas(df_test_parquet, query_payload["group_columns"], query_payload["select"])
    pandas_result = pandas_result.fillna("null")

    compare_results(pandas_result, response_json["result"]["values"],query_payload["select"])


def run_query_pandas(df, group_columns, select):
    """
    Wykonuje zapytanie na DataFrame przy użyciu funkcji agregacyjnych.
    """
    # Tworzenie listy agregacji dla Pandas
    agg_funcs = {}

    func_mapping = {
        "Average": "mean",
        "Maximum": "max",
        "Minimum": "min",
        "Sum": "sum"
    }

    for sel in select:
        column = sel["column"]
        function = sel["function"]
        if function in func_mapping:
            col_name = f"{column}_{function}"
            agg_funcs[col_name] = (column, func_mapping[function])
        else:
            raise ValueError(f"Unsupported function: {function}")

    result = df.groupby(group_columns, dropna=False).agg(**agg_funcs).reset_index()

    if len(group_columns) > 1:
        result['grouping_value'] = result[group_columns].agg('|'.join, axis=1)
        result = result.drop(columns=group_columns)
        columns = ['grouping_value'] + [col for col in result.columns if col != 'grouping_value']
        result = result[columns]

    return result



def compare_results(pandas_result, api_result, select):
    """
    Porównuje wyniki Pandas i API.
    """
    # Konwersja wyniku API do DataFrame
    api_values = []
    for value in api_result:
        grouping_value = value["grouping_value"]
        result_values = {}

        for idx, res in enumerate(value["results"]):
            column_name = select[idx]["column"]
            function_name = select[idx]["function"]

            if function_name == "Average" and res["count"] > 0:
                result_values[f"{column_name}_{function_name}"] = res["value"] / res["count"]
            else:
                result_values[f"{column_name}_{function_name}"] = res["value"]

        api_values.append([grouping_value] + list(result_values.values()))

    columns = pandas_result.columns.tolist()

    api_df = pd.DataFrame(api_values, columns=columns)


    
    pandas_result = pandas_result.sort_values(by=columns[0]).reset_index(drop=True)
    api_df = api_df.sort_values(by=columns[0]).reset_index(drop=True)
    print(api_df)

    if pandas_result.equals(api_df):
        print("Wyniki Pandas i API są identyczne.")
        
    else: # Porównanie
        print("Wyniki Pandas i API różnią się!")
        print("\nWyniki Pandas:")
        print(pandas_result)
        print("\nWyniki API:")
        print(api_df)
        assert False, "Wyniki Pandas i API różnią się!"


# current_dir = os.path.dirname(os.path.abspath(__file__))
# data_dir = os.path.join(current_dir, "data")als(api_df):
# file_path = os.path.join(data_dir, "test.parquet")

# df_test_parquet= pd.read_parquet(file_path)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

# query_payload1 = {
#     "group_columns": ["Surname"],
#     "select": [
#         {"column": "Age", "function": "Maximum"},
#         {"column": "Age", "function": "Average"},
#         {"column": "Age", "function": "Minimum"}
     
#     ],
#     "table_name": "test",
# }

# overflow_result = run_query_pandas(df_test_parquet, query_payload1["group_columns"], query_payload1["select"])
# print(overflow_result)

