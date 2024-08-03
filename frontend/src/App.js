import CarList from "./car_list";
import axios from "axios";
import {useEffect, useState} from "react";



const App = () => {
    const [cars, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/auto/') // Замените на ваш URL
            .then((response) => {
                setData(response.data);
                setLoading(false);
                console.log(response.data)
            })
            .catch((error) => {
                setError(error);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div>
            <h1>Data from API</h1>

            <h1>Список авто</h1>

            <CarList cars={cars}/>
        </div>
    );
};

export default App;

