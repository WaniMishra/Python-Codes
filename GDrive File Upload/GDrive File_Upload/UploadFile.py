from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
upload_file_list = ['new.txt']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1j8ih4nUP6tg_P_uHAttWa4p29SCMd6m2'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload(param={'supportsTeamDrives': True}) # Upload the file.