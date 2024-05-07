import base64
import requests

def generateImages(keywords, engine_id, api_host, api_key):
    images = {}
    for keyword_info in keywords:
        scene = keyword_info["scene"]
        prompt = keyword_info["keyword"]
        response = requests.post(
            f"{api_host}/v1/generation/{engine_id}/text-to-image",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {api_key}"
            },
            json={
                "text_prompts": [
                    {
                        "text": f"Dark nighty mystery, Realistic animated with suspense vibe. Keyword: {prompt}"
                    }
                ],
                "cfg_scale": 7,
                "height": 1536,
                "width": 1024,
                "samples": 1,
                "steps": 30,
            },
        )

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        for j, image in enumerate(data["artifacts"]):
            # Use the scene number to create a unique filename for each image
            filename = f"./assets/temp/images/scene_{scene}.png"
            with open(filename, "wb") as f:
                f.write(base64.b64decode(image["base64"]))
            images[scene] = filename
    return images