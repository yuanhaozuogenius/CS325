"use strict";

const fs = require("fs");
const os = require('os');

class Vertex {
    constructor(data) {
        this.data = data;
        this.edges = [];
        this.visited = false;
        this.predecessor = null;
        this.distance = null;
    }
}

const bfs = inputGraph => {
    let queue = [];
    let faces = [];
    let heels = [];
    let impossible = false;

    for(let j = 0; j < inputGraph.length; j++) {
        if(inputGraph[j].visited === false) {
            let startingIndex = j;
            queue.push(startingIndex);
            inputGraph[startingIndex].distance = 0;

            while(queue.length > 0) {
                let currentVertexIndex = queue.shift();
                let currentNeighbors = inputGraph[currentVertexIndex].edges;
                inputGraph[currentVertexIndex].visited = true;

                for(let i = 0; i < currentNeighbors.length; i++) {
                    if(inputGraph[currentNeighbors[i]].visited === false) {
                        inputGraph[currentNeighbors[i]].predecessor = currentVertexIndex;
                        inputGraph[currentNeighbors[i]].distance = inputGraph[inputGraph[currentNeighbors[i]].predecessor].distance + 1;
                        queue.push(currentNeighbors[i]);
                    }
                }
            }
        }
    }

    // Iterates through array to check if a face or a heel, checks against
    // neighbors to make sure a face or heel are not connected to same type,
    // returns impossible if a same match is made
    for(let k = 0; k < inputGraph.length; k++) {
        // If distance is even, it's a face
        if(inputGraph[k].distance % 2 === 0) {
            inputGraph[k].edges.forEach(neighbor => {
                if(inputGraph[neighbor].distance % 2 === 0) {
                    impossible = true;
                }
            })
            faces.push(k);
        // If distance is odd, it's a heel
        } else {
            inputGraph[k].edges.forEach(neighbor => {
                if(inputGraph[neighbor].distance % 2 !== 0) {
                    impossible = true;
                }
            })
            heels.push(k);
        }
    }

    if(impossible === true) {
        return "Impossible";
    } else {
        return [faces,heels];
    }
}

// Program uses wrestler.txt by default, or specified on the command line
// e.g. $ node wrestlerGraph.js wrestler1.txt
const fileName = process.argv[2] || "wrestler.txt";
const dataFile = fs.readFileSync(fileName);
const dataString = dataFile.toString("utf8");
let multiLineArray;

// Checks if line endings of file are Windows CRLF or Unix LF
if(dataString.indexOf("\r\n") > -1) {
  multiLineArray = dataString.split("\r\n");
} else {
  multiLineArray = dataString.split("\n");
}

let isArrayLine = true;
let lineArray = [];
let lineAmount = 0;
let workingGraph = [];

// Constructs the graph
multiLineArray.forEach(line => {
  lineArray = line.split(" ");

  if(lineArray.length === 1) {
      if(!isNaN(lineArray[0])) {

      } else {
        workingGraph.push(new Vertex(lineArray[0]));
      }
  } else {
    let rival1 = lineArray[0];
    let rival2 = lineArray[1];

    let obj1 = workingGraph.find(x => x.data === rival1);
    let obj2 = workingGraph.find(x => x.data === rival2);

    let index1 = workingGraph.indexOf(obj1);
    let index2 = workingGraph.indexOf(obj2);

    workingGraph[index1].edges.push(index2);
    workingGraph[index2].edges.push(index1);
  }
});

const result = bfs(workingGraph);

// Checks the result output and writes to file
if(result === "Impossible") {
    console.log(result);
} else {
    console.log("Yes");
    process.stdout.write("Babyfaces: ");
    result[0].forEach(face => {
        process.stdout.write(workingGraph[face].data + " ");
    })
    process.stdout.write("\n");
    process.stdout.write("Heels: ");
    result[1].forEach(heel => {
        process.stdout.write(workingGraph[heel].data + " ");
    })
    process.stdout.write("\n");
}
