import React from "react";
import CarList from "./car_list";

const Car = (props) => {
    return (
        <div className="car">
           <strong>
               {props?.cars?.map((el, index) => {
                   return (
                       <div key={index}>
                           {el.brand}
                       </div>
                   )
               })}
           </strong>
        </div>
    )
}

export default Car;