// JavaScript file D3 line graph KNMI data max temperature De Bilt
// Iris de Vries
// 10367675

// Determine values
var outerWidth = 1000;
var outerHeight = 500;
var margin = { left: 50, top: 50, right: 50, bottom: 50 };
var xColumn = "timestamp";
var yColumn = "temperature";

// make canvas to draw on
var svg = d3.select("body").append("svg")
	.attr("width",  outerWidth)
	.attr("height", outerHeight);

// 
var g = svg.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var path = g.append("path");

//
var innerWidth  = outerWidth  - margin.left - margin.right;
var innerHeight = outerHeight - margin.top  - margin.bottom;

// Make x_scale and y_scale
var xScale = d3.time.scale().range([0, innerWidth]);
var yScale = d3.scale.linear().range([innerHeight, 0]);

// Make line
var line = d3.svg.line()
	.x(function(d) { return xScale(d[xColumn]); })
	.y(function(d) { return yScale(d[yColumn]); });

// Render function with axes
function render(data){
	xScale.domain( d3.extent(data, function (d){ return d[xColumn]; }));
	yScale.domain( d3.extent(data, function (d){ return d[yColumn]; }));
	path.attr("d", line(data));

	// make x-axis
	var x_axis = d3.svg.axis()
		.scale(xScale)
		.orient("bottom")
		.tickFormat(d3.time.format("%m")) // display January as 01 etc.
		.tickSize(2); 

	// make y-axis	
	var y_axis = d3.svg.axis()
	    .scale(yScale)
	    .orient("left") ;

	// append x-axis to svg
	svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(50, 480)") 
		.call(x_axis)
		.append("text")
		.attr("dy", "-.71em")
		.attr("x", innerWidth)
		.style("text-anchor", "end")
			.text("maanden") ;    

	// append y-axis to svg
	svg.append("g")
	    .attr("class", "y axis")
	    .attr("transform", "translate(50, 80)") 
	    .call(y_axis)
	    .append("text")
	    .attr("transform", "rotate(-90)")
	    .attr("y", 6)
	    .attr("dy", "0.71em")
	    .style("text-anchor", "end")
	    	.text("temperatuur") ;   
}

// function mousemove() {
//     var x0 = xScale.invert(d3.mouse(this)[0]),
//     index = bisectDate(data, x0, 1),
//     d0 = data[index - 1],
//     d1 = data[index],
//     d = x0 - d0.date > d1.date - x0 ? d1 : d0;
//     var xPos = x(d.date);
//     var yPos = y(d.temp);  
//     crosshairX.attr("x1", xPos).attr("y1", 0).attr("x2", xPos).attr("y2", height);
//     crosshairY.attr("x1", 0).attr("y1", yPos).attr("x2", width).attr("y2", yPos);
//     displayTooltip(d.date, d.temp);
// }


// string to float
function type(d){
	d.timestamp = new Date(d.timestamp);
	d.temperature = +d.temperature;
	return d;
}

// load data
d3.csv("try2.csv", type, render);        
 

// title graph
svg.append("text")
        .attr("x", (outerWidth/2))             
        .attr("y", 20)
        .attr("text-anchor", "middle")  
        .style("font-size", "16px") 
        .text("Max Temperatuur De Bilt 2014");

