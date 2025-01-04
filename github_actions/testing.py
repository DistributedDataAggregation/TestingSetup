import pandas as pd

df = pd.read_parquet("/home/data/long_strings_dataset.parquet")


print("Podgląd danych:")
print(df.head())



# Funkcja do wykonania zapytań w Pandas
def run_query_pandas(df, group_columns, select):

    agg_funcs = {}

    # Mapowanie funkcji agregujących
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
            agg_funcs[column] = func_mapping[function]
        else:
            raise ValueError(f"Unsupported function: {function}")

    return df.groupby(group_columns).agg(agg_funcs).reset_index()

def compare_results(pandas_result, api_result):
    """
    Porównuje wyniki Pandas i API.
    """
    # Konwersja wyniku API do DataFrame
    api_values = []
    for value in api_result:
        grouping_values = value["grouping_value"] if isinstance(value["grouping_value"], list) else [value["grouping_value"]]
        result_values = {res["column"]: res["value"] for res in value["results"]}
        api_values.append(grouping_values + list(result_values.values()))
    
    # Ustalanie nazw kolumn
    columns = pandas_result.columns.tolist()

    # Konwersja wyniku API do DataFrame
    api_df = pd.DataFrame(api_values, columns=columns)

    # Porównanie
    is_equal = pandas_result.equals(api_df)
    if is_equal:
        print("Wyniki Pandas i API są identyczne.")
    else:
        print("Wyniki Pandas i API różnią się!")
        print("\nWyniki Pandas:")
        print(pandas_result)
        print("\nWyniki API:")
        print(api_df)

# Wczytanie danych
df_overflow = pd.read_parquet("/home/data/large_salary_overflow_dataset.parquet")
df_missing_values = pd.read_parquet("/home/data/missing_values_dataset.parquet")
df_long_strings = pd.read_parquet("/home/data/long_strings_dataset.parquet")

# Zapytanie 1: Overflow Test
print("\n### Overflow Test ###")
overflow_query = {
    "group_columns": ["Age"],
    "select": [{"column": "Salary", "function": "Average"}]
}
overflow_result = run_query_pandas(df_overflow, overflow_query["group_columns"], overflow_query["select"])
print(overflow_result)

# Zapytanie 2: Missing Values Test
print("\n### Missing Values Test ###")
missing_values_query = {
    "group_columns": ["Name"],
    "select": [{"column": "Salary", "function": "Average"}]
}
missing_values_result = run_query_pandas(df_missing_values, missing_values_query["group_columns"], missing_values_query["select"])
print(missing_values_result)

# Zapytanie 3: Long Strings Test
print("\n### Long Strings Test ###")
long_strings_query = {
    "group_columns": ["Name","Surname"],
    "select": [{"column": "Salary", "function": "Maximum"}]
}
long_strings_result = run_query_pandas(df_long_strings, long_strings_query["group_columns"], long_strings_query["select"])
print(long_strings_result)


# average_age_by_surname = df.groupby("Surname")["Age"].mean().reset_index()

# max_age_by_surname = df.groupby("Surname")["Age"].max().reset_index()

# min_age_by_surname = df.groupby("Surname")["Age"].min().reset_index()

# min_age_by_surname = df.groupby("Surname")["Age"].min().reset_index()

# min_age_by_surname_vegetables = df.groupby(["Vegetables", "Surname"])["Age"].min().reset_index()
# max_age_by_surname_vegetables = df.groupby(["Vegetables", "Surname"])["Age"].max().reset_index()
# mean_age_by_surname_vegetables = df.groupby(["Vegetables", "Surname"])["Age"].mean().reset_index()

# min_cube_numbers_by_surname_vegetables = (
#     df.groupby(["Vegetables", "Surname"])["Cube Numbers"].min().reset_index()
# )
# max_cube_numbers_by_surname_vegetables = (Countries
#     df.groupby(["Vegetables", "Surname"])["Cube Numbers"].max().reset_index()
# )
# mean_cube_numbers_by_surname_vegetables = (
#     df.groupby(["Vegetables", "Surname"])["Cube Numbers"].mean().reset_index()
# )

# min_cube_numbers_by_surname = (
#     df.groupby(["Surname"])["Cube Numbers"].min().reset_index()
# )
# max_cube_numbers_by_surname = (
#     df.groupby([ "Surname"])["Cube Numbers"].max().reset_index()
# )
# mean_cube_numbers_by_surname = (
#     df.groupby(["Surname"])["Cube Numbers"].mean().reset_index()
# )

# print("\nŚredni wiek (Age) grupowany według Surname:")
# print(average_age_by_surname)

# print("\nMaksymalny wiek (Age) grupowany według Surname:")
# print(max_age_by_surname)

# print("\nMinimalny wiek (Age) grupowany według Surname:")
# print(min_age_by_surname)

# print("\nMinimalny wiek (Age) grupowany według Vegetables i Surname:")
# print(min_age_by_surname_vegetables)

# print("\nMaksymalny wiek (Age) grupowany według Vegetables i Surname:")
# print(max_age_by_surname_vegetables)

# print("\nŚredni wiek (Age) grupowany według Vegetables i Surname:")
# print(mean_age_by_surname_vegetables)

# print("\nMinimalne Cube Numbers grupowane według Vegetables i Surname:")
# print(min_cube_numbers_by_surname_vegetables)

# print("\nMaksymalne Cube Numbers grupowane według Vegetables i Surname:")
# print(max_cube_numbers_by_surname_vegetables)

# print("\nŚrednie Cube Numbers grupowane według Vegetables i Surname:")
# print(mean_cube_numbers_by_surname_vegetables)

# print("\nMinimalne Cube Numbers grupowane według Surname:")
# print(min_cube_numbers_by_surname)

# print("\nMaksymalne Cube Numbers grupowane według Surname:")
# print(max_cube_numbers_by_surname)

# print("\nŚrednie Cube Numbers grupowane według Surname:")
# print(mean_cube_numbers_by_surname)
