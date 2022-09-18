
const newsapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7"

async function news(){
    const response = await fetch(newsapi);
    const data = await response.json();
    return data
}



async function populate(){
    const data = await news()
    for(i = 1; i < 20; i ++){
        console.log(data['articles'][i])
        var content = '';
        let img = document.querySelector(`.news${i}`)
        content += `<img src="${data['articles'][i]['urlToImage']}">`
        content += `<p>${data['articles'][i]['title']}</p>`
        content += `<a href=${data['articles'][i]['url']}>Link to Article</a>`
        content += `<p> ${data['articles'][i]['content']}<p>`
        img.innerHTML = content;
    }
}


populate()