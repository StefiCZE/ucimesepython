def main():
    třídy = [
    {"Označení": "IT1A", "Počet žáků": 17},
    {"Označení": "IT1B", "Počet žáků": 16},
    {"Označení": "IT2A", "Počet žáků": 17},
    {"Označení": "IT2B", "Počet žáků": 17},
    {"Označení": "IT3", "Počet žáků": 13},
    {"Označení": "IT4", "Počet žáků": 14},
]
for třída in třídy:
    print("-------------------------------")
    print(f"Označení: {třída["Označení"]}")
    print(f"počet žáků: {třída["Počet žáků"]}")
    print("-------------------------------")
if(__name__== "__main__"):
    main()