# python import
import csv


# Read CSV File
with open('sample-csv-to-html-exercise.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get the headers
    header = "".join(f'<th scope="col">{column}</th>' for column in headers)
    table_body = ""

    # Get the row data
    for row in reader:
        data = "".join(f'<td>{column}</td>\n' for column in row)
        table_body += "".join(f'<tr>\n{data}</tr>\n')


# Create table content using the fstrings
table_content = f'''
<table class="table">
<thead class="thead-dark">
<tr>
{header}
</tr>
</thead>
<tbody>
{table_body}
</tbody>
</table>
'''


# Heading Contents
heading = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV TO HTML </title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>
"""


# Body content and add table content into.
body = f"""
<body>
<div class="container">
<h1 class="text-center mt-2">CSV Data</h1>
{table_content}
<div>
<body>
"""


# Footer content
footer = """
</html>
"""

# Collect all the content and stor into a html_content
html_content = f"{heading} {body} {footer}"


# Read the HTMl file
with open('demo.html', encoding='utf-8') as hf:
    s = hf.read()
    s = s.replace(s, html_content)  # Replace the content of the HTML files


# Write the HTML file
with open('demo.html', "w", encoding='utf-8') as hf:
    hf.write(s)
