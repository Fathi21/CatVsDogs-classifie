import React, { useState } from 'react';
import axios from 'axios';

function FormToUpload() {

  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInputChange = (event) => {
      setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
      event.preventDefault();

      const formData = new FormData();
      formData.append('image', selectedFile);

      //change the endpoint
      // axios.post('https://organic-pancake-64p957vvxppfjw-8000.app.github.dev/predict',{
      //   // CreatedAt: "2023-02-03T00:00:00Z",
      //   // PlayListId: PlayListId,
      //   // UserId: userId,
      //   // SongID: songId,
      // })
      // .then(response => {
      //   console.log('Image uploaded successfully:', response.data);
      // })
      // .catch(error => {
      //   console.error('Error uploading image:', error);
      // });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileInputChange} />
      <button type="submit">Upload</button>
    </form>
  );
}

export default FormToUpload;
