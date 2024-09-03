"""
This module provides a Flask REST API for analyzing system-generated security logs.
The API exposes two endpoints to assist clients in identifying and mitigating potential
vulnerabilities.
    - The first endpoint returns the top 10 most critical vulnerabilities
     for a specific host.
    - The second endpoint returns all vulnerabilities in alphabetical order
     for a specific host. Additionally, this API supports pagination.
"""

import pandas as pd
from flask import Flask, jsonify, request, abort, Response

app = Flask(__name__)

# Caching the data to prevent inefficiency in reading the same data every time when the api is called
# To avoid using global variables, in production the data can be stored in a system specific cache.
df = pd.read_csv("vulnerabilities(fixed).csv")


@app.route("/hosts/<string:host>/ten-riskiest-vulnerabilities", methods=["GET"])
def ten_riskiest_vulnerabilities(host: str) -> Response:
    """
    This endpoint returns 10 most risky vulnerabilities for a specific host
    Path parameter:
        host (str): IP address of the host
    Returns:
        Response: A response object containing the list of the ten most risky vulnerabilities
                  for the specified host
    Raises:
        404: The specified host is not found in the report file
    """
    host_df = (
        df[df["source"] == host].sort_values("risk_score", ascending=False).head(10)
    )
    count = host_df.shape[0]
    if count == 0:
        abort(404, "Host is not found.")

    response = jsonify(data=host_df.to_dict(orient="records"))
    return response


@app.route(
    "/hosts/<string:host>/sorted-vulnerabilities/", methods=["GET"]
)
def get_alphabetically_sorted_vulnerabilities(host: str) -> Response:
    """
    Path parameter:
        host (str): IP address of the host
    Query parameters:
        page (int): The starting page of the search
        limit (int): The maximum number of records returned on each page
    Returns:
        Response:   A response object containing all alphabetically ordered
                    vulnerabilities for the specified host, as well as
                    pagination information.
    Raises:
        404:
            - The specified host is not found in the report file
            - The offset, calculated as (page-1) * limit, is larger or equal than
              the number of records (vulnerabilities)
            - The page parameter is invalid
            - The limit parameter is invalid
    """
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)
    start = (page - 1) * limit
    end = start + limit

    host_df = df[df["source"] == host].sort_values("vulnerability", ascending=True)
    record_count = host_df.shape[0]

    if record_count == 0:
        abort(404, "Host is not found")
    if record_count <= start:
        abort(
            404,
            f"Invalid offset parameter. The offset {(page - 1)* limit}, calculated\
             as (page - 1)* limit, is larger or equal than the number of records {record_count}.",
        )
    if page < 0:
        abort(404, "Invalid page parameter.")
    if limit < 0:
        abort(404, "Invalid limit parameter.")

    paginated_host_df = host_df[start:end]
    page_count = (
        record_count // limit
        if (record_count % limit == 0)
        else (record_count // limit + 1)
    )
    pagination_info = {
        "page": page,
        "limit": limit,
        "record_count": record_count,
        "page_count": page_count,
    }
    response = jsonify(
        data=paginated_host_df.to_dict(orient="records"), pagination=pagination_info
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
