/* eslint-disable */
export default class Car {
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    // Method to clone the car
    cloneCar() {
      const Constructor = this.constructor; // Access the class constructor dynamically
      return new Constructor(); // Create a new instance without attributes
    }
  }
  