
const newsapi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=11b0fa8c03c0448b989105dcc2acecc7"

async function news(){
    const response = await fetch(newsapi);
    const data = await response.json();
    return data
}


async function populate(){
    const data = await news()
    var content = '';
    for(i = 1; i < 20; i ++){
        if(data['articles'][i]['urlToImage']){
            let img = document.querySelector('.newsholder');
            content += `<div id='newspage' class='news${i}'>`;
            content += `<img src="${data['articles'][i]['urlToImage']}">`;
            content += `<div id='hover'>`;
            content += `<p> ${data['articles'][i]['content']} </p> </div>`;
            content += `<div class='title2'><a href="${data['articles'][i]['url']}"><p>${data['articles'][i]['title']}</p></a></div>`;
            content += '</div>';
            img.innerHTML = content;
        }
    }
}


populate()