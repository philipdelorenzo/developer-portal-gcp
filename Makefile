shell = ${SHELL}

# Meta-Goals
.PHONY: help
.DEFAULT_GOAL := help
#project := app
#entrypoint := app.py

default:
	echo 'Makefile default target!'

##@ Section 1: Local Build Commands
.PHONY: install
install: ## Install Unity Tree Development server
	$(info ******** Installing the Unity Tree Development Environment ********)
	@python -m venv .python
	@.python/bin/pip install -r requirements.txt

##@ Section 2: Local Run Commands
.PHONY: run
run: ## Run Unity Tree Services
	$(info ******** Running the Unity Tree Services ********)
	@.python/bin/python -m reflex run

##\@ Section 3: Kubernetes Environment Commands

##\@ Section 4: Dockerfile Build Commands

### Help Section
help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
