import React, { useState } from "react";
import axios from "axios";

function FormToUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState(null);
  const [error, setError] = useState(null);
  const fileInputRef = React.useRef(null); // Ref for the file input

  const handleFileInputChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!selectedFile) {
      setError("Please select an image.");
      return;
    }

    setUploadStatus("Uploading...");
    setError(null);

    const formData = new FormData();
    formData.append("image", selectedFile);

    axios
      .post("http://127.0.0.1:8000/Api/uploadImage", formData, {
        // Key change: formData directly
        headers: {
          "Content-Type": "multipart/form-data", // Important if not automatically set
        },
      })
      .then((response) => {
        setUploadStatus("Upload complete!");
        console.log("Image uploaded successfully:", response.data);
        setSelectedFile(null); // Clear selected file state
        if (fileInputRef.current) {
          fileInputRef.current.value = ""; // Clear the file input value
        }
      })
      .catch((error) => {
        setUploadStatus("Upload failed.");
        setError(error.response ? error.response.data.image : error.message); // Extract server error
        console.error("Error uploading image:", error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileInputChange} />
      <button type="submit" disabled={!selectedFile}>
        Upload
      </button>

      {uploadStatus && <p>{uploadStatus}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}

export default FormToUpload;
