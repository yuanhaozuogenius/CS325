"use strict";

const fs = require("fs");

const getRandomInt = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
};

const genRandomNumbers = numToGen => {
    let numArray = [];

    for(let i = 0; i < numToGen; i++) {
        numArray.push(getRandomInt(0,10000));
    }

    return numArray;
};

const stoogeSort = (array, lowIndex, highIndex) => {
  const n = highIndex - lowIndex + 1;

  if (n === 2 && array[lowIndex] > array[lowIndex + 1]) {
      const storage = array[lowIndex];
      array[lowIndex] = array[lowIndex + 1];
      array[lowIndex + 1] = storage;
  }

  else if (n > 2) {
      const m = Math.ceil((2 * n) / 3);
      stoogeSort(array, lowIndex, m - 1 + lowIndex);
      stoogeSort(array, n - m + lowIndex, highIndex);
      stoogeSort(array, lowIndex, m - 1 + lowIndex);
  }
};

const timeArray = [500,1000,1500,2000,2500,3000,3500];

fs.writeFileSync("stoogetime.csv", "num,time\n");

timeArray.forEach(num => {
    for(let i = 0; i < 5; i++) {
        const randomArray = genRandomNumbers(num);
        const start = new Date();
        const hrstart = process.hrtime();
        stoogeSort(randomArray, 0, randomArray.length - 1);
        const end = new Date() - start;
        const hrend = process.hrtime(hrstart);
        fs.appendFileSync("stoogetime.csv", num + "," + end + "\n");
    }
});
