import os, json  # json for pretty output
from serpapi import GoogleSearch
import requests

num_pages = 1

def get_google_images(num_pages):
    for i in range(num_pages):
        print(f"Downloading images from page {i}...")
        params = {
            # "api_key": os.environ.get("SERPAPI_KEY"),
            "api_key": "YOUR_API_KEY",
            "engine": "google",
            "q": "small parking lot from above",
            "tbm": "isch",
            "ijn": i
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        # print(json.dumps(results['suggested_searches'], indent=2, ensure_ascii=False))
        # save files to /SerpApi_Images/ if it doesn't exist create the folder
        if not os.path.exists("./SerpApi_Images/"):
            os.makedirs("./SerpApi_Images/")

        # -----------------------
        # Downloading images
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

        for index, image in enumerate(results["images_results"]):

            try:
                print(f"Downloading {index} image...")

                # filepath is current working directory + SerpApi_Images + params["q"] + index + .jpg
                # changed the code to account for file naming conventions if run multiple times with different ijn
                filepath = os.path.join("./SerpApi_Images/", params["q"] + str(index) + "_" + str(params["ijn"]) +".jpg")
                
                response = requests.get(image['original'], headers=headers).content
                with open(filepath, "wb") as f:
                    f.write(response)

            except Exception as e:
                print(e)
                print(f"Error downloading {index} image. Error =", e)

    num_files = len(os.listdir("./SerpApi_Images/"))
    print(f"Collected {num_files} images") 

get_google_images(num_pages=num_pages)