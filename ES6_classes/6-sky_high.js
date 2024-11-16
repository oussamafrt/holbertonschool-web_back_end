/* eslint-disable */
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
