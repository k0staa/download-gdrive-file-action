import io
import json
import mimetypes
import os
import sys
from pathlib import Path

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
    if len(file_list) == 0:
        print("Can't find file: %s" % file_name)
        sys.exit(1)
    file_id = file_list[0].get('id')
    print("Found file with ID: %s" % file_id)
    return file_id


def _get_output_file_path(file_name: str) -> Path:
    chosen_path = os.getenv("DOWNLOAD_TO")
    mime_type = os.getenv("EXPORT_MEDIA_TYPE")
    download_directory = Path(chosen_path)
    download_directory.mkdir(parents=True, exist_ok=True)
    output_file_path = download_directory / file_name
    
    # add an appropriate extension if file_name does not
    # have an extension, and if we can guess the appropriate
    # extension
    if not output_file_path.suffix and mime_type:
        extension = mimetypes.guess_extension(mime_type)
        if extension:
            output_file_path = output_file_path.with_suffix(extension)

    return output_file_path


def _download_file(file_id: str, file_name: str) -> None:
    mime_type = os.getenv("EXPORT_MEDIA_TYPE")
    if mime_type:
        request = drive_service.files().export_media(
            fileId=file_id,
            mimeType=mime_type,
        )
    else:
        request = drive_service.files().get_media(fileId=file_id)
    output_path = _get_output_file_path(file_name)
    output_file_path = io.FileIO(output_path, 'w+b')
    downloader = MediaIoBaseDownload(output_file_path, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    service_account_info = json.loads(os.getenv("SERVICE_ACCOUNT_KEY_JSON"))
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    drive_service = build('drive', 'v3', credentials=credentials)
    download_file()
