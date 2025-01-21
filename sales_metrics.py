# sales_metrics.py
def calculate_daily_sales(sales):
   """
   Calculates the total sales for the day.
   :param sales: list of numerical sales values
   :return: total sales sum
   """
   return sum(sales)

if __name__ == "__main__":
   sample_sales = [100, 200, 150]
   print("Total Sales:", calculate_daily_sales(sample_sales))