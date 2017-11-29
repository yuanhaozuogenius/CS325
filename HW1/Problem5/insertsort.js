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

const insertionSort = array => {
    for(let j = 1; j < array.length; j++) {
        const key = array[j];

        let i = j - 1;
        while((i > -1) && (array[i] > key)) {
            array[i + 1] = array[i];
            i = i - 1;
        }

        array[i + 1] = key;
    }
};

const timeArray = [500,1000,1500,2000,2500,3000,3500];;

fs.writeFileSync("inserttime.csv", "num,time\n");

timeArray.forEach(num => {
    for(let i = 0; i < 5; i++) {
        const randomArray = genRandomNumbers(num);
        const start = new Date();
        const hrstart = process.hrtime();
        insertionSort(randomArray);
        const end = new Date() - start;
        const hrend = process.hrtime(hrstart);
        fs.appendFileSync("inserttime.csv", num + "," + end + "\n");
    }
});
