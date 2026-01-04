import json
import re
import os

def get_card_details_strict(card_name_in_readme, issuer_name, card_benefits_data):
    """
    Searches for a card in the card_benefits_data and returns its details.
    Uses a stricter matching logic.
    """
    
    card_name_in_readme_lower = card_name_in_readme.lower()

    # Priority 1: Exact match of card name from README in the JSON card name, considering issuer
    for card in card_benefits_data:
        card_name_from_json = card['Card Name'].lower()
        if card_name_in_readme_lower in card_name_from_json and issuer_name.lower() in card_name_from_json:
            return card

    # Priority 2: Exact match of card name from README in the JSON card name, without issuer
    for card in card_benefits_data:
        card_name_from_json = card['Card Name'].lower()
        if card_name_in_readme_lower in card_name_from_json:
            return card

    return None

def format_card_details(details):
    """
    Formats the card details into a markdown string.
    """
    if not details:
        return ""
    
    details_str = "<ul>"
    for key, value in details.items():
        if key != "Card Name":
            details_str += f"<li><b>{key}:</b> {value}</li>"
    details_str += "</ul>"
    return details_str

def update_readme(readme_path, card_benefits_data):
    """
    Updates the README.md file with card details.
    """
    issuer_name = os.path.basename(os.path.dirname(readme_path))
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Regex to find card names in the markdown table
    card_name_regex = re.compile(r"(!\[(.*?)\]\(.*?\))\s*(.*?)\s*\|")

    def replace_func(match):
        image_md = match.group(1)
        card_name_in_readme = match.group(3).strip()
        
        card_details = get_card_details_strict(card_name_in_readme, issuer_name, card_benefits_data)
        
        if card_details:
            details_html = format_card_details(card_details)
            return f"{image_md}<br/>{card_name_in_readme}{details_html} |"
        else:
            return match.group(0)

    updated_readme_content = card_name_regex.sub(replace_func, readme_content)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_readme_content)
    print(f"Updated {readme_path}")

if __name__ == '__main__':
    with open('card_benefits.json', 'r', encoding='utf-8') as f:
        card_benefits = json.load(f)
    
    for issuer_dir in os.listdir('.'):
        if os.path.isdir(issuer_dir) and 'README.md' in os.listdir(issuer_dir):
            update_readme(os.path.join(issuer_dir, 'README.md'), card_benefits)
