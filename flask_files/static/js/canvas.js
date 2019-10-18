window.onload = function () {
  var chart = new CanvasJS.Chart("chartContainer", {
     theme: "light2", // "light2", "dark1", "dark2"
      animationEnabled: true, // change to true
       title:{
           text: "Unique Videos per Category"
          },
           data: [
              {
  // Change type to "bar", "area", "spline", "pie",etc.
          type: "bar",
          dataPoints:
            { label: "Music",  y: 6325  },
            { label: "Sports", y: 2241  },
            { label: "Politics", y: 2489  }
          ]
        }
        ]
      });
chart.render();
}
