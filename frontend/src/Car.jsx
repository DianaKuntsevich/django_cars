import React from "react";

const Car = (props) => {
    return (
        <div className="car">
           <strong>
               {this.props.cars.map((el, index) => {
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