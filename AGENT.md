# Directory Overview

This directory contains a collection of images and data related to various payment cards, primarily from US-based financial institutions. The collection is organized by card issuer, with each issuer having its own directory. Within each issuer's directory, there are subdirectories for different card types (e.g., Credit Card, Debit Card) and categories (e.g., Personal, Business).

The primary purpose of this repository is to serve as a visual and data library for payment cards. It includes:

-   **Card Images:** A vast collection of credit, debit, and gift card images.
-   **Card Benefits Data:** An Excel file (`docs/card benefit.xlsx`) that contains detailed information about card benefits, sign-up bonuses, earning rates, and fees.
-   **Documentation:** `README.md` files within each issuer's directory provide a quick-glance view of the card images available for that issuer.

# Key Files

-   `docs/card benefit.xlsx`: An Excel spreadsheet containing structured data on various credit card benefits. This is the main data source in the repository.
-   `read_excel.py`: A Python script that reads the `card benefit.xlsx` file and can be used to convert it into other formats (e.g., JSON). This script is useful for data processing and integration.
-   `**/README.md`: Markdown files that act as visual catalogs for the card images within their respective directories.

# Usage

This directory is intended for:

-   **Reference:** Looking up information about different payment cards, their appearance, and their benefits.
-   **Data Source:** Using the `card benefit.xlsx` file as a data source for applications or analysis related to credit card rewards and features.
-   **Asset Library:** Utilizing the card images for projects that require visuals of payment cards.

To work with the data in this repository, you can:

-   **View Card Images:** Browse the directories and `README.md` files to find and view card images.
-   **Analyze Card Benefits:** Open the `docs/card benefit.xlsx` file in a spreadsheet application or use the `read_excel.py` script to process the data programmatically. To use the script, you will need to have Python and the `pandas` library installed. You can install `pandas` using pip:
    ```
    pip install pandas
    ```
    Then, run the script:
    ```
    python read_excel.py
    ```
