def get_city_function(city, country, population=None):
    try:
        # Перетворюємо населення на числове значення, якщо воно передано
        population = int(population.replace(' ', '')) if population else None
    except ValueError:
        raise ValueError("Population must be a numeric value.")

    city = city.strip().title()
    country = country.strip().title()

    if population:
        formatted_city_country = f"{city}, {country} - population {population:,}"
    else:
        formatted_city_country = f"{city}, {country}."

    return formatted_city_country
