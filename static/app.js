const converter_button = document.getElementById('convert_button');
const gif = document.getElementById('converted_gif');

function saveLastUrl(url=null) {
      return url ?
            localStorage.setItem('last-converted', url)
                  : `URL is ${url}`;
}

async function handleData(data={}) {
    return await fetch('http://localhost:5555/',
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
            body: JSON.stringify({data:
                  {

                  }

            })
        });
}

var url = document.getElementById('input_for_url');
// data = url.length > 0 ? url : false;
// data ? handleData() : false;

converter_button.addEventListener('click', e => {
      saveLastUrl();
})
