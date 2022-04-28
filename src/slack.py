import urllib3
import json

class Slack:
    def __init__(self, url: str, debug=False):
        self.url = url
        self.debug = debug
        self.http = urllib3.PoolManager()

    def error(self, message, text=""):
        if self.debug:
            print(f"[DEBUG] skip send message: Error - {message}")
            return
        print(f"[DEBUG] send message: Error - {message}")
        data = self.template_error(message, text)
        res = self.http.request('POST', self.url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))

    def info(self, message):
        if self.debug:
            print(f"[DEBUG] skip send message: Info - {message}")
            return
        print(f"[DEBUG] send message: Info - {message}")
        data = self.template_info(message)
        res = self.http.request('POST', self.url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))

    def send(self, apartment):
        if self.debug:
            print(f"[DEBUG] {vars(apartment)}")
            return 
        data = self.template_send(apartment)
        res = self.http.request('POST', self.url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))

    def template_send(self, apartment):
        map_address = apartment.address.replace(" ", "+")
        return {
    "text": f"Warm {apartment.price} | {apartment.space} | {apartment.room} | {apartment.address}",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Warm {apartment.price} | {apartment.space} | {apartment.room}*\n\n{apartment.title} - <https://www.immobilienscout24.de/expose/{apartment.apartment_id}#/| Web>"
			},
			"accessory": {
				"type": "image",
				"image_url": f"{apartment.photo}",
				"alt_text": f"{apartment.title}"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "mrkdwn",
					"text": f":round_pushpin: <https://www.google.com/maps/place/{map_address}|{apartment.address}>"
				}
			]
		}
	]
}

    def template_error(self, message: str, text: str):
        return {
            "attachments": [{
                "color": "#f4613d",
                "fallback": message,
                "text": f"{text}\n```[Error] {message}```"
            }]
        }

    def template_info(self, message: str):
        return {
            "attachments": [{
                "color": "#cccccc",
                "fallback": message,
                "text": "[Info] " + message
            }]
        }
