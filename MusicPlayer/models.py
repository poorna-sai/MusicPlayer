from django.db import models

# Create your models here.
LastFolderId = 0
class Song(models.Model):
    Song_name = models.CharField(max_length=255)
    audio_file = models.FileField(blank =False  , upload_to='songs/')
    Folder_Id = models.IntegerField(default = 0)
    

class Folder(models.Model):
    FolderName = models.CharField(max_length =225 , blank = False , default="UnKnown Album")
    def __int__(self):
        return self.id




