function readCookie(name) {
    let nameEq = name + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEq) === 0) return c.substring(nameEq.length, c.length);
    }
    return null;
}

const CSRFToken = readCookie('csrftoken');

function postLogMessage(type, msg) {
    /* Sends logs to our backend API, which logs the message to a python logger */
    try {
        fetch('/js-logs/',
            {
                method: 'POST',
                headers: {'X-CSRFToken': CSRFToken, 'Content-Type': 'application/json'},
                body: JSON.stringify({'type': type, 'msg': msg})
            }
        );
    } catch (error) {
        console.error(error)
    }
}

// Event listener for error events for posting errors to the backend
window.addEventListener('error', (event) => {
    postLogMessage('console_error', event.message);
});

// Patch console.log function to post all other logs to the backend
console._overwritten = console.log;
console.log = function (log) {
    postLogMessage('console_log', log);
    console._overwritten(log);
};
