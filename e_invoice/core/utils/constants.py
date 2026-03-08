"""Global constants and configuration values for the e-invoice service."""

from core.utils.json_handler import load_json

ENDPOINTS = load_json(json_file="factus_api/config/endpoints.json")

CODE_TABLES = load_json(json_file="factus_api/config/code_tables.json")
