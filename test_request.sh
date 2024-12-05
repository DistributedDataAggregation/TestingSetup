curl -X 'POST' \
  'http://localhost:80/api/v1/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "group_columns": [
    "Position", "Age"
  ],
  "select": [
    {
      "column": "Salary",
      "function": "Min"
    }
  ],
  "table_name": "test"
}'