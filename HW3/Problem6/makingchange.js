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

const fillArrayOfDenoms = numToGen => {
  let arrayOfDenoms = [];

  for(let i = 0; i < numToGen; i++) {
    arrayOfDenoms.push(i+1);
  }

  return arrayOfDenoms;
};

// Quick function to add 2 arrays together for calculation in the main function
const addArrays = (array1, array2) => {
  for(let i = 0; i < array1.length; i++) {
    array1[i] += array2[i];
  }
};

const makeChange = (denoms, amount) => {
  let coinAmountTracker = [];
  let currentDenomsCount = denoms;

  // Fills out 2-dimensional array of possible coins per amount of money
  // for example: [0,0,0,0] (one subarray), with the first 3 0's being 
  // denominations and the last being the number of total coins, so it might 
  // end up: [1,0,3,4]
	for(let i = 0; i <= amount; i++) {
    coinAmountTracker.push([]);
    for(let j = 1; j <= denoms.length + 1; j++) {
      coinAmountTracker[i].push(0);
    }
  }

  // Iterate through all numbers from 1 to the target coin amount
  for(let j = 0; j <= amount; j++) {
    let amountLeft = j;

      // Iterate through all coin denominations starting with the largest
      for(let i = denoms.length - 1; i >= 0; i--) {
        if(amountLeft > 0) {
          // Tracks current coin denomination
          let currentCoin = denoms[i];

          if(currentCoin <= amountLeft) {

            // Calculates the number needed of the current coin
            let numCurrentCoin = Math.floor(amountLeft / currentCoin);

            // adds the number to the result array
            coinAmountTracker[j][i] += numCurrentCoin;

            // keeps a running coin total on the subarray
            coinAmountTracker[j][denoms.length] += numCurrentCoin;

            // calculates the remainder
            amountLeft -= (numCurrentCoin * currentCoin);

            // Looks for previous calculations using the amount in the remainder
            // then adds the 2 arrays of results if found
            if(amountLeft > 0) {
              addArrays(coinAmountTracker[j], coinAmountTracker[amountLeft]);
              amountLeft = 0;
            }
          }

          
      }
    }
  }
  
  return(coinAmountTracker[amount]);
};

const numDenomsToTest = [500,1000,1500,2000,2500,3000,3500];

fs.writeFileSync("changetime.csv", "denoms,amount,time\n");

numDenomsToTest.forEach(num => {
    for(let i = 0; i < 5; i++) {
        const denomsArray = fillArrayOfDenoms(num);
        const amount = getRandomInt(0,10000);
        const start = new Date();
        const hrstart = process.hrtime();
        makeChange(denomsArray, amount);
        const end = new Date() - start;
        const hrend = process.hrtime(hrstart);
        fs.appendFileSync("changetime.csv", num + "," + amount + "," + end + "\n");
    }
});
