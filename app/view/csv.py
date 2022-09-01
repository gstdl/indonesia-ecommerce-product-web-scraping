def to_response(row_count: int, output_file: str):
    return {
        "message": "Scraping successful",
        "output_file": output_file,
        "number_of_rows_written": row_count,
    }
