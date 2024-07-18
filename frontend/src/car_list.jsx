import React from "react";
import Car from "./Car";

const CarList = ({cars}) => {
    //  if (!cars.length) {
    //     return <h1 style={{textAlign: "center"}}>Дела не найдены</h1>
    // }


    return (
        <div>
            {cars &&
                cars.map(car => <Car car={car} key={car.id}/>)}
        </div>

    )
}

export default CarList;