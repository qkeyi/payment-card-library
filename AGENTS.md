# Directory Overview

This directory contains a collection of images and data related to various payment cards, primarily from US-based financial institutions. The collection is organized by card issuer, with each issuer having its own directory. Within each issuer's directory, there are subdirectories for different card types (e.g., Credit Card, Debit Card) and categories (e.g., Personal, Business).

The primary purpose of this repository is to serve as a visual and data library for payment cards. It includes:

-   **Card Images:** A vast collection of credit, debit, and gift card images.
-   **Documentation:** `README.md` files within each issuer's directory provide a quick-glance view of the card images available for that issuer.
-   **Serialization Data**: `benefits.json`, `cards.json`, `card_faces.json`, `issuers.json`, `template_cards.json`, `template_card_benefits.json`
    -   Fields are based on `schema.prisma`
-   `**/README.md`: Markdown files that act as visual catalogs for the card images within their respective directories.

# Usage

This directory is intended for:

-   **Reference:** Looking up information about different payment cards, their appearance, and their benefits.
-   **Asset Library:** Utilizing the card images for projects that require visuals of payment cards.

To work with the data in this repository, you can:

-   **View Card Images:** Browse the directories and `README.md` files to find and view card images.


# Instructions

## Add a template card
1. Add a new record into `card.json`
2. Add a reference in `template_cards.json`

## Add a benefit
1. Add a new record in `benefit.json`
2. Add a reference in `template_card_benefits.json`

## Add a card face
1. Add a new record in `card_faces.json`

