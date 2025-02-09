import './App.css';
import FormToUpload from "./comp/FormToUpload";
import ListImagesUploaded from './comp/ListImagesUploaded'
function App() {

  return (
    <div className="App">
      <FormToUpload/>
      <ListImagesUploaded />
    </div>
  );
}

export default App;
