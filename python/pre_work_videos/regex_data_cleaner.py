"""extract and clean messy records."""

import re

# Sample data from the assignment
records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]


def extract_names(records):
    """Find the name after 'Name:' in every record."""
    names = []
    for record in records:
        match = re.search(r"Name:\s*([^|]+)", record)
        if match:
            names.append(match.group(1).strip())
    return names


def extract_emails(records):
    """Find email addresses, including addresses with multiple domain parts."""
    emails = []
    for record in records:
        match = re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", record)
        if match:
            emails.append(match.group())
    return emails


def normalize_phones(records):
    """Change different US phone formats into XXX-XXX-XXXX."""
    phones = []
    for record in records:
        # Get only the Phone field, before the next | character.
        match = re.search(r"Phone:\s*([^|]+)", record)
        if match:
            digits = re.sub(r"\D", "", match.group(1))  # Remove non-digits.
            if len(digits) == 10:
                phones.append(f"{digits[:3]}-{digits[3:6]}-{digits[6:]}")
    return phones


def extract_dates(records):
    """Find MM/DD/YYYY, MM-DD-YYYY, and YYYY/MM/DD dates as written."""
    dates = []
    date_pattern = r"\b(?:\d{4}/\d{2}/\d{2}|\d{2}[/-]\d{2}[/-]\d{4})\b"
    for record in records:
        match = re.search(r"Joined:\s*(" + date_pattern + r")", record)
        if match:
            dates.append(match.group(1))
    return dates


def parse_records(records):
    """Bonus: put each complete record into its own dictionary."""
    parsed = []
    for record in records:
        names = extract_names([record])
        emails = extract_emails([record])
        phones = normalize_phones([record])
        dates = extract_dates([record])
        if names and emails and phones and dates:
            parsed.append({
                "name": names[0],
                "email": emails[0],
                "phone": phones[0],
                "joined": dates[0],
            })
    return parsed


if __name__ == "__main__":
    print("Names:", extract_names(records))
    print("Emails:", extract_emails(records))
    print("Normalized phones:", normalize_phones(records))
    print("Dates:", extract_dates(records))
    print("\nParsed records (bonus):")
    for item in parse_records(records):
        print(item)

    # Check that all four functions return the expected results.
    assert extract_names(records) == ["Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince"]
    assert extract_emails(records) == [
        "alice.j@gmail.com", "bob_smith@yahoo.com",
        "charlie@outlook.com", "diana.prince@company.co.uk",
    ]
    assert normalize_phones(records) == [
        "555-123-4567", "555-987-6543", "555-111-2222", "555-444-3333",
    ]
    assert extract_dates(records) == ["01/15/2023", "03-22-2023", "2023/07/01", "11/30/2023"]
    assert len(parse_records(records)) == 4
    print("\nAll tests passed!")
