let calcScrollValue = () =>{
    let scrollProgress = document.getElementById("progress");
    let progressValue = document.getElementById("progress-value");
    let pos = document.documentElement.scrollTop;

    let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);


    if(pos > 200){
        scrollProgress.style.display = "grid";
    } else {
        scrollProgress.style.display = "none";
    }
    scrollProgress.addEventListener("click", () =>{
        document.documentElement.scrollTop = 0;
    });
    scrollProgress.style.background = `conic-gradient(rgba(30, 75, 115, 1) ${scrollValue}%, rgba(255, 255, 255, 0) ${scrollValue}%)`;
};

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;


//----------------xx-------------- Load more functionality ----------------xx-----------------//
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let visible = 3
const postsBox = document.getElementById('posts-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const endBox = document.getElementById('end-box')
//const url = window.location
const url = 'http://127.0.0.1:8000/'
let page = 1;

const getData = function(page = 1){
    spinnerBox.classList.remove('not-visible');

    $.ajax({
        type: 'POST',
        url: `/data/`,
        data: {
            page,
        },
        headers: {'X-CSRFToken': csrftoken},
        success: function(response){
            spinnerBox.classList.add('not-visible');
            console.log(response)
            if (response.size ==  0 && page === 1){
                endBox.textContent = "No posts added yet..."
            }
            else if(response.size < visible){
                loadBtn.classList.add('not-visible')
                endBox.innerHTML = " ";
            }

            const data = response.data
            data.forEach(function(el){
                category = el.category
                postsBox.innerHTML += `
                    <div class="all ${category}" data-id="test-category">
                        <div class="post-img">
                            <img src="${el.image}" alt="post">
                            <a href="gallery/${el.category}" class="category-name">${el.category}</a>
                        </div>
                        <div class="post-content">
                            <div class="post-content-top">
                                <span><i class="fas fa-calendar"></i> ${el.created.slice(0,10)}</span>

                            </div>
                            <h2>${el.title}</h2><p>${el.description}...</p>
                        </div>
                        <a href="${url}post/${el.id}" type="button" class="read-btn"> Read All </a>
                    </div>
                `;
            });
    },
        error: function(err){
            spinnerBox.classList.add('not-visible');
            console.log(err)
        }
    })
}
getData()

loadBtn.addEventListener('click', function(e){
    getData(++page)
})


//-------xx------- navbar functionality -------xx-------//

const header = document.querySelector("header");
const sectionOne = document.querySelector(".home-intro");

const sectionOneOptions={
    rootMargin: "-100px 0px 0px 0px"
};
const sectionOneObserver = new IntersectionObserver(function(
    entries,
    sectionOneObserver
    ){
        entries.forEach(entry => {
            if(!entry.isIntersecting){
                header.classList.add("nav-scrolled");
            } else {
                header.classList.remove("nav-scrolled");
            }
        });
    }, sectionOneOptions);

sectionOneObserver.observe(sectionOne);