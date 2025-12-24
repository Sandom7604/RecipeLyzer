
# RecipeLyzer
## Video Demo: [the video demo](https://www.youtube.com/watch?v=aARbJnOWf18)


## Overview

RecipeLyzer is a Python-based recipe lookup application.
It provides multiple search methods for retrieving recipe information from an external API.

The project was developed as part of the **CS50P final assessment**, with a focus on API usage, input validation, and structured program flow.

---

## Functional Scope

The application supports the following operations:

* Recipe search by main ingredient
* Recipe search by recipe name
* Random recipe retrieval

All data is fetched dynamically at runtime.

---

## System Requirements

* Python 3.x
* Internet connectivity (required for API requests)

---

## Dependencies

* Python
* Flask (web interface)
* Requests (HTTP requests)
* HTML, CSS (frontend)

---

## Application Flow

1. User selects a search method.
2. Input is validated according to the selected method.
3. An HTTP request is sent to the API endpoint.
4. The API response is parsed from JSON.
5. Validated recipe data is rendered to the user.

---

## Error Handling

* Invalid search types are rejected.
* Empty or malformed input is handled safely.
* Network and API failures do not crash the application.
* Missing or unavailable recipe data is managed internally.

---

## Usage

1. Start the application.
2. Select one of the supported search modes.
3. Provide input where required.
4. View the resulting recipe information.

---

## Notes

> This application was created as the **Final Project for CS50’s Introduction to Programming with Python (CS50P)**.

> Recipe data is sourced from **TheMealDB API**.

> API responses depend on external availability and may vary.

---

## Limitations

* Requires an active internet connection.
* Limited to the data provided by the external API.
* Results depend on API accuracy and completeness.

---

## Summary

RecipeLyzer is a lightweight Python application demonstrating structured programming, API integration, and defensive input handling in accordance with CS50P guidelines.

# RecipeLyzer
