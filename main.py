from openpyxl import load_workbook
from rich.console import Console
import requests

console = Console()

workbook = load_workbook(filename="./movies.xlsx")
# print(workbook.sheetnames)
sheet = workbook.active
# print(sheet)

for value in sheet.iter_rows(min_row=2, max_row=3, min_col=1, max_col=1, values_only=True):
    value_split = value[0].split(" ")
    name = " ".join(value_split[:-1])
    link = value_split[-1]
    open("a.txt", "w").write(link)
    console.log(f"Testing [bright_magenta]{name}[/bright_magenta] at [bright_cyan bold]{link}[/bright_cyan bold]")
    response = requests.get(link, allow_redirects=True)
    console.log(f"Recieved {response.status_code}")
    console.log(f"Page {response.text}")

    print("")
