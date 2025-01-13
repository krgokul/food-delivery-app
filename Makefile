# Makefile for managing Django app creation and setup

# Default target
.PHONY: all

# Define the app name and directory as variables
APP_NAME ?= new_app
APP_DIRECTORY ?= food_delivery_app/apps

# Task to create a new Django app in the specified directory
.PHONY: create_app
create_app:
	@echo "Creating new Django app ✅: $(APP_NAME) in $(APP_DIRECTORY)"
	@mkdir -p $(APP_DIRECTORY)/$(APP_NAME)
	python manage.py startapp $(APP_NAME) $(APP_DIRECTORY)/$(APP_NAME)

migrate:
	python manage.py makemigrations
	python manage.py migrate

# Task to remove an app (this will delete the app folder and its contents)
.PHONY: remove_app
remove_app:
	@echo "Removing app ❌: $(APP_DIRECTORY)/$(APP_NAME)"
	rm -rf $(APP_DIRECTORY)/$(APP_NAME)