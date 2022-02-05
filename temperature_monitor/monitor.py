#!/usr/bin/env python3
if __name__ == '__main__':
    import time
    import systemd.daemon
    import datetime
    from googleapiclient.discovery import build
    import google.auth

    FREQUENCY = 10
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/cloud-platform']
    SPREADSHEET_ID = 'akdjhsflbasdfjhabsdffalhjdvalfjdhvafd'

    default_credentials, project_id = google.auth.default(scopes=SCOPES)
    service = build('sheets', 'v4', credentials=default_credentials)
    sheet = service.spreadsheets()

    systemd.daemon.notify('READY=1')

    while True:
        # read temperature
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            temp = f.read()
        resource = {"majorDimension": "COLUMNS", "values": [
            [datetime.datetime.now().isoformat()], [temp]]}
        # append the data in the spreadsheet, including a timestamp
        sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="RawData!A:Z",
                              insertDataOption="INSERT_ROWS", valueInputOption="USER_ENTERED", body=resource).execute()
        # wait 30 seconds before continuing
        time.sleep(FREQUENCY*60)
