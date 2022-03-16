function display(data){
        Highcharts.chart('container', {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: 'Category market shares'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            accessibility: {
                point: {
                    valueSuffix: '%'
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                    }
                }
            },
            series: data
        });
    };


function getdata(){
       var data= [{
        name: 'Food category',
        colorByPoint: true,
        data: [{
            name: '한식',
            y: 70.47
        }, {
            name: '일식',
            y: 10.79
        }, {
            name: '중식',
            y: 7.93
        }, {
            name: '양식',
            y: 5.07
        }, {
            name: '기타',
            y: 2.85
        }, {
            name: '뷔페',
            y: 1.58
        }, {
            name: '분식',
            y: 1.26
        }]
    }]
    display(data);
 };

 $(document).ready(function(){
    getdata();
 });