"use strict";

const fs = require("fs");

const stoogeSort = (array, lowIndex, highIndex) => {
  const n = highIndex - lowIndex + 1;

  if (n === 2 && array[lowIndex] > array[lowIndex + 1]) {
      const storage = array[lowIndex];
      array[lowIndex] = array[lowIndex + 1];
      array[lowIndex + 1] = storage;
  }

  else if (n > 2) {
      const m = Math.floor((2 * n) / 3);
      stoogeSort(array, lowIndex, m - 1 + lowIndex);
      stoogeSort(array, n - m + lowIndex, highIndex);
      stoogeSort(array, lowIndex, m - 1 + lowIndex);
  }
};

const dataFile = fs.readFileSync("data.txt");
fs.writeFileSync("stooge.out", "");
const dataString = dataFile.toString("utf8");
const multiLineArray = dataString.split("\n");

multiLineArray.forEach(line => {
    let lineArray = line.split(" ");
    
    for(let i = 0; i < lineArray.length; i++) {
        lineArray[i] = parseInt(lineArray[i], 10);
    }

    const intArray = lineArray.slice(1);

    stoogeSort(intArray, 0, intArray.length - 1);

    intArray.forEach(number => {
      fs.appendFileSync("stooge.out", number + " ");
    });

    fs.appendFileSync("stooge.out", "\n");
});

