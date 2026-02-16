"""
Lab 1 — Part 2 Starter (BUGGY ON PURPOSE)
API: Cat Facts — https://catfact.ninja/
Goal: Fetch ONE cat fact and save it to data/cat_fact.txt

❗ Your job: run this script, read the error(s), consult the docs linked above,
fix the bugs, and add brief comments explaining each fix.

Hints:
- Check the endpoint path (facts vs. fact)
- Verify keys in the JSON payload
- Ensure timeouts and types are correct
- Make sure files/directories exist before writing
- Double‑check typos in file names and variables
"""

# TODO: Import what you actually need (this line is intentionally incomplete)
import json
import requests             #imported requests to be able to use requests.get

API_URL = "https://catfact.ninja/fact"  # <-- Is this the correct endpoint for a single random fact?
#changed "facts" endpoint to "fact" to only get one fact

def get_cat_fact():
    """Fetch a single cat fact string from the API and return it."""
    # NOTE: There may be a few bugs below. Read errors carefully!
    resp = requests.get(API_URL, timeout=5)  # BUG: timeout type? also missing import above
    #changed timeout type to integer instead of string, fixed import request.
    data = resp.json()
    # Expecting the payload to contain the fact text at data["fact"]
    # (Verify with docs! If the endpoint returns a list, this will fail.)
    fact = data["fact"]
    #changed facts with fact

    return fact

def save_fact_to_file(text):
    """Save the provided text to data/cat_fact.txt"""
    out_path = "data/cat_fact.txt"
    # If the folder doesn't exist, this will fail.
    #Manually created the data folder, enabling the fact to be saved in a txt file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved to data/cat_fact.txt")  # BUG: filename typo

def main():
    fact = get_cat_fact()
    # Add a simple guard so we don't write None/empty strings
    if fact and isinstance(fact, str):
        save_fact_to_file(fact)
    else:
        print("No fact fetched. Check API response structure.")

if __name__ == "__main__":
    main()
