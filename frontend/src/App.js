
import axios from "axios";
import {useEffect, useState} from "react";



const App = () => {
    const [cars, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
            axios.get("http://127.0.0.1:8000/api/auto/") // Замените на ваш URL
                .then((response) => {
                    setData(response.data);
                    setLoading(false);
                    console.log(response.data);
                })
                .catch((error) => {
                    setError(error);
                    setLoading(false);
                });
        }, []);


    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div className="App">

            <h1>Список авто</h1>

            <div className="cars">
                {cars && cars.map((cars, index) => {
                    return(
                        <div className="car" key={index}>
                            <h3> Car {index + 1}</h3>
                            <h2>{cars.results.brand}</h2>

                        </div>
                    );
                })}
            </div>
        </div>
    );
}

export default App;

