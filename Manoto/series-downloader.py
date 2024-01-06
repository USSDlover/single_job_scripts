import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def extract_video_link(soup):
    """Extracts the video link from the given BeautifulSoup object."""

    try:
        # Customize this selector based on your website's structure
        video_element = soup.find("video", src=True)  # Find the video element with a "src" attribute
        if video_element:
            return video_element["src"]  # Extract the "src" attribute, which usually contains the video link
        else:
            print("Video element not found on the page.")
            return None

    except Exception as e:
        print("Error extracting video link:", e)
        return None


def extract_download_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    episode_title = soup.find("title").text.strip()
    print(f"Episode title: {episode_title}")

    # Find episode links (customize this based on your website's structure)
    episode_links = soup.find_all("a")

    print(f"Found Episode Links {len(episode_links)}")

    # Extract download links from each episode page
    download_links = []
    for episode_link in episode_links:
        episode_url = episode_link["href"]
        episode_response = requests.get(episode_url)
        episode_soup = BeautifulSoup(episode_response.content, "html.parser")

        # Customize this to find the download link element on your episode pages
        download_link = episode_soup.find("a", class_="button")
        if download_link:
            download_links.append(download_link["href"])
    print(f"Found Download Links {len(download_links)}")

    return download_links

def extract_download_links_driver(series_url):
    """Downloads all videos from the specified series page."""

    driver = webdriver.Chrome()  # Replace with your preferred browser driver
    driver.get(series_url)

    try:
        page_title = driver.title
        print(f"Page title: {page_title}")

        episode_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.Inner"))  # Adjust selector as needed
        )
        print(f"Found {len(episode_links)}")

        episode_download_links = []
        for episode_link in episode_links:
            # episode_download_links.append(episode_link["href"])
            print(f"Found Episode {episode_link}")
            print(f"Found Episode {episode_link.text.strip()}")
            episode_link.click()

            # try:
            #     download_link = WebDriverWait(driver, 10).until(
            #         EC.presence_of_element_located((By.CSS_SELECTOR, "a.button"))  # Adjust selector as needed
            #     )
            #     # download_link.click()
            #     # download_links.append(download_link["href"])
            #     print(download_link)
            #
            #     # Wait for download to start (optional)
            #     # ...
            #
            # except (TimeoutException, NoSuchElementException) as e:
            #     print(f"Error finding download link on episode page: {e}")
            #
            # driver.back()

        print(f"Found {len(episode_download_links)}")
        return episode_download_links

    except TimeoutException:
        print("Error loading series page or finding episode links.")

    finally:
        driver.quit()  # Close the browser


# Example usage
links = ["https://www.manototv.com/show/2342"]
download_links = []
for link in links:
    download_links.extend(extract_download_links_driver(link))

# Store the download links in a file
with open("download_links.txt", "w") as file:
    for link in download_links:
        file.write(link + "\n")

print("Download links extracted and saved to download_links.txt")
