import requests
import pandas as pd
import os

# Dictionary of scheme names and AMFI codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Create output directory
os.makedirs("data/raw", exist_ok=True)

print("=" * 70)
print("Fetching Live NAV Data for 5 Mutual Fund Schemes")
print("=" * 70)

for scheme_name, amfi_code in schemes.items():

    print(f"\nFetching {scheme_name} ({amfi_code})...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data["data"])

            filename = f"data/raw/{scheme_name}_NAV.csv"

            df.to_csv(filename, index=False)

            print("✓ Success")
            print("Scheme:", data["meta"]["scheme_name"])
            print("Records:", len(df))
            print("Saved:", filename)

        else:
            print(f"✗ Failed (Status Code: {response.status_code})")

    except Exception as e:
        print("Error:", e)

print("\n" + "=" * 70)
print("All NAV files downloaded successfully!")
print("=" * 70)