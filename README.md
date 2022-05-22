# Google Drive Simple Download action

This action download file from Google Drive. It's simple and secure.

For instructions on how to set up service account required to download file,
see [How to create a project, service account and generate authentication key section](#How-to-create-a-project,-service-account-and-generate-authentication-key)

## Examples

```yaml
- name: Download file X from Google Drive to default (./) directory
  uses: k0staa/download-gdrive-file-action@v1
  with:
    service-account-auth-json: ${{ secrets.SERVICE_ACCOUNT_AUTH_JSON }}
    download-file-name: bmw.jpg
```

```yaml
- name: Download file X from Google Drive to ./out/ directory
  uses: k0staa/download-gdrive-file-action@v1
  with:
    service-account-auth-json: ${{ secrets.SERVICE_ACCOUNT_AUTH_JSON }}
    download-file-name: bmw.jpg
    download-to: ./out/
```

## Inputs

- `service-account-key-json` **Required** The credentials key of the service account that is allowed to download file
  from Google Drive account.

- `download-file-name` **Required** File name of the file that should be downloaded.

- `download-to` optional Download destination path. Default is the current directory.

## How to create a project, service account and generate authentication key

1. Create a project in the [Google Cloud Platform Console](https://console.cloud.google.com/)
   . [See instructions](instructions/CREATE_PROJECT.md)
2. Enable [Google Drive API](https://developers.google.com/drive/api/v3/enable-drive-api) in new project. [See instructions](instructions/ENABLE_API.md)
3. Create a service account for new project. [See instructions](instructions/CREATE_SERVICE_ACCOUNT.md)
4. Create authentication keys for the service account and download it as `json` file. [See instructions](instructions/CREATE_AUTH_KEY.md)
5. Share the file that you want to download to the service account. [See instructions](instructions/SHARE_FILE.md)

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
