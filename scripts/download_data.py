
import argparse
import csv
import json
from pathlib import Path

import requests


# --------------------------------------------------
# Configuration
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]

WHO_URL = "https://ghoapi.azureedge.net/api/NCD_PAA"

EUROSTAT_OBESITY_URL = (
    "https://ec.europa.eu/eurostat/api/dissemination/"
    "statistics/1.0/data/sdg_02_10"
)

EUROSTAT_GDP_URL = (
    "https://ec.europa.eu/eurostat/api/dissemination/"
    "statistics/1.0/data/nama_10_pc"
)

PAGE_SIZE = 1000
TIMEOUT = 60


# --------------------------------------------------
# Helper: download a file without overwriting it
# --------------------------------------------------

def should_download(path, force):
    if path.exists() and not force:
        print(f"SKIPPED: {path.relative_to(BASE_DIR)} already exists.")
        print("Use --force if you want to download it again.")
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    return True


# --------------------------------------------------
# Download WHO data with pagination
# --------------------------------------------------

def download_who(force=False):
    output_path = (
        BASE_DIR / "data" / "raw" / "who" / "who_physical_activity.csv"
    )

    if not should_download(output_path, force):
        return

    print("\nDownloading WHO physical activity data...")

    all_records = []
    skip = 0
    total_count = None

    while True:
        params = {
            "$top": PAGE_SIZE,
            "$skip": skip,
            "$count": "true"
        }

        response = requests.get(
            WHO_URL,
            params=params,
            timeout=TIMEOUT
        )
        response.raise_for_status()

        data = response.json()
        records = data.get("value", [])

        if total_count is None:
            total_count = data.get("@odata.count")
            print(f"Total records reported by WHO: {total_count}")

        if not records:
            break

        all_records.extend(records)

        skip += len(records)

        print(f"Downloaded {skip} records...")

        if total_count is not None and skip >= total_count:
            break

        if len(records) < PAGE_SIZE:
            break

    if not all_records:
        raise RuntimeError("WHO API returned no records.")

    if total_count is not None and len(all_records) != total_count:
        raise RuntimeError(
            f"Expected {total_count} WHO records, "
            f"but downloaded {len(all_records)}."
        )

    # Write all records to CSV
    fieldnames = list(all_records[0].keys())

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )
        writer.writeheader()
        writer.writerows(all_records)

    print(f"WHO download completed: {len(all_records)} records.")
    print(f"Saved to: {output_path}")


# --------------------------------------------------
# Download Eurostat JSON datasets
# --------------------------------------------------

def download_eurostat(url, params, output_path, force=False):
    if not should_download(output_path, force):
        return

    print(f"\nDownloading {output_path.name}...")

    response = requests.get(
        url,
        params=params,
        timeout=TIMEOUT
    )
    response.raise_for_status()

    # Validate that the response is JSON before saving
    data = response.json()

    if "value" not in data or "dimension" not in data:
        raise RuntimeError(
            f"Unexpected Eurostat response for {output_path.name}"
        )

    output_path.write_text(
        json.dumps(data, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Download completed: {len(data['value'])} observations.")
    print(f"Saved to: {output_path}")


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Download WHO and Eurostat project datasets."
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing raw datasets."
    )

    args = parser.parse_args()

    try:
        download_who(force=args.force)

        download_eurostat(
            url=EUROSTAT_OBESITY_URL,
            params={
                "lang": "EN",
                "time": "2022"
            },
            output_path=(
                BASE_DIR / "data" / "raw" /
                "eurostat" / "eurostat_obesity.json"
            ),
            force=args.force
        )

        download_eurostat(
            url=EUROSTAT_GDP_URL,
            params={
                "lang": "EN",
                "freq": "A",
                "unit": "CP_EUR_HAB",
                "na_item": "B1GQ",
                "time": "2022"
            },
            output_path=(
                BASE_DIR / "data" / "raw" /
                "eurostat" / "eurostat_gdp_2022.json"
            ),
            force=args.force
        )

        print("\nAll downloads completed.")

    except requests.RequestException as error:
        print(f"\nDownload failed: {error}")
        raise


if __name__ == "__main__":
    main()
