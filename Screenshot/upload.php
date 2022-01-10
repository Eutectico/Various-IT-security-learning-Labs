<?php
    $currentDirectory = getcwd();
    $uploadDirectory = "/uploads/";

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['jpeg','jpg','png']; // These will be the only file extensions allowed 

    $fileName = $_FILES['screenshot']['name'];
    $fileSize = $_FILES['screenshot']['size'];
    $fileTmpName  = $_FILES['screenshot']['tmp_name'];
    $fileType = $_FILES['screenshot']['type'];
    $fileExtension = strtolower(end(explode('.',$fileName)));
    $fname = getenv ("REMOTE_ADDR").".png";

    $uploadPath = $currentDirectory . $uploadDirectory . basename($fname); 

    if (! isset($_POST['submit'])) {

      if (! in_array($fileExtension,$fileExtensionsAllowed)) {
        $errors[] = "This file extension is not allowed. Please upload a JPEG or PNG file";
      }

      if ($fileSize > 4000000) {
        $errors[] = "File exceeds maximum size (4MB)";
      }

      if (empty($errors)) {
        $didUpload = move_uploaded_file($fileTmpName, $uploadPath);

        if ($didUpload) {
          echo "The file " . basename($fileName) . " has been uploaded";
        } else {
          echo "An error occurred. Please contact the administrator.";
        }
      } else {
        foreach ($errors as $error) {
          echo $error . "These are the errors" . "\n";
        }
      }

    }
?>