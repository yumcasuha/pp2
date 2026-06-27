import re
import json

def parse_receipt(text):
    prices = re.findall(r'\d+[.,]\d{2}', text)
    products = re.findall(r'\d+\.\s*(.+?)\n', text)
    datetime_info = re.findall(r'\d{2}[./-]\d{2}[./-]\d{4}\s+\d{2}:\d{2}', text)
    payment_method = re.findall(r'(Наличные|Карта|Cash|Card)', text, re.IGNORECASE)
    total = sum(float(p.replace(',', '.')) for p in prices)
    result = {
        "products": products,
        "prices": prices,
        "total": total,
        "datetime": datetime_info,
        "payment_method": payment_method
    }
    return result

if __name__ == "__main__":
    with open("raw.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    parsed = parse_receipt(raw_text)
    print(json.dumps(parsed, indent=4, ensure_ascii=False))
