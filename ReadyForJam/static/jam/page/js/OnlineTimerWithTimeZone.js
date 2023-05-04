document.addEventListener("DOMContentLoaded", function () {
    let timerBlock = document.querySelector('.jam-block__timer-container')
    function calculateRemainingTime() {
        timerBlock.removeEventListener('DOMNodeInserted', calculateRemainingTime);
        let url = 'https://worldtimeapi.org/api/ip';
        fetch(url)
            .then(response => response.json())
            .then(data => {
                let startDateValue = document.querySelector('#startDate');
                if (!startDateValue) return;
                else startDateValue = startDateValue.value;
                let currentTime = new Date(data.utc_datetime);
                let targetTime = new Date(startDateValue);
                // change this to your target date and time in UTC
                let timeDifference = (targetTime.getTime() - currentTime.getTime()) / 1000;
                let days = Math.floor(timeDifference / 86400);
                let hours = Math.floor((timeDifference % 86400) / 3600);
                let minutes = Math.floor((timeDifference % 3600) / 60);
                let seconds = Math.floor(timeDifference % 60);
                updateTimer(days, hours, minutes, seconds);
                setInterval(() => {
                    timeDifference--;
                    days = Math.floor(timeDifference / 86400);
                    hours = Math.floor((timeDifference % 86400) / 3600);
                    minutes = Math.floor((timeDifference % 3600) / 60);
                    seconds = Math.floor(timeDifference % 60);
                    updateTimer(days, hours, minutes, seconds);
                }, 1000);
            })
            .catch(error => console.error('Error:', error));
    }

    function updateTimer(days, hours, minutes, seconds) {
        document.getElementById("days").innerText = formatTime(days);
        document.getElementById("hours").innerText = formatTime(hours);
        document.getElementById("minutes").innerText = formatTime(minutes);
        document.getElementById("seconds").innerText = formatTime(seconds);
    }

    function formatTime(time) {
        return time < 10 ? `0${time}` : time;
    }

    timerBlock.addEventListener('DOMNodeInserted', calculateRemainingTime);

})
