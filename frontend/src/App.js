import CarList from "./car_list";
import axios from "axios";
import {useState} from "react";


const API_URL = 'http://127.0.0.1:8000/api/auto/'

function App() {
    const [cars, setCars] = useState([])
    async function getAuto() {
        const response = await axios.get(API_URL)
        setCars(response.data)
    }

    return (
        <div className="App">

            <button className="btn btn-info" onClick={getAuto}>Обновить авто</button>
            <CarList cars={cars}/>

        </div>
    );
}

export default App;