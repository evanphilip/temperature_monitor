# Temperature Monitor
A systemd service which uploads the CPU temperature to a Google Spreadsheet at a specified frequency. I use it to keep an eye on the temperature of my Pi-hole.

1. It requires a Google Service Account, which is not considered best practice. However, I am unable to download the token required to use a OAuth 2.0 Client ID on my Raspberry Pi so I am resorting to this. 
2. Once the Google Service Account is created, the desired Google Spreadsheet has to be shared with the email ID of the Service Account. 
3. A JSON private key has to be created and downloaded for the Google Service Account. The path to this JSON file has to be set in the systemd service unit configuration by setting the environment variable GOOGLE_APPLICATION_CREDENTIALS.
4. The temperature.service file can be used to create a systemd service that starts on boot. 
5. You can use the Google Spreadsheet [here](https://docs.google.com/spreadsheets/d/1YtQ3_Wx4KqyIQyJsfG8nBcuaCFNSrYwiIAtdfDYUL34/edit?usp=sharing) to visualize your data. Don't forget to share the copy you make with your Google Service Account and update the SPREADSHEET_ID in monitor.py.
