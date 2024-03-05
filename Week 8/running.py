def most_popular(company_to_placements: dict[str, list[int]]) -> list[str]:
    """Return the company (or companies) with the most placements in the race
    according to company_to_placements.
    
    Precondition: company_to_placements is not empty
    """

    result = []
    most_placements = 0
    
    for company in company_to_placements:
        if len(company_to_placements[company]) > most_placements:
            most_placements = len(company_to_placements[company])

    for company in company_to_placements:
        if len(company_to_placements[company]) == most_placements:
            result.append(company)
    
    return result
