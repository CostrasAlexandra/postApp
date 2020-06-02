
function pieChart() {
                // pie chart data
            var pieData = [
                {
                    value: 20,
                    color:"#878BB6"
                },
                {
                    value : 40,
                    color : "#4ACAB4"
                },
                {
                    value : 10,
                    color : "#FF8153"
                },
                {
                    value : 30,
                    color : "#FFEA88"
                }
            ];
            // pie chart options
            var pieOptions = {
                 segmentShowStroke : false,
                 animateScale : true
            }
            // get pie chart canvas
            var countries= document.getElementById("countries").getContext("2d");
            // draw pie chart
     new Chart(countries).Pie(pieData, pieOptions);
}

$( document ).ready( function() {
    $('div.pieChart').each(function(i, d) {
        console.log('slot found: ' + d.id);
         var pieData = [
                {
                    value: 20,
                    color:"#878BB6"
                },
                {
                    value : 40,
                    color : "#4ACAB4"
                },
                {
                    value : 10,
                    color : "#FF8153"
                },
                {
                    value : 30,
                    color : "#FFEA88"
                }
            ];
            // pie chart options
            var pieOptions = {
                 segmentShowStroke : false,
                 animateScale : true
            }
            // get pie chart canvas
            var countries= document.getElementById("countries").getContext("2d");
            // draw pie chart
     new Chart(countries).Pie(pieData, pieOptions);
    });
});

 function linechart() {
     const LINECHART = document.getElementById("lineChart")

        pieData = {
    datasets: [{
        data: [{value:10, color:"red"}, 20, 30]
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
};
        // pie chart data
            var a = [
                {
                    value: 20,
                    color:"#878BB6"
                },
                {
                    value : 40,
                    color : "#4ACAB4"
                },
                {
                    value : 10,
                    color : "#FF8153"
                },
                {
                    value : 30,
                    color : "#FFEA88"
                }
            ];
            // pie chart options
            var pieOptions = {
                 segmentShowStroke : false,
                 animateScale : true
            }


     let lineChart = new Chart(LINECHART, {
    type: 'doughnut',
    data: pieData,
    options: {}
});
 }

 function tryagain(){
     var pieData = [
    {
        value: 20,
        color:"#878BB6"
    },
    {
        value : 40,
        color : "#4ACAB4"
    },
    {
        value : 10,
        color : "#FF8153"
    },
    {
        value : 30,
        color : "#FFEA88"
    }
];

var pieOptions = {
    segmentShowStroke : false,
    animateScale : true
}

var countries= document.getElementById("lineChart").getContext("2d");
        return new Chart(countries).Pie(pieData, pieOptions);
 }