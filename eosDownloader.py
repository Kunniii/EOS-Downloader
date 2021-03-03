import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service

class EOS_DOWNLOADER():
    def __init__(self, fileId, savedFileName):
        self.CLIENT_SECRET_FILE = 'D:\\Coding\\Py\\DriveAPI\\credentials.json'
        self.API_NAME = 'drive'
        self.API_VERSION = 'v3'
        self.SCPOES = ['https://www.googleapis.com/auth/drive']
        self.fileId = fileId
        self.savedFileName = savedFileName

    def launch(self):
        self.service = Create_Service(self.CLIENT_SECRET_FILE, self.API_NAME, self.API_VERSION, self.SCPOES)
        self.request = self.service.files().get_media(fileId=self.fileId)

        self.fh = io.BytesIO()
        self.downloader = MediaIoBaseDownload(fd=self.fh, request=self.request)
        self.status = self.downloader.next_chunk()[0].progress()
        self.fh.seek(0)

        with open(f"D:\\EOSs\\{self.savedFileName}", 'wb+') as self.f:
            self.f.write(self.fh.read())
        self.status = self.status == 1

if __name__ == "__main__":
    downloader = EOS_DOWNLOADER(fileId='15orxKbmGm4foV5Lpc0RYnz9Imvp3IbWF', savedFileName='EOS-Client.zip')
    downloader.launch()
    print(True) if downloader.status else print(False)