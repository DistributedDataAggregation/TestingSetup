import pandas as pd

df = pd.read_parquet("/home/data/MS.parquet")

print("Podgląd danych:")
print(df.head())

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
# max_cube_numbers_by_surname_vegetables = (
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
