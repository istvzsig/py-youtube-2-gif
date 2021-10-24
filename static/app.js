const convert_button = document.getElementById('convert_button');

async function sendDataToPy() {
    const data = await fetch('http://localhost:5555/',
        {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            },
            redirect: 'manual',
            referrerPolicy: 'no-referrer',
            body: JSON.stringify({url:'url'})
        });

        return
}

// convert_button.addEventListener('click', e => {
//
// })


var url = document.getElementById('input_for_url');
// data = url.length > 0 ? url : false;
// data ? sendDataToPy() : false;

url.addEventListener('change', e => console.log(e))


console.log(navigator)
