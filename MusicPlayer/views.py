from django.shortcuts import render , redirect
from .models import *
# Create your views here.

def Home(request):
	All_Folders = Folder.objects.all()
	context = {
			'Folders': All_Folders
		}

	return render(request , 'Index.html' ,context)

def Upload_song(request):
	if request.method == 'POST':
		Song_name = request.POST.get('Song_name')
		audio_file = request.FILES.get('audio_file')
		Folder_Id = request.POST.get('Folder_Id')
		Folder_Name = request.POST.get('FolderName')
		if Folder_Id =="Create_new_Folder":
			Folder_Id = Folder(FolderName = Folder_Name)
			Folder_Id.save()
			Folder_Id = Folder_Id.id
			UploadData = Song(Song_name = Song_name , audio_file = audio_file , Folder_Id =Folder_Id)
			UploadData.save()
			return redirect('Home')
		elif Folder_Id!=0:
			UploadData = Song(Song_name = Song_name , audio_file = audio_file , Folder_Id =Folder_Id)
			UploadData.save()
			return redirect('Home')
		else:
			UploadData = Song(Song_name = Song_name   , audio_file = audio_file , Folder_Id =0)
			UploadData.save()
			return redirect('Home')

	else:
		All_Folders = Folder.objects.all()
		context = {
			'Folders': All_Folders
		}
		return render(request , 'Upload_Song.html' , context)

	return render(request , 'Upload_song.html')

def ViewFolder(request , pk):
	Songs = Song.objects.all().filter(Folder_Id = pk)
	Folder_Name = Folder.objects.get(id = pk)
	
	context  = {
		'key': Songs,
		'Folder_Name':Folder_Name.FolderName
	}
	return render(request , 'ViewSong.html' ,context)

def DeleteSong(request , pk):
	GetSong = Song.objects.all().filter(id = pk)
	Folder_Name = Folder.objects.get(id = pk)
	GetSong.delete()
	return redirect("Home")


