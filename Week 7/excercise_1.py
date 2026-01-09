CATEGORY_DISCOUNTS = {
    "Electronics": 0.90,  
    "Clothing": 0.85,     
    "Books": 0.95,        
    "Home": 0.88          
}

TIER_DISCOUNTS = {
    "Premium": 0.95,     
    "Standard": 1.00,    
    "Budget": 0.98       
}

def readdata():
   products = []
    try:
        with open(r"Week 7\products.txt", "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    name, price, category, tier = line.strip().split(";")
                    products.append({
                        "name": name,
                        "price": float(price),
                        "category": category,
                        "tier": tier
                    })
                except ValueError as e:
                    print(f"Warnung: Zeile {line_num} konnte nicht verarbeitet werden: {e}")
                    continue
    except FileNotFoundError:
        print("Fehler: Die Datei 'Week 7\\products.txt' wurde nicht gefunden!")
        return []
    
    return products

def calculation(products):
    for product in products:
        original_price = product["price"]
        price = original_price
        
        if product["category"] in CATEGORY_DISCOUNTS:
            price *= CATEGORY_DISCOUNTS[product["category"]]
        
        if product["tier"] in TIER_DISCOUNTS:
            price *= TIER_DISCOUNTS[product["tier"]]
        
        product["final_price"] = round(price, 2)
        product["discount_percent"] = round((1 - price / original_price) * 100, 2)
    
    return products

def write_report(products):
    try:
        with open(r"Week 7\discount_report.txt", "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write("PRODUCT DISCOUNT REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            header = f"{'Product':<20} {'Category':<15} {'Tier':<10} {'Original':>10} {'Final':>10} {'Discount':>10}\n"
            f.write(header)
            f.write("-" * 80 + "\n")
            
            for p in products:
                line = (
                    f"{p['name']:<20} "
                    f"{p['category']:<15} "
                    f"{p['tier']:<10} "
                    f"{p['price']:>10.2f} € "
                    f"{p['final_price']:>9.2f} € "
                    f"{p['discount_percent']:>9.2f} %\n"
                )
                f.write(line)
        
        print("\nBericht wurde erfolgreich in 'Week 7\\discount_report.txt' gespeichert!")
    
    except Exception as e:
        print(f"Fehler beim Schreiben der Datei: {e}")

def print_summary(products):
    """Druckt eine Zusammenfassung auf der Konsole."""
    if not products:
        print("\nKeine Produkte zu verarbeiten.")
        return
    
    total_products = len(products)
    total_original = sum(p["price"] for p in products)
    total_final = sum(p["final_price"] for p in products)
    average_discount = round((1 - total_final / total_original) * 100, 2) if total_original > 0 else 0
    total_savings = round(total_original - total_final, 2)
    
    print("\n" + "=" * 80)
    print("ZUSAMMENFASSUNG")
    print("=" * 80)
    print(f"Anzahl verarbeiteter Produkte: {total_products}")
    print(f"Gesamtpreis (Original):        {total_original:.2f} €")
    print(f"Gesamtpreis (Final):           {total_final:.2f} €")
    print(f"Gesamtersparnis:               {total_savings:.2f} €")
    print(f"Durchschnittlicher Rabatt:     {average_discount:.2f} %")
    print("=" * 80 + "\n")

def main():
    print("Starte Produktverarbeitung...\n")
    
    products = readdata()
    
    if not products:
        print("Keine Produkte gefunden. Programm wird beendet.")
        return
    
    products = calculation(products)
    
    print("\n" + "=" * 80)
    print("PRODUKTLISTE MIT RABATTEN")
    print("=" * 80)
    print(f"{'Product':<20} {'Category':<15} {'Tier':<10} {'Original':>10} {'Final':>10} {'Discount':>10}")
    print("-" * 80)
    
    for p in products:
        print(
            f"{p['name']:<20} "
            f"{p['category']:<15} "
            f"{p['tier']:<10} "
            f"{p['price']:>10.2f} € "
            f"{p['final_price']:>9.2f} € "
            f"{p['discount_percent']:>9.2f} %"
        )
    
    write_report(products)
    
    print_summary(products)

if __name__ == "__main__":
    main()