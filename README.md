## Project background

Tests were created for academic classes, the goal was to test chosen web application using Selenium Webdriver in Python.

## Usage

To run the script you will need the **geckodriver** on your system PATH and python enviorment with selenium installed.

```
pip install -U selenium
```

## Test coverage

My tests check following assertions:

- If my name is set up correctly,
- if I have more than 5 followers (popularity check),
- if Java is the most frequent language for my public repos (java dominance check), 
- if I've commited more than 5 times in last week (lazyness check).