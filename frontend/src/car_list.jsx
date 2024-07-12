import React from "react";
import Car from "./Car";

const CarList = ({cars}) => {
    if (!cars.length) {
        return <h1>Автомобили не найдены !</h1>
    }

    return (
        <div>
            {cars.map(car => <Car car={car} key={car.id}/>)}
        </div>

    )
}

export default CarList;