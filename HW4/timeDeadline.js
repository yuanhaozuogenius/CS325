"use strict";

class Activity {
    constructor(deadline, penalty) {
        this.deadline = deadline;
        this.penalty = penalty;
    }
}

const timeDeadline = listOfJobs => {
    // Sorts the jobs by deadline, ascending
    listOfJobs.sort((a,b) => {
        return a.deadline-b.deadline;
    });

    let chosenActivities = [];
    chosenActivities.push(listOfJobs[0]);
    let lastAddedActivity = listOfJobs[0];

    for(let j = 1; j < listOfJobs.length; j++) {
        let potentialActivity = listOfJobs[j];
        
        if(potentialActivity.end <= lastAddedActivity.deadline) {
            chosenActivities.push(listOfJobs[j]);
            lastAddedActivity = listOfJobs[j];
        }
    }

    return chosenActivities;
};