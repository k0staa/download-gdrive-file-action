import io
import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def download_file() -> None:
    file_name = os.getenv("DOWNLOAD_FILE_NAME")
    file_id = _find_file_id(file_name)
    _download_file(file_id, file_name)


def _find_file_id(file_name: str) -> str:
    query = f"name = '{file_name}'"
    search_result = drive_service.files().list(q=query,
                                               pageSize=10, fields="nextPageToken, files(id, name)").execute()
    file_list = search_result.get('files', [])
    file_id = file_list[0].get('id')
    print("Found file with ID: %s" % file_id)
    return file_id


def _download_file(file_id: str, file_name: str) -> None:
    request = drive_service.files().get_media(fileId=file_id)
    output_file = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(output_file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    service_account_info = json.loads(os.getenv("SERVICE_ACCOUNT_KEY_JSON"))
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    drive_service = build('drive', 'v3', credentials=credentials)
    download_file()
