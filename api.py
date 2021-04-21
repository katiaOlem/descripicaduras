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
          key="aa2111f0-a266-11eb-8dd7-7bf9ce57255263cd7076-2980-48cd-8569-8856be70a56e"
          url="https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"
          response = requests.get(url, params={ "data" : texto})
          if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
            label = topMatch["class_name"]
            confidence = topMatch["confidence"]
            data = {}
            data["resultado: "] = label
            data["confianza: "] = confidence
            result = json.dumps(data)
            return result       
          else:
            response.raise_for_status()
        except:
          data = {}
          data["mensaje"] = "**No reconocido**"
          return json.dumps(data)

if __name__ == "__main__":
    app.run()