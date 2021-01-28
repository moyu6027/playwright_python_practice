# playwright_python_practice
Just a [Playwright Python](https://github.com/Microsoft/playwright-python) tool practice

## How to run
1. Run tests `execute_tests.sh`

## Notes:
Pretty interesting and fast-growing tool for test automation. It can have some troubles with the first setup 
(especially with Docker), but generally this tool faster than Selenium and have pretty nice facade methods out of the box.

It's hard to say if I can recommend this tool to young Python AQA engineers because Selenium is a standard 
and supports by W3C. But if you have a small project, then it can be a wise choice to use Playwright.



## Docker
Execute tests - `docker-compose run tests`

Rebuild container - `docker-compose build --no-cache setup`