from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.imdb.com/search/name/")
        self.wait = WebDriverWait(self.driver, 10)

    def fill_search_form(self, search_query, gender, profession, sort_by):
        # Fill in the search query
        search_box = self.wait.until(EC.element_to_be_clickable((By.ID, "search-credit-name")))
        search_box.send_keys(search_query)

        # Select gender from drop-down menu
        gender_select = self.wait.until(EC.element_to_be_clickable((By.NAME, "gender")))
        gender_select.click()
        self.driver.find_element(By.XPATH, f"//option[text()='{gender}']").click()

        # Select profession from drop-down menu
        profession_select = self.wait.until(EC.element_to_be_clickable((By.NAME, "primary_profession")))
        profession_select.click()
        self.driver.find_element(By.XPATH, f"//option[text()='{profession}']").click()

        # Select sort by option from drop-down menu
        sort_by_select = self.wait.until(EC.element_to_be_clickable((By.NAME, "sort")))
        sort_by_select.click()
        self.driver.find_element(By.XPATH, f"//option[text()='{sort_by}']").click()

    def perform_search(self):
        # Click the Search button
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, "search-btn")))
        search_button.click()

        # Wait for the search results page to load (you may need to customize this)
        self.wait.until(EC.title_contains(self.driver.find_element(By.ID, "search-credit-name").get_attribute("value")))

        # Your further actions on the search results page can be added here

    def close_browser(self):
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    imdb_search = IMDbSearch()
    imdb_search.fill_search_form("Your Search Query", "male", "Actor", "Name")
    imdb_search.perform_search()
    imdb_search.close_browser()