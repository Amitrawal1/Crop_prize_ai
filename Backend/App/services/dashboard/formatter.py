def format_dashboard_response(data):

    if data["status"] != "success":

        return {
            "status": False,
            "message": data["message"],
            "records": [],
        }

    return {
        "status": True,
        "message": data["message"],
        "records": data["data"]["records"],
    }