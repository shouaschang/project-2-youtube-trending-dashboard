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
