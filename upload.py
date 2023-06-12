# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.insert
# NOTES:
# 1. This sample code uploads a file and can't be executed via this interface.
#    To test this code, you must run it locally using your own API credentials.
#    See: https://developers.google.com/explorer-help/code-samples#python
# 2. This example makes a simple upload request. We recommend that you consider
#    using resumable uploads instead, particularly if you are transferring large
#    files or there's a high likelihood of a network interruption or other
#    transmission failure. To learn more about resumable uploads, see:
#    https://developers.google.com/api-client-library/python/guide/media_upload

import os

import googleapiclient.discovery

from googleapiclient.http import MediaFileUpload

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "" # Developer API Key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().insert(
        part="snippet,status",
        notifySubscribers=False,
        body={
          "snippet": {
            "categoryId": "22",
            "description": "Description of uploaded video.",
            "title": "Test video upload."
          },
          "status": {
            "privacyStatus": "private"
          }
        },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("C:\\Work\\Content\\Videos\\Steve Is Drowning.mp4")
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()