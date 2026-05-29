import requests


def find_city(city):
    url = "https://photon.komoot.io/api"

    params = {
        "q": city,
        "limit": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    """   print("STATUS:", response.status_code)
        print("RAW RESPONSE:")
        print(response.text[:300])  # first 300 chars"""

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    try:
        data = response.json()
    except Exception as e:
        return f"JSON error: {e}"

    if data.get("features"):
        props = data["features"][0]["properties"]

        city_name = props.get("name")
        country = props.get("country")

        return f"{city_name}, {country}"

    return "City not found"


