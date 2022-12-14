const alertPlaceholder = document.getElementById('liveAlertPlaceholder')

const alert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-fixed alert-${type} alert-dismissible d-flex align-items-center" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

document.querySelector('#addbooks').addEventListener('click', () => {
    let books = document.querySelectorAll("tr");
    let stocks = document.querySelectorAll('[name="stock"]');
    let stocksList = new Array();
    let booksList = new Array();

    let len = stocks.length;
    for (let i = 0; i < len; i++) {
        if (parseInt(stocks[i].value) > 0) {
            booksList.push(books[i+1].innerText);
            stocksList.push(stocks[i].value);
        }
    }
    if (stocksList.length === 0) {
        alert("Please enter some input in stock input fields to add books.", "warning");
        return;
    }
    
    let callURL = `${document.location.protocol}//${document.location.host}/addbooks`;
    // console.log(data);
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.post(callURL, {
        "books" : booksList,
        "stocks" : stocksList
    }).then(res => {
        if (res.data.status === "fail") {
            alert(res.data.message, "danger");
        }
        alert(res.data.message, res.data.status);
    })
})