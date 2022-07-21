const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.carousel__button--right');
const prevButton = document.querySelector('.carousel__button--left');
const dotsNav = document.querySelector('.carousel__nav');
const dots = Array.from(dotsNav.children)
const url = '127.0.0.1:8000'
const window_url = window.location



const slideSize = slides[0].getBoundingClientRect(); // DOMRect {x: 201.5, y: 800, width: 888, height: 0, top: 800, …}
const slideWidth = slideSize.width;

// arrange the slides next to one  another
//slides[0].style.left = slideWidth * 0 + 'px';
//slides[1].style.left = slideWidth * 1 + 'px';
//slides[2].style.left = slideWidth * 2 + 'px';
//for(let i = 0; i < slides.length; i++){
//    slides[i].children[0].style.left = slideWidth * i + 'px';
//}
const setSlidePosition = (slide, index) => {
    slide.style.left = slideWidth * index + 'px';
}
slides.forEach(setSlidePosition);

// when i click right, move slides to the left
    const currentSlideAll = track.querySelectorAll('.carousel__slide');
    currentSlideAll[0].classList.add('current-slide');

const moveToSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = 'translateX(-' + targetSlide.style.left + ')';
    currentSlide.classList.remove('current-slide'); // current-slide is used to get the width of next slide
    targetSlide.classList.add('current-slide');
}

const updateDots = function(currentDot, targetDot){
    currentDot.classList.remove('current-slide');
    targetDot.classList.add('current-slide');
}

const hideShowArrows = function(slides, prevButton, nextButton, targetIndex){
    if (targetIndex === 0){
        prevButton.classList.add('is-hidden');
        nextButton.classList.remove('is-hidden');
    } else if (targetIndex === slides.length - 1) {
        prevButton.classList.remove('is-hidden');
        nextButton.classList.add('is-hidden');
    } else {
        prevButton.classList.remove('is-hidden');
        nextButton.classList.remove('is-hidden');
    }
}

nextButton.addEventListener('click', function(e){
    try {
        const currentSlide = track.querySelector('.current-slide');
        const nextSlide = currentSlide.nextElementSibling;
        nextSlide.classList.add('slidein')
        currentSlide.classList.remove('slidein')
        const currentDot = dotsNav.querySelector('.current-slide');
        const nextDot = currentDot.nextElementSibling;
        const nextIndex = slides.findIndex(slide => slide === nextSlide);
        moveToSlide(track, currentSlide, nextSlide);
        updateDots(currentDot, nextDot);
        hideShowArrows(slides, prevButton, nextButton, nextIndex);
    } catch(error){
        console.log('No more elements to display')
    }

//    const amountToMove = nextSlide.style.left;
//    track.style.transform = 'translateX(-' + amountToMove + ')';
//    currentSlide.classList.remove('current-slide');
//    nextSlide.classList.add('current-slide');
})

// when i click left, move slides to the right

prevButton.addEventListener('click', function(e){
   try {
       const currentSlide = track.querySelector('.current-slide');
       const prevSlide = currentSlide.previousElementSibling;
       prevSlide.classList.add('slidein')
       currentSlide.classList.remove('slidein')
       const currentDot = dotsNav.querySelector('.current-slide');
       const prevDot = currentDot.previousElementSibling;
       const prevIndex = slides.findIndex(slide => slide === prevSlide);
       hideShowArrows(slides, prevButton, nextButton, prevIndex);
       moveToSlide(track, currentSlide, prevSlide);
       updateDots(currentDot, prevDot);
   } catch(error){
       console.log('No more elements to display')
   }

//    console.log(prevSlide)
//    const amountToMove = prevSlide.style.left;
//    track.style.transform = 'translateX(-' + amountToMove + ')';
//    currentSlide.classList.remove('current-slide');
//    nextSlide.classList.add('current-slide');
})
// when i click nav indicators, move to that slide

const dotsNavAll = document.querySelectorAll(".carousel__indicator")
dotsNavAll[0].classList.add('current-slide')

dotsNav.addEventListener('click', function(e){
    const targetDot = e.target.closest('button');
    //console.log(e); // gives all the information about the dotsNav
    //console.log(e.target); tells exactly what we are clicking on
    if (!targetDot) return;

    const currentSlide = track.querySelector('.current-slide');
    const currentDot = dotsNav.querySelector('.current-slide');
    const targetIndex = dots.findIndex(dot => dot === targetDot); // find the index of each dot button
//    console.log(targetIndex); // 0,1,2
//    console.log(slides); // [li.carousel__slide.current-slide, li.carousel__slide, li.carousel__slide]
    const targetSlide = slides[targetIndex]
//    console.log(targetSlide);
    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot);
    hideShowArrows(slides, prevButton, nextButton, targetIndex);
})

//-------xx---- End of Carousel functionality -------xx--------//

const backImage = document.querySelector('.wrapper__background--image');
console.log(backImage)
category = window_url.pathname.split('/')[2];
if (category === "culture"){
    backImage.src="../images/culture_background.jpg"
} else if(category === "books"){
     backImage.src="../images/business_background.jpg"
}else if(category === "sports"){
     backImage.src="../images/sports_background.jpg"
}else if(category === "movies"){
     backImage.src="../images/Lord-Of-The-Rings.jpg"
}else if(category === "history"){
     backImage.src="../images/genghis-khan.jpg"
}

