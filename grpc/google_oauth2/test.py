import google.oauth2.service_account
from googleapiclient.discovery import build

def get_credentials():

    secret_data = {} # google cloud secret key

    # google cloud project_id
    project_id = secret_data['project_id']

    # google gloud get Credentials
    credentials = google.oauth2.service_account.Credentials.from_service_account_info(secret_data)
    # Google API를 사용하기 위한 클라이언트 객체를 생성
    google_client = build('oauth2', 'v2', credentials=credentials)

    print(project_id)
    print(credentials)
    print(google_client)


if __name__ == '__main__':
    get_credentials()