import React, { useEffect, useState } from 'react';

const App = () => {
    const [cars, setCars] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/auto/');
                const result = await response.json();
                 // Логируем результат
                console.log("API Response:", result);

                // Проверяем, что результат это массив
                if (Array.isArray(result)) {
                    setCars(result);
                } else {
                    console.error("API returned data is not an array", result);
                }
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    // Проверка, что cars — это массив
    if (Array.isArray(cars)) {
    cars.forEach(car => {
        console.log("Car ID:", car.id, "Car Name:", car.brand);
    });
} else {
    console.error("Expected an array but got:", typeof cars);
}

    return (
        <div>
            <h1>Cars List</h1>
            <ul>
                {cars.map(car => <li key={car.id}>{car.brand}</li>)}
            </ul>
        </div>
    );
};

export default App;