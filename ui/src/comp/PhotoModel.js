import React, { useState, useEffect } from "react";
import axios from "axios";

function PhotoModel(props) {
  const [imageData, setImageData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [predicting, setPredicting] = useState(false);
  const [predictionResult, setPredictionResult] = useState(null);

  useEffect(() => {
    const fetchImage = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/Api/GetUploadedImageById/" + props.imageId
        );

        setImageData(response.data[0]);
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

  const handlePrediction = async () => {
    setPredicting(true);
    setError(null);
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/Api/SaveThePrediction",
        {
          imageId: props.imageId, // Use imageId directly
        }
      );
      console.log("Prediction Response:", response.data);
      setPredictionResult(response.data);
    } catch (err) {
      setError(err.message);
      console.error("Error during prediction:", err);
    } finally {
      setPredicting(false);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  const card = imageData ? (
    <div className="card">
      <img
        src={`http://127.0.0.1:8000${imageData.image}`}
        className="card-img-top"
        alt={`Image ${imageData.id}`}
        style={{ objectFit: "cover", height: "200px" }}
      />
      <div className="card-body">
        <h5 className="card-title">ImageID {imageData.id}</h5>
        <p className="card-text">
          Uploaded at: {new Date(imageData.created_at).toLocaleString()}
        </p>
        {predictionResult && (
          <div className="prediction-result-box">
            <p>
              <strong>Prediction:</strong> {predictionResult.prediction}
            </p>
            <p>
              <strong>Confidence:</strong>{" "}
              {predictionResult.confidence.toFixed(2)}%
            </p>
          </div>
        )}
      </div>
    </div>
  ) : null;

  return (
    <div
      className="modal fade"
      id="staticBackdrop"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabIndex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div className="modal-dialog">
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
            <button
              type="button"
              className="btn btn-primary"
              onClick={handlePrediction}
              disabled={predicting}
            >
              {predicting ? "Predicting..." : "Get Prediction"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PhotoModel;
