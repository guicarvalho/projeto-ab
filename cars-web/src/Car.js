import React from 'react';
import axios from 'axios';

export default class CarList extends React.Component {
  state = {
    cars: []
  }

  componentDidMount() {
    axios.get('http://localhost:5000/api/v1/cars')
      .then(res => {
        const cars = res.data;
        this.setState({ cars });
      });
  }

  render() {
    return (
      <div>
        <h1>Carros</h1>
        <ul>
          { this.state.cars.map(car => <li key={ car.cod_fipe }>{car.modelo}</li>) }
        </ul>
      </div>
    )
  }
}
