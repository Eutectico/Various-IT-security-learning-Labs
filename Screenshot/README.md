# Secretly create and send a screenshot

It is often convenient to take screenshots of the target systems and send them to an external server.

Attached is a short python and php script that allows you to do this. 

## Target systems

Copy **screenshot.py** on the target systems

## Server

Do you need a PHP server. Copy **upload.php** on your Server

Now there are a couple final steps before we can start uploading files:
* Go to your uploads/ directory and make it writable by running: chmod 0755 uploads/
* Make sure your php.ini file is correctly configured to handle file uploads *(Tip: to find your php.ini file, run php --ini):*


    max_file_uploads = 20
    upload_max_filesize = 2M
    post_max_size = 8M


Finally, if you now start the PHP server.