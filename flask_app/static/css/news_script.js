
const newsapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7"

async function news(){
    const response = await fetch(newsapi);
    const data = await response.json();
    console.log(data)
    return data
}


async function populate(){
    const data = await news()
    for(i = 1; i < 20; i ++){
        console.log(data['articles'][i])
        var content = '';
        let img = document.querySelector(`.news${i}`)
        content += `<img src="${data['articles'][i]['urlToImage']}">`
        content += `<a href="${data['articles'][i]['url']}"><p>${data['articles'][i]['title']}</p></a>`
        content += `<p> ${data['articles'][i]['content']}<p>`
        img.innerHTML = content;
    }
}


populate()