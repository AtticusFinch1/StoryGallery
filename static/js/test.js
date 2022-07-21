const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

menuLinks = document.querySelectorAll('.menu-link')
menuLinks.forEach(link =>{
    link.addEventListener('click', function(){
        var current = document.getElementsByClassName("active");
        current[0].className=current[0].className.replace(" active", "");
        this.className += " active";
    })
})

// show sidebar
menuBtn.addEventListener('click', function(){
    sideMenu.style.display = 'block';
})

// close sidebar
closeBtn.addEventListener('click', function(){
    sideMenu.style.display = 'none';
})

// change theme
themeToggler.addEventListener('click', function(){
    document.body.classList.toggle('dark-theme-variables')
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('isactive');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('isactive')
})

const miu = document.getElementsByClassName('material-icons-sharp')
miu[6].innerHTML = "analytics"
miu[7].innerHTML = "account_balance"
miu[8].innerHTML = "movie"
miu[9].innerHTML = "book"
miu[10].innerHTML = "downhill_skiing"