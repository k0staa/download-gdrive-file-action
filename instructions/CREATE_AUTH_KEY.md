## Create authentication keys for the service account and download it as `json` file

1. Click button marked in red and then
   choose "APIs and services" and "Enabled APIs and services"
   . ![Google Cloud Platform navigation](5.png "Google Cloud Platform navigation")
2. Click on the newly created service account
   . ![Service account list](14.png "Service account list")
3. Click tab pointed by mouse "KEYS"
   . ![Service account details](15.png "Service account details")
4. Click "ADD KEY" button and then "Create new key" option
   . ![Service account keys](16.png "Service account keys")
5. Choose "JSON" key type and click "CREATE"
   . ![Create service account key](17.png "Create service account key")
6. JSON file with kye will be automatically downloaded to your computer
   . ![Google Cloud Platform navigation](18.png "Google Cloud Platform navigation")
7. In the repository when you will use "Simple Download Google Drive file" action you have to create a new secret with
   the content of JSON file that you just created.
    1. On GitHub, navigate to the main page of the repository.
    2. Under your repository name, click on the "Settings" tab.
    3. In the left sidebar, click "Secrets".
    4. On the right bar, click on "Add a new secret"
       ![Create repository secret](create-secret.png)
    5. Type `SERVICE_ACCOUNT_KEY_JSON` as a name for your secret in the "Name" input box.
    6. Paste content of JSON file as "Value".
    7. Click "Add secret" to finish this procedure.
       ![Add new secret](Add-secret-name-value.png)

Authentication key and secret are created now. Follow next instructions. 
