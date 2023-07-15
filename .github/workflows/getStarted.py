name: Hello World Workflow

on:
  push:
    branches:
      - main  # Adjust the branch name as per your repository's default branch

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.1 # Specify the Python version you want to use

    - name: Run Python script
      run: python print.py  # Replace 'your_script.py' with the actual filename

