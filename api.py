import web
import requests
import json
urls = (
    '/picaduras?', 'Picaduras'
)
app = web.application(urls, globals())

class Picaduras():
    def GET(self):
        try:
          picaduras = web.input()
          texto=(picaduras["texto"])
          key="41bb8fa0-a270-11eb-a5d3-577120b8d016ac764cce-05bf-4ed5-98fb-84627ae6b761"
          url="https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"
          response = requests.get(url, params={ "data" : texto})
          if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            label = topMatch["class_name"]
            confidence = topMatch["confidence"]
            data = {}
            data["Tipo: "] = label
            data["%"] = confidence
            result = json.dumps(data)
            return result       
          else:
            response.raise_for_status()
        except:
          data = {}
          data["mensaje"] = "**SINTOMA NO RECONOCIDO**"
          return json.dumps(data)

if __name__ == "__main__":
    app.run()