def filter_sales(sales, threshold=100):
    """
    Filters out sales below a given threshold.
    :param sales: list of numerical sales values
    :param threshold: minimum sale value to keep
    :return: filtered list of sales
    """
    return [sale for sale in sales if sale >= threshold]

if __name__ == "__main__":
    sample_sales = [50, 100, 200, 75, 150]
    filtered = filter_sales(sample_sales, threshold=100)
    print("Filtered Sales:", filtered)
    print("Total Filtered Sales:", calculate_daily_sales(filtered))
