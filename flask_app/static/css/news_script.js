

let img = document.querySelector('.news0')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let article = data['articles']
        img.innerHTML = `<img src="${article[1]['urlToImage']}">`
        img.innerHTML += `<p>${article[1]['title']}</p>`
        img.innerHTML += `<a href=${article[1]['url']}>Link to Article</a>`
    })
    .catch(err => console.log(err) )




let img2 = document.querySelector('.news2')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let article = data['articles']
        img2.innerHTML = `<img src="${article[2]['urlToImage']}">`
        img2.innerHTML += `<p>${article[2]['title']}</p>`
        img2.innerHTML += `<a href=${article[2]['url']}>Link to Article</a>`
    })
    .catch(err => console.log(err) )
    

let img3 = document.querySelector('.news3')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let article = data['articles']
        img3.innerHTML = `<img src="${article[3]['urlToImage']}">`
        img3.innerHTML += `<p>${article[3]['title']}</p>`
        img3.innerHTML += `<a href=${article[3]['url']}>Link to Article</a>`
    })
    .catch(err => console.log(err) )


let img4 = document.querySelector('.news4')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let article = data['articles']
        img4.innerHTML = `<img src="${article[4]['urlToImage']}">`
        img4.innerHTML += `<p>${article[4]['title']}</p>`
        img4.innerHTML += `<a href=${article[4]['url']}>Link to Article</a>`
    })
    .catch(err => console.log(err) )


let img5 = document.querySelector('.news5')
fetch("https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7")
    .then(response => response.json() )
    .then(data => {
        let article = data['articles']
        img5.innerHTML = `<img src="${article[5]['urlToImage']}">`
        img5.innerHTML += `<p>${article[5]['title']}</p>`
        img5.innerHTML += `<a href=${article[5]['url']}>Link to Article</a>`
    })
    .catch(err => console.log(err) )
    
    




