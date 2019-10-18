function buildBar1() {
    var trace = {
      type: "bar",
      x: ["Music", "Sports", "Politics"],
      y: [150, 200, 175]

    };

    var data = [trace];

    var layout = {
     title: "Comments Comparison in All Categories",
    };

    Plotly.newPlot('bar1', data, layout)
  };

buildBar1();


function buildBar2() {
    var trace = {
      type: "bar",
      x: ["Music", "Sports", "Politics"],
      y: [6325, 2241, 2489]

    };

    var data = [trace];

    var layout = {
     title: "Unique Videos Within Category",
    };

    Plotly.newPlot('bar2', data, layout)
  };

buildBar2();

function init() {
  var data = [{
    values: [1, 39],
    labels: ["Likes", "Dislikes"],
    type: "pie"
  }];

  var layout = {
  height: 500,
  width: 500
}
  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  var PIE = document.getElementById("pie");
  Plotly.restyle(PIE, "values", [newdata]);
}

function getData(dataset) {
  var data = [];
  switch (dataset) {
  case "dataset1":
    data = [114188, 1333];
    break;
  case "dataset2":
    data = [655, 25];
    break;
  case "dataset3":
    data = [12654, 1363];
    break;
  default:
    data = [0, 0, 0, 0];
  }
  updatePlotly(data);
}

init();

function init2(){

  // Create the Traces
  var trace1 = {
    x: 300,
    y: 200,
    mode: "markers",
    type: "scatter",
    name: "high jump",
    marker: {
      color: "#2077b4",
      symbol: "hexagram"
    }
  };

  var trace2 = {
    x: 100,
    y: 200,
    mode: "markers",
    type: "scatter",
    name: "discus throw",
    marker: {
      color: "orange",
      symbol: "diamond-x"
    }
  };

  var trace3 = {
    x: 500,
    y: 600,
    mode: "markers",
    type: "scatter",
    name: "long jump",
    marker: {
      color: "rgba(156, 165, 196, 1.0)",
      symbol: "cross"
    }
  };

  // Create the data array for the plot
  var data = [trace1, trace2, trace3];

  // Define the plot layout
  var layout = {
    title: "Views by Months",
    xaxis: { title: "Months" },
    yaxis: { title: "Views" }
  };

  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("scatter", data, layout);

  function updatePlotly(newdata) {
    var SCATTER = document.getElementById("scatter");
    Plotly.restyle(SCATTER, "values", [newdata]);
  }

  function getData(dataset) {
    var data = [];
    switch (dataset) {
    case "dataset1":
      data = {x: 300,
      y: 200,
      mode: "markers",
      type: "scatter",
      name: "high jump",
      marker: {
        color: "#2077b4",
        symbol: "hexagram"
      }
      };
      break;
    case "dataset2":
      data = {x: 300,
      y: 200,
      mode: "markers",
      type: "scatter",
      name: "high jump",
      marker: {
        color: "#2077b4",
        symbol: "hexagram"
      }
      };
      break;
    case "dataset3":
      data = {x: 300,
      y: 200,
      mode: "markers",
      type: "scatter",
      name: "high jump",
      marker: {
        color: "#2077b4",
        symbol: "hexagram"
      }
      };
      break;
    default:
      data = [0, 0, 0, 0];
    }}
    updatePlotly(data);

}

init2();
