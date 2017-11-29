"use strict";

const fs = require("fs");

class Activity {
    constructor(activityNum, start, end) {
        this.activityNum = activityNum;
        this.start = start;
        this.end = end;
    }
}

const lastToStart = listOfActivities => {
    // Sorts the jobs by start time, starting with the last start time
    listOfActivities.sort((a,b) => {
        return b.start-a.start;
    });

    let chosenActivities = [];
    chosenActivities.push(listOfActivities[0]);
    let lastAddedActivity = listOfActivities[0];

    for(let j = 1; j < listOfActivities.length; j++) {
        let potentialActivity = listOfActivities[j];
        
        if(potentialActivity.end <= lastAddedActivity.start) {
            chosenActivities.push(listOfActivities[j]);
            lastAddedActivity = listOfActivities[j];
        }
    }

    return chosenActivities;
};

const dataFile = fs.readFileSync("act.txt");
const dataString = dataFile.toString("utf8");
const multiLineArray = dataString.split("\n");

let setNum = 0;
let numActivities = parseInt(multiLineArray[0]);
let activityArray = [];

for(let j = 1; j < multiLineArray.length; j++) {
    let lineArray = multiLineArray[j].split(" ");
    
    for(let i = 0; i < lineArray.length; i++) {
        lineArray[i] = parseInt(lineArray[i]);
    }

    if(lineArray.length !== 1) {
        let activityNum = lineArray[0];
        let start = lineArray[1];
        let end = lineArray[2];
        activityArray.push(new Activity(activityNum, start, end));
    } else {
        setNum++;
        console.log("Set " + setNum);
        let chosenActivities = lastToStart(activityArray);
        let numChosen = chosenActivities.length;
        console.log("Number of activities selected = " + numChosen);
        process.stdout.write("Activities: ");

        chosenActivities.reverse().forEach(activity => {
            process.stdout.write(activity.activityNum.toString() + " ");
        });
        console.log("\n");
        activityArray = [];
    }
}
