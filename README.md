# Python Scraper

## Description

The Python Scraper project aims to scrape product data from an e-commerce website, store the data in a PostgreSQL database, and expose the data via a REST API. The project is built with Python, Django, PostgreSQL, and Scrapy.

## Objective

1. Web Scraping: Use a Scrapy spider to scrape product data (name, URL, price, and image) from an e-commerce website. At least 100 products should be scraped.
2. Database Setup: Store the scraped data in a PostgreSQL database with a table named product_data (columns: id, name, url, price, and image_url).
3. Django Application: Create a Django app that can trigger the Scrapy spider via a command-line interface and store the scraped data in the PostgreSQL database. The app also exposes a REST API endpoint (/products/) which supports pagination and retrieves data from the PostgreSQL database in JSON format.

## Requirements

- Python 3
- Postgres Database

## Installation

1. Clone the repository and navigate to the folder
    ```
    git clone *Add your git repository link here* && cd *Add your project folder here*
    ```

2. Activate your virtual environment
    ```
    source venv/bin/activate
    ```

3. Set up the required credentials in the .env file
    ```
    DATABASE_NAME=scrapwave
    DATABASE_USER=paul
    DATABASE_PASSWORD=
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

## Usage

1. Make migrations:
    ```
    python3 manage.py makemigrations
    ```
2. Apply migrations:
    ```
    python3 manage.py migrate
    ```
3. Navigate to the `/scrapwave/scraper/` directory
4. Run the scraper:
    ```
    python3 -m scrapy crawl properties
    ```

## API Endpoints

**/products/**

- Returns a paginated list of products in the PostgreSQL database.
- Use query parameters to navigate through pages (e.g., `/products/?page=2`).

## Contribution

For any changes, please open an issue first to discuss what you would like to change. 

## License

[MIT](https://choosealicense.com/licenses/mit/)
