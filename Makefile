# Pet-Friendly Campsites Israel - Makefile

.PHONY: help install install-dev run clean test lint format docs

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  run          Run the campsite collector"
	@echo "  clean        Clean up temporary files"
	@echo "  test         Run tests"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  docs         Generate documentation"

# Install production dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements-dev.txt

# Run the main application
run:
	python main.py

# Clean up temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/

# Run tests
test:
	pytest tests/ -v

# Run linting
lint:
	flake8 main.py
	mypy main.py --ignore-missing-imports

# Format code
format:
	black main.py
	isort main.py

# Generate documentation
docs:
	sphinx-build -b html docs/ docs/_build/

# Setup virtual environment
venv:
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate  # On Linux/Mac"
	@echo "  venv\\Scripts\\activate     # On Windows"

# Full setup for new users
setup: venv install
	@echo "Setup complete! Don't forget to activate your virtual environment."
