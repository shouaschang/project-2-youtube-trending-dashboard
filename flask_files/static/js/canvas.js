window.onload = function () {

  var chart = new CanvasJS.Chart("chartContainer", {
    theme: "light2", // "light2", "dark1", "dark2"
    animationEnabled: true, // change to true		
    title:{
      text: "Unique view per Category"
    },
    data: [
    {
      // Change type to "bar", "area", "spline", "pie",etc.
      type: "column",
      dataPoints: [
        { label: "Music",  y: 10  },
        { label: "Sports", y: 15  },
        { label: "Politics", y: 25  }
      ]
    }
    ]
  });
  chart.render();
  
  }