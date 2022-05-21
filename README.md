# Simple Download Google Drive file

This action download file from Google Drive. It's simple and secure.

For instructions on how to set up service account required to download file,
see [How to create a project, service account and generate authentication key section](#How-to-create-a-project,-service-account-and-generate-authentication-key)

## Example

```yaml
- name: Download file X from Google Drive
  uses: k0staa/download-gdrive-file-action@v1
  with:
    service-account-auth-json: ${{ secrets.SERVICE_ACCOUNT_AUTH_JSON }}
    download-file-name: /path/to/download
    download-to: ./

    # For those who set up Google Drive API client ID and secret themselves
    google-client-id: ${{ secrets.GOOGLE_CLIENT_ID }}
    google-client-secret: ${{ secrets.GOOGLE_CLIENT_SECRET }}
```

## Inputs

- `service-account-key-json` **Required** The credentials key of the service account that is allowed to download file
  from Google Drive account.

- `download-file-name` **Required** File name of the file that should be downloaded.

- `download-to` optional Download destination path. Default is the current directory.

## How to create a project, service account and generate authentication key

1. Create a project in the [Google Cloud Platform Console](https://console.cloud.google.com/)
2. Create a service account for this newproject
3. Create authentication keys for this new service account and download it as `json`
4. Enable [Google Drive API](https://developers.google.com/drive/api/v3/enable-drive-api) in new project
5. Share the file that you want to download to the service account

## Contribution

PRs are accepted. Contributions to the [roadmap](#roadmap) are also welcome!

If you are having trouble or feature
request, [post new issue](https://github.com/k0staa/download-gdrive-file-action/issues/new).

## Roadmap

- Support batch download
- Support file download using file_id
- Support file download from provided folder name

## Known issues

- If you share two files with the same name (different folders), the first one found will be downloaded.

## License

Check [LICENSE.md](LICENSE.md) file.
