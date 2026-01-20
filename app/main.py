def get_property(prop: str) -> str | bool:
    if prop == "line_number":
        return "line"
    if prop == "column_number":
        return "column"
    if prop == "text":
        return "message"
    if prop == "code":
        return "name"
    return "source"


def format_linter_error(error: dict) -> dict:
    return {**{get_property(key): value for key,
            value in error.items() if get_property(key)},
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "failed" if len(errors) else "passed"}


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, value) for key,
            value in linter_report.items()]
