import re

def detect_financial_pii(text):
    """
    Detects bank account numbers, credit card numbers, and common transaction ID formats 
    in a given text using regular expressions.

    Args:
        text (str): The input or output text from the LLM.

    Returns:
        dict: A dictionary containing the types of PII found and their matches.
    """
    pii_found = {}

    # 1. Credit Card Numbers (13-19 digits, with optional spaces/dashes)
    # This regex is generic and might have false positives, but is a starting point.
    # More specific regex can target card types (Visa, MasterCard, Amex etc.).
    cc_pattern = r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12}|\d{13,19})\b'
    # Adding flexibility for spaces/dashes within the number for detection purposes
    cc_flexible_pattern = r'\b(?:\d[ -]*?){13,19}\b' 
    
    # 2. Bank Account Numbers (typically 9-18 digits, highly variable by country/bank)
    # This is a very generic pattern. Real world usage needs country specific patterns.
    bank_account_pattern = r'\b[0-9]{9,18}\b' 

    # 3. Transaction Information (very context dependent, example for a generic format: date, amount, description)
    # This example looks for a date followed by a description and an amount
    transaction_pattern = r'(\d{2}\s[a-z]{3}\s\d{4}|\d{2}/\d{2}/\d{4}).*?(\$\d+\.?\d*)'

    patterns = {
        "Credit Card": cc_flexible_pattern,
        "Bank Account": bank_account_pattern,
        "Transaction Info": transaction_pattern
    }

    for pii_type, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Flatten transaction info matches if they are tuples
            if pii_type == "Transaction Info":
                matches = [item for match_tuple in matches for item in match_tuple if item]
            pii_found[pii_type] = list(set(matches)) # Use set to avoid duplicates

    return pii_found

def guardrail(text):
    """
    Guardrail function to check for PII and redact it or flag the content.
    """
    detected_pii = detect_financial_pii(text)
    
    if detected_pii:
        print("--- PII Detected ---")
        for pii_type, items in detected_pii.items():
            print(f"{pii_type} found: {items}")
            # Redaction logic (simple replacement for demonstration)
            for item in items:
                text = text.replace(item, f"[REDACTED_{pii_type.upper()}]")
        print("--- Redacted Text ---")
        return text
    else:
        return text

# --- Example Usage ---
sample_input = "Please process the payment for transaction 01 Jan 2025 $150.75. The card number is 4111222233334444 and the account number is 1234567890. Thanks!"

processed_output = guardrail(sample_input)
print(processed_output)
