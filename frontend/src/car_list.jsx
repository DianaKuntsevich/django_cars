import React from "react";
import Car from "./Car";

const CarList = ({cars}) => {
     if (!cars.length) {
        return <h1 style={{textAlign: "center"}}>Авто не найдены</h1>
    }


    return (
        <div>
            <h1>Car List</h1>
            <ul>
                  {cars?.map(car => <Car car={car} key={car.id}/>)}
            </ul>
        </div>

    )
}

export default CarList;