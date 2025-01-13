from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
import socket
import os


def health_check(request):
    # Check database connectivity
    try:
        db_conn = connections["default"]
        db_conn.cursor()  # Try to get a cursor to check if the DB is up
        db_status = "Database is up"
    except OperationalError:
        db_status = "Database is down"

    # Check server (basic check: attempt to resolve server itself)
    try:
        server_status = "Server is up"
        db_host = os.getenv("DB_HOST")
        server_port = os.getenv("SERVER_PORT")
        socket.create_connection(
            (db_host, server_port), timeout=5
        )  # Try connecting to server on port 80
    except socket.error:
        server_status = "Server is down"

    # Return a JSON response with the status of both components
    return JsonResponse(
        {
            "status": "ok",
            "database": db_status,
            "server": server_status,
        }
    )
