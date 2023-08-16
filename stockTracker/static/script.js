var tickers = JSON.parse(localStorage.getItem('tickers')) || [];
var lastPrices = {};
var counter = 15;

function startUpdateCycle() {
    updatePrices();
    var countDown = setInterval(function() {
        counter--;
        $('#counter').text(counter);
        if (counter <= 0) {
            updatePrices();
            counter = 15;
        }
    }, 1000)
}

function updatePrices() {
}

$(document).ready(function() {
    tickers.forEach(function(ticker) {
        addTickerToGrid();
    });
    updatePrices();
});