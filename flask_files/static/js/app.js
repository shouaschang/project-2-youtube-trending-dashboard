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
      y: [200, 175, 150]

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
    height: 600,
    width: 800
  };

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
