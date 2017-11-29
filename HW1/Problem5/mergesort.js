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

const mergeSort = array => {
    const arraySize = array.length;

    if(arraySize === 1 || arraySize === 0) {
        return array;
    }

    const arraySplit = arraySize / 2;

    const n1 = mergeSort(array.slice(0, arraySplit));
    const n2 = mergeSort(array.slice(arraySplit));

    return merge(n1,n2);
};

const merge = (array1, array2) => {
    let newArray = [];

    while(array1.length != 0 && array2.length != 0) {
        if(array1[0] < array2[0]) {
            newArray.push(array1[0]);
            array1.splice(0,1);
        } else {
            newArray.push(array2[0]);
            array2.splice(0,1);
        }
    }

    if(array1.length === 0) {
        newArray = newArray.concat(array2);
    } else {
        newArray = newArray.concat(array1);        
    }

    return newArray;
};

const timeArray = [500,1000,1500,2000,2500,3000,3500];

fs.writeFileSync("mergetime.csv", "num,time\n");

timeArray.forEach(num => {
    for(let i = 0; i < 5; i++) {
        const randomArray = genRandomNumbers(num);
        const start = new Date();
        const hrstart = process.hrtime();
        const sortedArray = mergeSort(randomArray);
        const end = new Date() - start;
        const hrend = process.hrtime(hrstart);
        fs.appendFileSync("mergetime.csv", num + "," + end + "\n");
    }
})
