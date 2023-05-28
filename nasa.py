import requests
import csv

class NASAEarthDataScraper:
    def __init__(self):
        self.base_url = 'https://api.nasa.gov/planetary/apod'
        self.api_key = 'YOUR_API_KEY'  # Replace with your NASA API key

    def fetch_data(self):
        url = f'{self.base_url}?api_key={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data

    def save_to_csv(self, data):
        if data:
            keys = data[0].keys()
            filename = 'nasa_earth_data.csv'
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            print(f'Data saved to {filename}')
        else:
            print('No data to save')

if __name__ == '__main__':
    scraper = NASAEarthDataScraper()
    scraped_data = scraper.fetch_data()
    scraper.save_to_csv(scraped_data)
