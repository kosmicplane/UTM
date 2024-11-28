import requests

url = "https://services.sentinel-hub.com/api/v1/statistics"
headers = {
  "Authorization": "Bearer eyJraWQiOiJzaCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiZTYwMDYxNi1iZjFkLTRhMmItYjhiYi0xMmQwNzQxNzYwNzYiLCJhdWQiOiIwZjYxZDM4NS01YzhiLTQ0ZjktYTE1NC0yYWRmNTFkNTAxNDEiLCJqdGkiOiIzMWZkZWU2OS00NTcwLTRkZTgtYjFmYy0zMTA3MDcxMGI5M2UiLCJleHAiOjE2OTI3NTMzMTEsIm5hbWUiOiJKdWFuICBiZXJvbiIsImVtYWlsIjoiamViYWVyb3NAZ21haWwuY29tIiwiZ2l2ZW5fbmFtZSI6Ikp1YW4gIiwiZmFtaWx5X25hbWUiOiJiZXJvbiIsInNpZCI6IjkwZjQ5ZDgyLWQ5NGYtNGMwNi1hNzVmLWQ0NzZjMmU2MWYxNyIsImRpZCI6MSwiYWlkIjoiMjE0ZDJlNjEtOTYzZC00ZjhlLWE3ZTQtODcyM2Y5ZWVmZjIwIiwiZCI6eyIxIjp7InJhIjp7InJhZyI6MX0sInQiOjExMDAwfX19.h3-7CD40fGrDSyGgBwBGKeTAHK1tpZIqUlvf3kO3HXAwWiF26Zo9F0Izj_UgW993RqHnSFfAVNyB4Q1vD3v_LpiEsoNSyPkAS0f4-lVTH1y0lpKF_W2NDthkEGwVqlTSE_wRnYHLqFGxAo_xcge0EnsmHj_19h2fslnBicxp7QHQgM6EmmvXg8mjRwI1nlL--ReKLq0hqrZYh3zdfMWTz3Zrlvi7FgVZgDXyWNKqo2HKEOOZCyoOm2Yo0pdiqUR0zS1LvOxYojWINH3HmRRIOR-D5L-XR1_O_df42xPrTyBhV6VaP5SWVuLV7wc1vyoK4LiDlIeXu1KVzA6SU6cmiA",
  "Accept": "application/json",
  "Content-Type": "application/json"
}
data = {
  "input": {
    "bounds": {
      "bbox": [
        12.44693,
        41.870072,
        12.541001,
        41.917096
      ]
    },
    "data": [
      {
        "dataFilter": {},
        "type": "sentinel-2-l2a"
      }
    ]
  },
  "aggregation": {
    "timeRange": {
      "from": "2023-04-22T00:00:00Z",
      "to": "2023-08-22T23:59:59Z"
    },
    "aggregationInterval": {
      "of": "P10D"
    },
    "width": 512,
    "height": 343.697,
    "evalscript": "//VERSION=3\nfunction setup() {\n  return {\n    input: [{\n      bands: [\n        \"B04\",\n        \"B08\",\n        \"SCL\",\n        \"dataMask\"\n      ]\n    }],\n    output: [\n      {\n        id: \"data\",\n        bands: 3\n      },\n      {\n        id: \"scl\",\n        sampleType: \"INT8\",\n        bands: 1\n      },\n      {\n        id: \"dataMask\",\n        bands: 1\n      }]\n  };\n}\n\nfunction evaluatePixel(samples) {\n    let index = (samples.B08 - samples.B04) / (samples.B08+samples.B04);\n    return {\n        data: [index, samples.B08, samples.B04],\n        dataMask: [samples.dataMask],\n        scl: [samples.SCL]\n    };\n}\n"
  },
  "calculations": {
    "default": {}
  }
}

response = requests.post(url, headers=headers, json=data)
response = response.json()
print(response)