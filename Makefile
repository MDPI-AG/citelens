
.PHONY: install_pre_commit
install_pre_commit:  ## configure and install pre commit tool
	uv run pre-commit install --overwrite --install-hooks -t pre-push -t pre-commit

.PHONY: uninstall_pre_commit
uninstall_pre_commit:  ## configure and install pre commit tool
	uv run pre-commit uninstall

.PHONY: lock
lock:  ## Lock the project dependencies
	uv lock

.PHONY: install
install:  ## Install the project and it's development dependencies
	uv sync --all-extras

.PHONY: ruff
ruff:  ## Run ruff linter
	uv run ruff check .

.PHONY: deptry
deptry:  ## Run deptry dependency checker
	uv run deptry .

.PHONY: test
test:  ## Run unittests with pytest
	uv run pytest


.PHONY: check
check: test ruff deptry ## Run all checks

.PHONY: help
help: ## Ask for help in the Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
