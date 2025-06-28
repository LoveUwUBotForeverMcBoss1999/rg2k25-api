from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def load_response_data():
    """Load data from response.json file"""
    try:
        with open('response.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return default data if file doesn't exist
        return {
            "download_link": "https://download1500.mediafire.com/5iruh2bba3jgKzWIABXolouVQ3wiNzoMhZZtUj3bmXukGKSfiB0rJZ0ZMN9V1f2MiIEbYtIlmq4n5htf_G-mZtzsY_sxaK7EjS3peasBsxX9frGY9TDhweo3Et0I_dF5Hmp2d8s-ZbZFO5qt_T-s5IP6-xoaJp_cIieqPFAxPLIVhzc/adb8dk4a3uk5m1x/23-06+RG2K25+ModPack.zip",
            "name": "RG2K25 Battle Royal Server Up to date ModPack",
            "version": "2.9",
            "updated_date": "2025-06-29",
            "ip": "rg2k25.mcboss.top"
        }

@app.route('/rg2k24/api/download', methods=['GET'])
def get_download_info():
    """API endpoint to get download information"""
    try:
        data = load_response_data()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "Failed to load data", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "API is running"}), 200

@app.route('/', methods=['GET'])
def root():
    """Root endpoint with API info"""
    return jsonify({
        "message": "RG2K24 API",
        "version": "1.0",
        "endpoints": {
            "/rg2k24/api/download": "GET - Download information",
            "/health": "GET - Health check"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))