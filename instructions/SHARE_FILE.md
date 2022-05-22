## Share the file that you want to download to the service account

The file that will be downloaded by GitHub workflow must be shared with the service account created in the previous
steps.

1. Click button marked in red and then
   choose "IAM and admin" and "Service account"
   . ![Google Cloud Platform navigation](19.png "Google Cloud Platform navigation")
2. Mark and copy the email name of service account.
   . ![Service account list](20.png "Service account list")
3. Go to your Google Drive where you keep file that will be downloaded in GitHub workflow. Click it with the right mouse
   button and click "Share".
   . ![Google Drive Share](21.png "Google Drive Share")
4. In the "Add people and group" input enter email of the service account that you copied in step 2.
   . ![Google Drive Share Add People and groups](22.png "Google Drive Share Add People and groups")
5. Choose "Viewer" role for the service account and click "Send"
   . ![Google Drive Share Role](23.png "Google Drive Share Role")

File is shared, and now you can download it using "Simple Download Google Drive file" action. 

