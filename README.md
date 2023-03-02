

* Use the Windows command prompt (cmd)
* Install python for windows from python.org

### Run on Windows cmd:
```
pip install -r requirements.txt
```

To run the program
```
python validate_results.py
```

# Create a Windows executable python script
```
pyinstaller --onefile --noconsole LIMS_results_validation.py
```
An `.exe` file will be generated inside the `dist` directory.

* Run tests on main functionality
```
pytest -s
```

# LIMS validation results
A tool for checking an excel file against another file to validate output results of genetic data from LIMS.
