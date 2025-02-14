import React, { useState, useEffect } from "react";
import axios from "axios";

function PhotoModel(props) {
  const [imageData, setImageData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchImage = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/Api/GetUploadedImageById/" + props.imageId
        );

        console.log("API Response:", response); // Log the full response

        setImageData(response.data[0]); // Access the first element of the array
      } catch (err) {
        setError(err.message);
        console.error("Error fetching image:", err);
      } finally {
        setLoading(false);
      }
    };

    if (props.imageId) {
      fetchImage();
    } else {
      setImageData(null);
    }
  }, [props.imageId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  console.log("data:", imageData ? imageData.image : null); // Log the full response

  const card = imageData ? (
    <div className="card">
      <img
        src={`http://127.0.0.1:8000${imageData.image}`} // Construct image URL
        className="card-img-top"
        alt={`Image ${imageData.id}`} // Use a dynamic alt attribute
        style={{ objectFit: "cover", height: "200px" }}
      />
      <div className="card-body">
        <h5 className="card-title">ImageID {imageData.id}</h5>
        {/* Dynamic title */}
        <p className="card-text">
          Uploaded at: {new Date(imageData.created_at).toLocaleString()}
          {/* Format date */}
        </p>
      </div>
    </div>
  ) : null;

  return (
    <div
      className="modal fade"
      id="staticBackdrop"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h1 className="modal-title fs-5" id="staticBackdropLabel">
              Modal title
            </h1>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">{card}</div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button type="button" className="btn btn-primary">
              Understood
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PhotoModel;
