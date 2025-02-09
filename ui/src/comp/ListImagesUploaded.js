import React from 'react';

function ListImagesUploaded() {
  return (
    <div className="container text-center">

    <div className="row row-cols-1 row-cols-md-3 g-4">
      <div className="col">
        <div className="card">
          <img
            src="https://images.pexels.com/photos/1314550/pexels-photo-1314550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            className="card-img-top"  // Add Bootstrap class for responsive images
            alt="..."
            style={{ objectFit: 'cover', height: '200px' }} // Control image height and fit
          />
          <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">This is a longer card...</p>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card">
          <img
            src="https://images.pexels.com/photos/1314550/pexels-photo-1314550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            className="card-img-top"  // Add Bootstrap class for responsive images
            alt="..."
            style={{ objectFit: 'cover', height: '200px' }} // Control image height and fit
          />
          <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">This is a longer card...</p>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card">
          <img
            src="https://images.pexels.com/photos/1314550/pexels-photo-1314550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            className="card-img-top"  // Add Bootstrap class for responsive images
            alt="..."
            style={{ objectFit: 'cover', height: '200px' }} // Control image height and fit
          />
          <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">This is a longer card...</p>
          </div>
        </div>
      </div>

      <div className="col">
        <div className="card">
          <img
            src="https://images.pexels.com/photos/1314550/pexels-photo-1314550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            className="card-img-top"  // Add Bootstrap class for responsive images
            alt="..."
            style={{ objectFit: 'cover', height: '200px' }} // Control image height and fit
          />
          <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">This is a longer card...</p>
          </div>
        </div>
      </div>


      <div className="col">
        <div className="card">
          <img
            src="https://images.pexels.com/photos/1314550/pexels-photo-1314550.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
            className="card-img-top"  // Add Bootstrap class for responsive images
            alt="..."
            style={{ objectFit: 'cover', height: '200px' }} // Control image height and fit
          />
          <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">This is a longer card...</p>
          </div>
        </div>
      </div>
      {/* ... (repeat the structure for other cards) */}
    </div>
    </div>

  );
}

export default ListImagesUploaded;