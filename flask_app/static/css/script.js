

let img = document.querySelector('.news0')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let image = data['articles'][0]['urlToImage']
        img.innerHTML = `<img src="${image}">`
    })
    .catch(err => console.log(err) )


let img2 = document.querySelector('.news2')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let image = data['articles'][2]['urlToImage']
        img2.innerHTML = `<img src="${image}">`
    })
    .catch(err => console.log(err) )
    

let img3 = document.querySelector('.news3')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let image = data['articles'][3]['urlToImage']
        img3.innerHTML = `<img src="${image}">`
    })
    .catch(err => console.log(err) )


let img4 = document.querySelector('.news4')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let image = data['articles'][4]['urlToImage']
        img4.innerHTML = `<img src="${image}">`
    })
    .catch(err => console.log(err) )


let img5 = document.querySelector('.news4')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let image = data['articles'][5]['urlToImage']
        img5.innerHTML = `<img src="${image}">`
    })
    .catch(err => console.log(err) )
    
    




