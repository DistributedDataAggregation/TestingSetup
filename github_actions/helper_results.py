import pandas as pd
import os


def results_compare(query_payload, response_json, files_path=None):

    if not files_path:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        file_path = os.path.join(data_dir, "small_size_some_keys_github_actions.parquet")
        files_path = [file_path]
    
    df_test_parquet = pd.concat([pd.read_parquet(file) for file in files_path], ignore_index=True)
     
    pandas_result = run_query_pandas(df_test_parquet, query_payload["group_columns"], query_payload["select"])
    
    pandas_result = pandas_result.fillna("null")
    # print(pandas_result)
    # print(response_json["result"]["values"])
    
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
        "Sum": "sum",
        "Count":"count"
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
        result['grouping_value'] = result[group_columns].astype(str).agg('|'.join, axis=1)
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

            value_string = "value"  

            if "result_type" in res:
                result_type = res["result_type"]

                if result_type == "INT":
                    value_string = "value"
                elif result_type == "DOUBLE":
                    value_string = "double_value"
                elif result_type == "FLOAT":
                    value_string = "float_value"

            if function_name == "Average" and res["count"] > 0:
                # Calculate and round to 5 decimal points
                avg_value = res[value_string] / res["count"]
                result_values[f"{column_name}_{function_name}"] = round(avg_value, 6)
            elif function_name == "Count":
                result_values[f"{column_name}_{function_name}"] = res["count"]
            else:
                result_values[f"{column_name}_{function_name}"] = res[value_string]

        api_values.append([grouping_value] + list(result_values.values()))

    columns = pandas_result.columns.tolist()

    api_df = pd.DataFrame(api_values, columns=columns)

    # Ensure Pandas result averages are rounded to 5 decimal points for comparison
    for col in pandas_result.columns[1:]:
        if "_Average" in col:
            pandas_result[col] = pandas_result[col].round(6)

    pandas_result = pandas_result.sort_values(by=columns[0]).reset_index(drop=True)
    api_df = api_df.sort_values(by=columns[0]).reset_index(drop=True)

    if pandas_result.equals(api_df):
        print("Wyniki Pandas i API są identyczne.")
    else:
        print("Wyniki Pandas i API różnią się!")
        print("\nWyniki Pandas:")
        print(pandas_result)
        print("\nWyniki API:")
        print(api_df)
        assert False, "Wyniki Pandas i API różnią się!"

