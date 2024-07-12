import React from "react";

const Car = (props) => {
    return (
        <div className="car">
           <p>{props.car.id} Авто {props.car.brand} </p>
        </div>
    )
}

export default Car;