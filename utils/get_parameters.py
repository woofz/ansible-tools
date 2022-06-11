import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import json


def get_module_parameters(module_name):
    """ Given module name, this function retrieves module's parameters from official ansible documentation """

    #url = f'https://docs.ansible.com/ansible/latest/collections/ansible/builtin/{module_name}_module.html#' \
    #      f'{module_name}-module'
    url = f'https://web.archive.org/web/20211017172704/http://docs.ansible.com/ansible/latest/collections/ansible/builtin/' \
          f'{module_name}_module.html#{module_name}-module' # Hot Fix...
    content = requests.get(url).content.decode()
    params = list(re.findall(r'parameter-(\w+)\"', content))
    params = list(dict.fromkeys(params))
    param_values = get_parameters_values(url)
    param_zip = zip(params, param_values)
    return dict(param_zip)


def get_parameters_values(url):
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")
    gdp = soup.find_all("table", attrs={"class": "documentation-table"})
    table1 = gdp[0]

    # the head will form our column names
    body = table1.find_all("tr")

    head = body[0]  # 0th item is the header row
    body_rows = body[1:]  # All other items becomes the rest of the rows

    headings = []
    for item in head.find_all("th"):  # loop through all th elements
        # convert the th elements to text and strip "\n"
        item = item.text.rstrip("\n")
        # append the clean column name to headings
        headings.append(item)

    all_rows = []  # will be a list for list for all rows
    for row_num in range(len(body_rows)):  # A row at a time
        row = []  # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"):  # loop through all row entries
            aa = re.sub("(\xa0)|(\n)|,", " ", row_item.text)
            row.append(aa)
        # append one row to all_rows
        all_rows.append(row)

    # We can now use the data on all_rows and headings to make a table
    # all_rows becomes our data and headings the column names
    df = pd.DataFrame(data=all_rows, columns=headings)
    values_list = []

    for item in df['Choices/Defaults']:
        item = item.replace('←', '').replace('Choices: ', '').replace('  ', ' ')
        values_list.append(item.split())

    return values_list
