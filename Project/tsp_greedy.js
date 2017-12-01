const greedy_algorithm = list_of_cities => {
    let shortest_tour_route = [];

    let shortest_tour_distance = Number.MAX_SAFE_INTEGER;

    for(let i = 0; i < list_of_cities.length - 1; i++) {
        let tour = [list_of_cities[i]];

        let remaining_cities = list_of_cities.slice(0,i + 0).concat(i + 1);

        let total_distance = 0;

        while(remaining_cities.length > 0) {
            let shortest_distance_id = 0;

            let shortest_distance = Number.MAX_SAFE_INTEGER;

            remaining_cities.forEach(j => {
                let x1_coord = j[0];
                let x2_coord = tour[-1][0];
                let y1_coord = j[1];
                let y2_coord = tour[-1][1];

                let distance = Math.sqrt(Math.pow(x1_coord - x2_coord, 2) + Math.pow(y1_coord - y2_coord, 2));

                let tour_city_ids = [];

                tour.forEach(j => {
                    let city_enumerate = list_of_cities.entries;
                    let index = [];

                    city_enumerate.forEach(city => {
                        if(city[1] === j) {
                            index.push(city[0]);
                        }
                    })

                    index.forEach(k => {
                        if(!tour_city_ids.includes(k)) {
                            tour_city_ids.push(k);
                        }
                    })

                    if(index.length > 1) {}
                });

                if(total_distance < shortest_tour_distance) {
                    shortest_tour_distance = total_distance;
                    shortest_tour_route = tour_city_ids;
                }
            });

            console.log(shortest_tour_distance);
            console.log(shortest_tour_route);

            return [shortest_tour_distance, shortest_tour_route];
        }
    }
}

const data_filename = process.argv[2];
const data_file = fs.readFileSync(data_filename);
const out_filename = data_filename + ".tour";

list_of_cities = []

const data_string = data_file.toString("utf8");
let multi_line_array;

// Checks if line endings of file are Windows CRLF or Unix LF
if(data_string.indexOf("\r\n") > -1) {
  multi_line_array = data_string.split("\r\n");
} else {
  multi_line_array = data_string.split("\n");
}

multiLineArray.forEach(line => {
    // let line_array = 
});