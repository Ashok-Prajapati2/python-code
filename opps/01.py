from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def main():
    
    json_data = {
    "1": {
        "PartnerTag": "xyz-20",
        "PartnerType": "Associates",
        "ItemIds": ["8424916514"],
        "LanguagesOfPreference": ["es_US"]
    },
    "2": {
        "PartnerTag": "xyz-20",
        "PartnerType": "Associates",
        "ItemIds": ["8424916514"],
        "LanguagesOfPreference": ["es_US"]
    },
    "3": {
        "PartnerTag": "xyz-20",
        "PartnerType": "Associates",
        "ItemIds": ["8424916514"],
        "LanguagesOfPreference": ["es_US"]
    },
    "4": {
        "PartnerTag": "xyz-20",
        "PartnerType": "Associates",
        "ItemIds": ["8424916514"],
        "LanguagesOfPreference": ["es_US"]
    }
}

    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)
