import urllib3
import json

class Slack:
    def __init__(self, url: str, color: str, debug=False):
        self.url = url
        self.color = color
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

    def send(self, property_class):
        if self.debug:
            print(f"[DEBUG] {vars(property_class)}")
            return 
        data = self.template_send(property_class)
        res = self.http.request('POST', self.url, headers={'Content-Type': 'application/json'}, body=json.dumps(data))

    def template_send(self, property_class):
        map_address = property_class.address.replace(" ", "+")
        message = f"Warm {property_class.price} | {property_class.space} | {property_class.room} | {property_class.address}"
        return {
          "attachments": [{
            "color": self.color,
            "fallback": message,
            "blocks": [
              {
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": f"*Warm {property_class.price} | {property_class.space} | {property_class.room}*\n\n{property_class.title} - <https://www.immobilienscout24.de/expose/{property_class.property_id}#/| Web>"
                },
                "accessory": {
                  "type": "image",
                  "image_url": f"{property_class.photo}",
                  "alt_text": f"{property_class.title}"
                }
              },
              {
                "type": "context",
                "elements": [
                  {
                    "type": "mrkdwn",
                    "text": f":round_pushpin: <https://www.google.com/maps/place/{map_address}|{property_class.address}>"
                  }
                ]
              }
            ]
          }]
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
