serve:
	uv run mkdocs serve

freeze:
	uv pip freeze > requirements.txt
