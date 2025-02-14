import React, { useState, useEffect } from "react";
import axios from "axios";
import PhotoModel from "./PhotoModel";

function ListImagesUploaded() {
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageClick = (image) => {
    setSelectedImage(image.id);
  };

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/Api/GetUploadedImages"
        );
        setImages(response.data);
      } catch (err) {
        setError(err.message); // Set the error message
        console.error("Error fetching images:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchImages();
  }, []); // Empty dependency array ensures this runs only once on mount

  if (loading) {
    return <div>Loading images...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>; // Display the error message
  }

  return (
    <div className="container text-center">
      <div className="row row-cols-1 row-cols-md-3 g-4">
        {images.map((image) => (
          <div
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#staticBackdrop"
            className="col"
            key={image.id}
          >
            {/* Add a unique key */}
            <div onClick={() => handleImageClick(image)} className="card">
              <img
                src={`http://127.0.0.1:8000${image.image}`} // Construct image URL
                className="card-img-top"
                alt={`Image ${image.id}`} // Use a dynamic alt attribute
                style={{ objectFit: "cover", height: "200px" }}
              />
              <div className="card-body">
                <h5 className="card-title">ImageID {image.id}</h5>
                {/* Dynamic title */}
                <p className="card-text">
                  Uploaded at: {new Date(image.created_at).toLocaleString()}
                  {/* Format date */}
                </p>
              </div>
            </div>
          </div>
        ))}

        <PhotoModel imageId={selectedImage} />
      </div>
    </div>
  );
}

export default ListImagesUploaded;
