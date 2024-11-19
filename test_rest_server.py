"""
This is is pytest module for testing the functionality of REST API  from the rest_server.py module.
To run the tests, please execute "pytest" command in the same directory as this file.
"""

from typing import List
import csv
import json
import random
import requests
import pandas as pd


def get_valid_hosts() -> List:
    """
    This function reads the "source" column from a CSV report file
    and returns it as a list of all valid hosts mentioned in the report.

    Returns:
        List : list of valid hosts
    """
    df = pd.read_csv("vulnerabilities(fixed).csv")
    return df["source"].tolist()


def get_random_valid_host() -> List:
    """
    This function selects a random host from the list of all valid hosts.

    Returns:
        str : a random host from the list of valid hosts
    """
    hosts = get_valid_hosts()
    return random.choice(hosts)


def get_host_record_count(host: str) -> int:
    """
    Given a host, this function returns the number of records associated
    with the host in a CSV report file.

    Parameters
        host: The host for which to find the number of records.

    Returns:
        The number of records associated with the host.
    """
    hosts = get_valid_hosts()
    return hosts.count(host)


def is_ascending_order(lst: List) -> bool:
    """
    This function checks if the elements of a provided list are in ascending order.

    Parameters:
        lst (List): Input list

    Returns:
         True if the elements in the list are in ascending order else False.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def get_pagination_page_count(host: str, limit: int) -> int:
    """
    This function determines the total number of pages required to paginate the
        vulnerability records of a specific host based on provided pagination limit.

    Parameters:
        host (str): the host for which pagination page count is to be calculated
        limit (int): the maximum number of records per page

    Returns:
        Total number of pages needed for pagination
    """
    record_count = get_host_record_count(host)
    count = record_count // limit
    page_count = count if (record_count % limit == 0) else (count + 1)
    return page_count


def get_top_ten_vulnerabilities_for_host(host: str) -> List:
    """
    Given a host, this function returns a list of the top 10 vulnerabilities
    for that host, sorted by risk_score in descending order.

    Parameters
        host (str): The host for which to find the top vulnerabilities.

    Returns:
        A list of the top 10 vulnerabilities for the given host, sorted by
        risk_score in descending order.
    """
    with open("vulnerabilities(fixed).csv") as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader)
        records = list(reader)

    # Sort the records by the risk_score column in descending order
    records = sorted(records, key=lambda x: int(x[3]), reverse=True)
    host_records = [record for record in records if record[1] == host]
    top_10 = host_records[:10]
    return top_10


def identical_risks(dict_list: List, list_list: List) -> bool:
    """
    Parameters:
        dict_list (List[Dict]): list of dictionaries where each dictionary has
        a key value pair "risk_score"
        list_list (List[List]): list of lists where each list has 4 elements,
        and the 4th element represents risk

    Returns:
        bool: True if the risk element of each list in list_list matches the
        risk_score value of the corresponding dictionary in dict_list, else False.
    """
    if len(dict_list) != len(list_list):
        return False
    for i, _ in enumerate (dict_list):
        if dict_list[i]["risk_score"] != int(list_list[i][3]):
            return False
    return True


def test_get_top_ten_riskiest_vulnerabilities():
    """
    This test verifies that the ten-riskiest-vulnerabilities endpoint returns
    the top ten most critical vulnerabilities for a specified host.

    Parameters:
        None

    Returns:
        None

    Raises:
        AssertionError: If the top ten risks are not returned correctly by the call.
    """
    host = get_random_valid_host()
    url = f"http://127.0.0.1:5000/hosts/{host}/ten-riskiest-vulnerabilities"
    response = requests.get(url=url, timeout=10)
    records = json.loads(response.text)["data"]
    # in order to have a valid comparison, we need to use a different method from
    # panda's method used on the server side. Instead of pandas, we will use a csv
    # reader to read the host data from the vulnerabilities(fixed).csv
    # file and then compare the risk_scores with records from the server side.
    top_ten = get_top_ten_vulnerabilities_for_host(host)
    assert identical_risks(records, top_ten)


def test_get_top_ten_riskiest_vulnerabilities_count():
    """
    This function tests the number of vulnerabilities returned by the API endpoint
    for a specific host. It verifies that the number of records in the data field equals 10.

    This function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an
        assertion error if the count of records is not equal to 10,
        or to a record count for the host if it is less than 10.
    """
    host = get_random_valid_host()
    url = f"http://127.0.0.1:5000/hosts/{host}/ten-riskiest-vulnerabilities"
    response = requests.get(url=url, timeout=10)
    records = json.loads(response.text)["data"]
    count = len(records)
    assert count == 10


def test_get_top_ten_riskiest_vulnerabilities_invalid_host():
    """
    This function tests that an assertion error is raised when an invalid host that
    doesn't have records in the error log is passed to the API.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        when an invalid host is passed as a parameter to the API.
    """
    url = "http://127.0.0.1:5000/hosts/0.0.0.0/sorted-vulnerabilities"
    response = requests.get(url=url, timeout=10)
    assert response.status_code == 404


def test_get_alphabetically_sorted_vulnerabilities():
    """
    This function tests whether the vulnerabilities returned by the API endpoint are in
    alphabetical order.
    The function does not require any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        if the list of vulnerabilities is not in alphabetical order.
    """
    host = get_random_valid_host()
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities"
    response = requests.get(url=url, timeout=10)
    records = json.loads(response.text)["data"]
    vulnerabilities = [record["vulnerability"] for record in records]
    assert is_ascending_order(vulnerabilities)


def test_pagination_default_limit():
    """
    This function verifies that the default value of the pagination limit parameter is
    set to 10 and the call to the endpoint returns 10 records, or the number of records
    the host has in the log if it is less than 10.
    The function does not require any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        if the list of vulnerabilities is not in alphabetical order.
    """
    host = get_random_valid_host()
    host_record_count = get_host_record_count(host)
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities"
    response = requests.get(url=url, timeout=10)
    data = json.loads(response.text)["data"]
    assert response.status_code == 200
    assert len(data) == (min(10, host_record_count))


def test_pagination_last_page():
    """
    This function verifies that the number of records on the last page can be less
    than the limit value. The test uses a specified host with 48 records and a pagination
    limit of 10 records per page. The expected result is that the fifth page will contain 8 records.
    The function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        if the last page doesn't contain 8 records.
    """
    host = "118.127.3.27"
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page=5&limit=10"
    response = requests.get(url=url, timeout=10)
    data = json.loads(response.text)["data"]
    assert response.status_code == 200
    assert len(data) == 8


def test_pagination_invalid_page():
    """
    This function tests that an assertion error will be raised when the
    starting offset for pagination is greater than the number of records.
    The test determines the number of pages for a given limit and then passes
    a page number that exceeds the calculated number of pages to the API endpoint.
    The function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        because the specified starting page for pagination is larger that the number of pages.

    """
    host = get_random_valid_host()
    limit = 10
    pages = get_pagination_page_count(host, limit)
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page={pages+1}&limit={limit}"
    response = requests.get(url=url, timeout=10)
    assert response.status_code == 404


def test_pagination_negative_limit():
    """
    This function tests that an assertion error will be raised when a negative value is
     passed as the limit parameter to the API endpoint.
     The function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        because the limit value can not be negative.
    """
    host = get_random_valid_host()
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page=1&limit=-1"
    response = requests.get(url=url, timeout=10)
    assert response.status_code == 404


def test_pagination_negative_page():
    """
    This function tests that an assertion error will be raised when a negative value
    is passed as the starting page number parameter to the API endpoint.
    The function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        because the starting page number can not be negative.
    """
    host = get_random_valid_host()
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page=-1&limit=10"
    response = requests.get(url=url, timeout=10)
    assert response.status_code == 404


def test_pagination_edge_cases():
    """
    This function tests that the edge cases for passing page and limit values to
    the API endpoint are handled correctly.
    The test includes two scenarios: the first sets the starting page to 1 and the
    limit value to the number of records for the specified host, while the second
    test sets the starting page to the number of records for the specified host and
    the limit value to 1.
    The function does not take any parameters.

    Returns:
        None: This function does not return any value, but it raises an assertion error
        if the wrong number of records is returned from the call.
    """
    host = get_random_valid_host()
    record_count = get_host_record_count(host)
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page=1&limit={record_count}"
    response = requests.get(url=url, timeout=10)
    data = json.loads(response.text)["data"]
    assert response.status_code == 200
    assert len(data) == record_count

    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page={record_count}&limit=1"
    response = requests.get(url=url, timeout=10)
    data = json.loads(response.text)["data"]
    assert response.status_code == 200
    assert len(data) == 1


def test_pagination_query_parameters():
    """
    This function tests the correctness of the pagination parameters returned by an
    API endpoint for a specified host.
    It verifies that the 'page', 'limit', 'page_count' and 'record_count' values in
    the pagination field match the expected values.
    This function does not take any parameters.

    Returns:
    None: This function does not return any value, but it raises an
    assertion error if the query parameters are not working correctly.
    """
    host = get_random_valid_host()
    page = 3
    limit = 5
    url = f"http://127.0.0.1:5000/hosts/{host}/sorted-vulnerabilities/?page={page}&limit={limit}"
    response = requests.get(url=url, timeout=10)
    pagination = json.loads(response.text)["pagination"]
    assert pagination["page"] == page
    assert pagination["limit"] == limit
    assert pagination["page_count"] == get_pagination_page_count(host, limit)
    assert pagination["record_count"] == get_host_record_count(host)
