.PHONY: all run lint format help

# Default target executed when no arguments are given to make.
all: help

run:
	poetry run python llm_w_langchain $(APP)

lint:
	poetry run mypy .
	poetry run black . --check
	poetry run ruff .

format:
	poetry run black .
	poetry run ruff --select I --fix .

help:
	@echo '----'
	@echo 'run                          - run application'
	@echo 'lint                         - run linters'
	@echo 'format                       - run code formatters'

